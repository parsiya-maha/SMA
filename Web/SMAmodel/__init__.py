from .login import LoginDataset,data_password,data_path
import os

image_formats = [
    ".png",
    ".jpeg",
    ".jpg"
]

def is_image_path(path:str) : return os.path.splitext(path)[1] in image_formats