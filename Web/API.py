# ---------------------------------------------------------------------------------------- Imports

from fastapi import FastAPI, Request
from fastapi import FastAPI, File, UploadFile, Form , Body
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from SMAmodel import LoginDataset,data_path,data_password,is_image_path,image_formats

from AI.BrainTumors import BrainTumorsPredictImage
from AI.LungCancer import LungCancerPredictImage
from AI.KidneyStone import KidneyStonePredictImage
from AI.ToRecognize import ToRecognizePredictImage
from AI import ToRecognizeAndPredictImage

# ---------------------------------------------------------------------------------------- Instance vars

#make api sample
app = FastAPI()

#mount api to '/static' folder
app.mount("/static", StaticFiles(directory="static"), name="static")

#make template smaplle
templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------------------------------------------- home

@app.get("/",
        tags=["Home"],
        summary="API for start of website (home)."
        )

async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

# ---------------------------------------------------------------------------------------- started

@app.get("/templates/test-start.html",
        tags=["Login","Start"],
        summary="API for started page (login)."
        )

async def started(request : Request):
    return templates.TemplateResponse(request=request, name="test-start.html")

# ---------------------------------------------------------------------------------------- main

@app.get("/templates/main.html",
        tags=["Main"],
        summary="API for main page (AI page)."
        )

async def main(request : Request):
    return templates.TemplateResponse(request=request, name="main.html")

# ---------------------------------------------------------------------------------------- article_brain

@app.get("/templates/articlebrain.html",
        tags=["Article"],
        summary="API for /articlebrain.html page."
        )

async def article_brain(request : Request):
    return templates.TemplateResponse(request=request, name="articlebrain.html")

# ---------------------------------------------------------------------------------------- article_kidney

@app.get("/templates/articleKidney.html",
        tags=["Article"],
        summary="API for /articleKidney.html page."
        )

async def article_kidney(request : Request):
    return templates.TemplateResponse(request=request, name="articleKidney.html")

# ---------------------------------------------------------------------------------------- article_lung

@app.get("/templates/articlelung.html",
        tags=["Article"],
        summary="API for /articlelung.html page."
        )

async def article_lung(request : Request):
    return templates.TemplateResponse(request=request, name="articlelung.html")

# ---------------------------------------------------------------------------------------- upload_image

@app.post("/templates/main.html/upload",
        tags=["Upload Image"],
        summary="Upload image and give the AI result."
        )

async def upload_image(image: UploadFile = File(...), option: str = Form(...)):
    try:
        contents = await image.read()
        # Here you can do something with the image data, for example, save it to disk
        path = option + "_" + image.filename

        if not is_image_path(path):
            
            return {"massage":"ERROR (bad format of image.)","path":path,"result":f"image format\
 most be {','.join(image_formats)}"}

        with open(path, "wb") as f:
            f.write(contents)

        if option == "BrainTumors":
            from AI.BrainTumors import BrainTumorsPredictImage as predict_model

        elif option == "LungCancer":
            from AI.LungCancer import LungCancerPredictImage as predict_model

        elif option == "KidneyStone":
            from AI.KidneyStone import KidneyStonePredictImage as predict_model

        elif option == "ToRecognize":
            from AI.ToRecognize import ToRecognizePredictImage as predict_model

        elif option == "ToRecognizeAndPredict":
            from AI import ToRecognizeAndPredictImage as predict_model

        else :
            return {"massage":"ERROR in process","path":path,"result":f"No {option} model found."}

        # predict model
        res = predict_model(path)

        # remove download file
        os.remove(path)
        
        return {"massage":"Successfully","path":path,"result":res}

    except Exception as Ex:
            return {"ERROR massage":str(Ex),
            "ERROR type":Ex.__class__.__name__
            }

# ---------------------------------------------------------------------------------------- check_login_input_data

@app.post("/templates/test-start.html/login",
        tags=["Login"],
        summary="Post login data to api and check them."
        )

async def check_login_input_data(username:str = Form(...),password:str = Form(...)):
    datasets_sample = LoginDataset(data_path,data_password)

    res = datasets_sample.match_username_password(username,password)

    if res : 
        return {"massage":"Successfully login","massage_bool":True}

    return {"massage":"Username or Password was wrong","massage_bool":False}