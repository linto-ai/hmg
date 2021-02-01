import json

from tensorflow.keras.models import Sequential, save_model
from tensorflow.keras.layers import Dense, GRU


class _Layer:
    name = None
    def __init__(self, is_input: bool = False, is_output: bool = False, is_required: bool = False):
        self.is_input = is_input
        self.is_output = is_output
        self.is_required = is_required

    def toDict(self) -> dict:
        layer_dict = dict()
        layer_dict["type"] = self.name
        layer_dict["is_input"] = self.is_input
        layer_dict["is_output"] = self.is_output
        layer_dict["is_required"] = self.is_required
        return layer_dict

    def loadValue(self, values: dict):
        for key in values.keys():
            if key in _Layer.__dict__.keys():
                self.__setattr__(key, values[key])
    
    def getEditableParameters(self) -> dict:
        ''' Return configurables parameters and types for ListItem creation'''
        return list()

    def getKerasLayer(self, input_shape = None):
        pass

    def toShortDesc(self) -> str:
        return "Abstract layer"
        
class GRU_Layer(_Layer):
    name = "gru"
    gru_act = ["linear", "tanh"]
    def __init__(self,
                 n_cell: int = 30,
                 activation_fun: str = "linear",
                 is_input: bool = True, 
                 is_output: bool = False,
                 unroll: bool = False,
                 reset_after: bool = True,
                 is_required: bool = False):
        _Layer.__init__(self, is_input, is_output, is_required)
        
        self.n_cell = n_cell
        self.activation_fun = activation_fun
        self.unroll = unroll
        self.reset_after = reset_after
    
    def toDict(self) -> dict:
        layer_dict = _Layer.toDict(self)
        layer_dict["n_cell"] = self.n_cell
        layer_dict["activation_fun"] = self.activation_fun
        layer_dict["unroll"] = self.unroll
        layer_dict["reset_after"] = self.reset_after
        return layer_dict

    def loadValue(self, values: dict):
        _Layer.loadValue(self, values)
        for key in values.keys():
            if key in GRU_Layer.__dict__.keys():
                self.__setattr__(key, values[key])
                
    def getEditableParameters(self) -> dict:
        ''' Return configurables parameters and types for ListItem creation'''
        params = []
        params.append(("n_cell", int, self.n_cell))
        params.append(("activation_fun", list, self.activation_fun, GRU_Layer.gru_act))
        params.append(("unroll", bool, self.unroll))
        params.append(("reset_after", bool, self.reset_after))
        return params

    def getKerasLayer(self, input_shape = None):
        if input_shape is None:
            return GRU(self.n_cell,
                        activation=self.activation_fun,
                        name="input" if self.is_input else self.name,
                        unroll=self.unroll,
                        reset_after=self.reset_after)
        else:
            return GRU(self.n_cell,
                        activation=self.activation_fun,
                        input_shape=input_shape,
                        name="input" if self.is_input else self.name,
                        unroll=self.unroll,
                        reset_after=self.reset_after)
    
    def toShortDesc(self) -> str:
        return "GRU Layer {} cells ({})".format(self.n_cell, self.activation_fun)

class Dense_Layer(_Layer):
    name = "dense"
    dense_act = ["relu", "sigmoid", "linear"]
    def __init__(self,
                 n_cell: int = 30,
                 activation_fun: str = "relu",
                 is_input: bool = True, 
                 is_output: bool = False,
                 is_required: bool = False):
        _Layer.__init__(self, is_input, is_output, is_required)
        self.n_cell = n_cell
        self.activation_fun = activation_fun
        
    def toDict(self) -> dict:
        layer_dict = _Layer.toDict(self)
        layer_dict["n_cell"] = self.n_cell
        layer_dict["activation_fun"] = self.activation_fun
        return layer_dict
    
    def getEditableParameters(self) -> dict:
        ''' Return configurables parameters and types for ListItem creation'''
        params = []
        params.append(("n_cell", int, self.n_cell))
        params.append(("activation_fun", list, self.activation_fun, Dense_Layer.dense_act))
        return params

    def getKerasLayer(self, input_shape = None):
        return Dense(units=self.n_cell, activation=self.activation_fun)

    def toShortDesc(self) -> str:
        return "Dense Layer {} cells ({})".format(self.n_cell, self.activation_fun)

