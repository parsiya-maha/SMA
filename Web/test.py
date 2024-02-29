from fastapi import FastAPI, Request
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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



@app.post("/upload")
async def upload_image(image: UploadFile = File(...), option: str = Form(...)):
    contents = await image.read()
    # Here you can do something with the image data, for example, save it to disk
    path = option + "_" + image.filename

    with open(path, "wb") as f:
        f.write(contents)