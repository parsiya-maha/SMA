from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field
import base64,cv2,os
import numpy as np

from AI.BrainTumors import BrainTumorsPredictImage
from AI.LungCancer import LungCancerPredictImage
from AI.KidneyStone import KidneyStonePredictImage
from AI.ToRecognize import ToRecognizePredictImage
from AI import ToRecognizeAndPredictImage


app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/upload")
async def upload():
    return {"message": "Hello World"}





class ImageModel(BaseModel):
    image_string: str = Field(..., example="base64 encoded string")

    @property
    def decode_image(self):
        try:
            return base64.b64decode(self.image_string)
        except Exception:
            raise ValueError("Invalid base64 string")

class ResponseModel(BaseModel):
    data: dict
    message: str
    HTTPstatus: int

@app.post("/uploadfiles", response_model=ResponseModel)
async def upload_files(image: ImageModel , model : str , _type):

    try:
        # read image
        nparr = np.frombuffer(image.decode_image, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # save image
        cv2.imwrite("LoadedImage.png",image_rgb)



        if model == "BrainTumors" : 
            from AI.BrainTumors import BrainTumorsPredictImage as predict_func

        elif model == "LungCancer":
            from AI.LungCancer import LungCancerPredictImage as predict_func

        elif model == "KidneyStone":
            from AI.KidneyStone import KidneyStonePredictImage as predict_func

        elif model == "ToRecognize":
            from AI.ToRecognize import ToRecognizePredictImage as predict_func

        elif model == "ToRecognizeAndPredict" :
            from AI import ToRecognizeAndPredictImage as predict_func


        res = predict_func("LoadedImage.png")
        os.remove("LoadedImage.png")

        result = {
            "result": res
        }

        return {"data": result, "message": "Success", "HTTPstatus": 200}


    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid base64 string")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))