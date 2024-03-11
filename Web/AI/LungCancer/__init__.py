"""
Most be 'model.json' and 'model.h5' in this cwd.
"""

from .PredictImage import predict_image
from .LoadModel import load_model
import os

base_path = os.path.join(os.getcwd(),"AI\LungCancer")

model_json = os.path.join(base_path,"model.json")
model_h5 = os.path.join(base_path,"model.h5")

def LungCancerLoadModel():
    return load_model(model_h5,model_json)

def LungCancerPredictImage(image_path:str):
    return predict_image(image_path,model_h5,model_json)