class Output_Layer(_Layer):
    name = "output"
    def __init__(self, 
                 n_cell,
                 activation_fun: str = "sigmoid",
                 is_input: bool = True, 
                 is_output: bool = False,
                 is_required: bool = True):
        _Layer.__init__(self, is_input, is_output, is_required)
        self.activation_fun = activation_fun
        self.n_cell = n_cell
        
    def toDict(self) -> dict:
        layer_dict = _Layer.toDict(self)
        layer_dict["n_cell"] = self.n_cell
        layer_dict["activation_fun"] = "sigmoid"
        return layer_dict

    def getKerasLayer(self, input_shape = None):
        return Dense(units=self.n_cell, activation=self.activation_fun, name="output")
    
    def toShortDesc(self) -> str:
        return "Output Layer"

class _Model:
    allowed_layers = []
    allowed_optimizer = []
    allowed_loss_fun = []
    def __init__(self, name: str):
        self.modelPath = ''
        self.name = name
        self.type = "void"
        self.layers = []
        self.optimizer = None
        self.loss = "mean_squared_error"
        self.metrics = ["accuracy"]
        
    def toDict(self) -> dict:
        manifest = dict()
        manifest["name"] = self.name
        manifest["type"] = self.type
        manifest["layers"] = [l.toDict() for l in self.layers]
        return manifest
    
    def loadModel(self, modelPath: str):
        pass

    def writeModel(self, modelPath: str = None):
        if modelPath is None:
            modelPath = self.modelPath
        manifest = self.toDict()
        try:
            with open(modelPath, 'w') as f:
                json.dump(manifest, f)
        except Exception as e:
            raise Exception("Could not write model at {}: {}".format(modelPath, e))
    
    def toKerasModel(self, input_shape: tuple, output_shape: int) -> Sequential:
        model = Sequential()
        model.add(self.layers[0].getKerasLayer(input_shape=input_shape))
        for layer in self.layers[1:-1]:
            model.add(layer.getKerasLayer())
        self.layers[-1].n_cell = output_shape
        model.add(self.layers[-1].getKerasLayer())
        model.compile(self.optimizer, loss=self.loss, metrics=self.metrics)
        return model

    def toShortDesc(self) -> str:
        desc = "Model {}\nLayers:\n".format(self.name)
        for layer in self.layers:
            desc.append("{}\n".format(layer.toShortDesc()))
        return desc

class GRU_Model(_Model):
    allowed_layers = ["gru", "dense"]
    allowed_optimizer = ["rmsprop"]
    allowed_loss_fun = ["mean_squared_error"]
    def __init__(self, name: str = "", layers: list = None):
        _Model.__init__(self, name)
        self.type = "gru"
        self.optimizer = "rmsprop"
        self.layers = [
            GRU_Layer(is_input=True, is_required=True),
            Dense_Layer(is_input=False),
            Output_Layer(1)
        ]

    def loadModel(self, modelPath: str):
        self.layers = []
        try:
            with open(modelPath, "r") as f:
                manifest = json.load(f)
        except:
            raise Exception("Could not read model manifest at {}".format(modelPath))
        try:
            self.name = manifest["name"]
            for layer in manifest["layers"]:
                layer_type = layer.pop("type")
                self.layers.append(getLayerbyType(layer_type)(**layer))
        except Exception as e:
            raise Exception("Cannot load model at {} wrong format".format(modelPath))


def getModelbyType(model_type) -> _Model:
    if model_type == "gru":
        return GRU_Model
    else:
        raise Exception("Error: Model {} not known.".format(model_type))

def getLayerbyType(layer_type) -> _Layer:
    if layer_type == "gru":
        return GRU_Layer
    elif layer_type == "dense":
        return Dense_Layer
    elif layer_type == "output":
        return Output_Layer
    else:
        raise Exception("Error: Layer {} not known.".format(layer_type))

def saveModel(model, path):
    save_model(model, path)