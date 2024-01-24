from . import BrainTumors
from . import LungCancer
from . import KidneyStone
from . import ToRecognize


def ToRecognizeAndPredictImage(image_path:str):
    rec = ToRecognize.ToRecognizePredictImage(image_path)

    # cancers ->  ['BrainTumor', 'KidneyStone', 'LungCancer']

    if rec == 'BrainTumor' :
        from .BrainTumors import BrainTumorsPredictImage as predict_func

    elif rec == 'KidneyStone' :
        from .KidneyStone import KidneyStonePredictImage as predict_func

    elif rec == 'LungCancer' :
        from .LungCancer import LungCancerPredictImage as predict_func


    return predict_func(image_path)