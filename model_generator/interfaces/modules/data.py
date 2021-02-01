import os
import json

from PyQt5 import QtWidgets, QtCore, QtChart, QtGui

from base import DataSet, Project
from .module import _Module
from interfaces.modules.ui.data_ui import Ui_Form
from interfaces.dialogs.createdialog import CreateDialog
from interfaces.dialogs import ConfirmDelete
from interfaces.dialogs.addFromFolder import AddFolderDialog
from interfaces.dialogs.exportdataset import ExportDatasetDialog
from interfaces.dialogs import SimpleDialog, RemoveFolderSamplesDialog

class Data(_Module):
    moduleTitle= "Data"
    iconName = "data.png"
    shortDescription = ''' Manage your project data '''
    category = "prep"
    moduleHelp = '''
                 The data module allow you to add audio samples to your project.
                 '''

    def __init__(self, project : Project):
        _Module.__init__(self, project)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.project = project
        self.project.project_updated.connect(self.updateDisplay)
        self.currentDataset = DataSet()
        if len(self.project.datasets) > 0:
            self.currentDataset = self.project.getDatasetByName(self.project.datasets[-1])
        
        self.populateDatasetCB()

        #Chart
        self.chart = DataChart(self.currentDataset.datasetValues())
        self.ui.graphPlaceHolder.setLayout(QtWidgets.QHBoxLayout())
        self.ui.graphPlaceHolder.layout().addWidget(self.chart)

        self.updateDisplay()
        
        # CONNECT
        self.ui.currentDataSet_CB.currentTextChanged.connect(self.onDataSetChanged)
        self.currentDataset.dataset_updated.connect(self.updateDisplay)

        ## buttons
        self.ui.createDataSet_PB.clicked.connect(self.onCreateDatasetClicked)
        self.ui.delete_PB.clicked.connect(self.onDeleteDatasetClicked)
        self.ui.addFromFolder_PB.clicked.connect(self.addFromFolder)
        self.ui.export_PB.clicked.connect(self.onExportClicked)
        self.ui.import_PB.clicked.connect(self.onImportClicked)
        self.ui.remove_PB.clicked.connect(self.onRemoveClicked)

    ########################################################################
    ##### UI LOGIC
    ########################################################################

    def onCreateDatasetClicked(self):
        dialog = CreateDialog(self, self.project.datasets, "Create Dataset", "Dataset name:")
        dialog.on_create.connect(self.createNewDataSet)
        dialog.show()

    def onDataSetChanged(self, name: str):
        if name is not None and name != '':
            self.currentDataset = self.project.getDatasetByName(name)
            self.updateDisplay()

    def onDeleteDatasetClicked(self):
        dialog = ConfirmDelete(self, "Delete Dataset", "Do you want to delete", self.ui.currentDataSet_CB.currentText())
        dialog.on_delete.connect(self.deleteDataset)
        dialog.show()
    
    def onExportClicked(self):
        dialog = ExportDatasetDialog(self, self.currentDataset)
        dialog.show()


    def onRemoveClicked(self):
        dialog = RemoveFolderSamplesDialog(self, self.currentDataset.getSamplesFolders())
        dialog.on_removed.connect(self.onRemoveSamples)
        dialog.show()

    def populateDatasetCB(self):
        self.ui.currentDataSet_CB.clear()
        for ds in self.project.datasets:
            self.ui.currentDataSet_CB.addItem(ds, userData = ds)

    def updateDisplay(self):
        dataset_existing = len(self.project.datasets) > 0
        self.ui.overView_GB.setEnabled(dataset_existing)
        self.ui.add_GB.setEnabled(dataset_existing)
        self.ui.addFromMan_PB.setEnabled(False) # TODO: implement
        self.ui.export_PB.setEnabled(dataset_existing)
        self.ui.remove_PB.setEnabled(dataset_existing)
        self.ui.overview_TE.clear()
        self.ui.overview_TE.appendPlainText(self.currentDataset.datasetInfo())
        self.chart.updateChart(self.currentDataset.datasetValues())


    ########################################################################
    ##### PROCCESSING
    ########################################################################

    def addFromFolder(self):
        dialog = AddFolderDialog(self, self.currentDataset)
        dialog.addSamples.connect(self.onAddSample)
        dialog.show()

    def createNewDataSet(self, name: str):
        self.project.addNewDataSet(name)
        self.populateDatasetCB()
        self.ui.currentDataSet_CB.setCurrentText(name)
        self.updateDisplay()

    def deleteDataset(self, name: str):
        try:
            self.project.deleteDataSet(name)
        except Exception as e:
            dialog = SimpleDialog(self, "Error", str(e))
            dialog.show()
            return
        self.populateDatasetCB()
        if len(self.project.datasets) > 0:
            self.currentDataset = self.project.getDatasetByName(self.project.datasets[0])
            self.ui.currentDataSet_CB.setCurrentIndex(0)
        else:
            self.currentDataset = DataSet()
        self.updateDisplay()
        
    def onAddSample(self, label: str, files: list):
        self.currentDataset.addSampleFiles(label, files)
        self.updateDisplay()

    def onRemoveSamples(self, folders):
        self.currentDataset.removeFromFolders(folders)

    def onImportClicked(self):
        def datasetLabels(manifest):
            target_labels = set()
            for s in manifest:
                target_labels.add(s["label"])
        
            return target_labels
        
        def isMatchingFormat(manifest):
            if type(manifest) != list and type(manifest[0]) != dict:
                return False
            if "label" in manifest[0].keys() and "file" in manifest[0].keys():
                return True
            else:
                return False
        
        def matchAllLabels(target_labels, labels):
            """ The ideal case where all labels in the imported match the project labels"""
            for l in labels + ['']:
                if not l in target_labels:
                    return False
            for l in target_labels:
                if l not in labels + ['']:
                    return False
            return True
                    
        res = QtWidgets.QFileDialog.getOpenFileName(self, "Select dataset json file.", filter="json(*.json)")[0]
        if not res:
            return

        datasetName = os.path.basename(res).split('.')[0]
        with open(res, 'r') as f:
            manifest = json.load(f)
        
        if not isMatchingFormat(manifest):
            dialog = SimpleDialog(self, "Format mismatch", "Could not import from dataset manifest.\nTry using create a new dataset and use import from manifest.")
            dialog.show()
            return
        
        target_labels = datasetLabels(manifest)                   

        if matchAllLabels(target_labels, self.currentDataset.labels):
            if datasetName in self.project.datasets:
                datasetName += "_imported"
            self.project.addNewDataSet(datasetName)
            dataset = self.project.getDatasetByName(datasetName)
            dataset.importDataSet(res)
            self.populateDatasetCB()
            self.ui.currentDataSet_CB.setCurrentText(datasetName)
            self.updateDisplay()
        else:
            pass
            #TODO label matching

    
    
        

class DataChart(QtChart.QChartView):
    ''' Display data repartition as pie chart'''
    def __init__(self, data: list):
        #data: list of tuple (label, value, percent)
        QtChart.QChartView.__init__(self)
        self.pie_slices = [QtChart.QPieSlice("{}- {} ({:.2}%)".format(*d), d[1]) for d in data]

        # Pie chart
        self.pie_series = QtChart.QPieSeries()
        for pie_slice in self.pie_slices:
            self.pie_series.append(pie_slice)
        self.pie_series.setHoleSize(0)

        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart().layout().setContentsMargins(0,0,0,0)
        self.chart().setMargins(QtCore.QMargins(0,0,0,0))
        self.chart().legend().setAlignment(QtCore.Qt.AlignRight)
        self.chart().addSeries(self.pie_series)

    def updateChart(self, data: list):
        self.pie_series.clear()
        if (sum([d[1] for d in data]) > 0):
            self.pie_slices = [QtChart.QPieSlice("{}- {} ({:.2}%)".format(*d), d[1]) for d in data]
            for pie_slice in self.pie_slices:
                self.pie_series.append(pie_slice)