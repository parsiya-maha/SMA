"""
Most be 'model.json' and 'model.h5' in this cwd.
"""

from .PredictImage import predict_image
import os

base_path = r"D:\Parsia Works\python\Project\AI\KidneyStone"

model_json = os.path.join(base_path,"model.json")
model_h5 = os.path.join(base_path,"model.h5")

def KidneyStonePredictImage(image_path:str):
    return predict_image(image_path,model_h5,model_json)
