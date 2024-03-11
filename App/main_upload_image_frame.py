import customtkinter,os
from PIL import Image



def upload_image_sub_frame(master)->customtkinter.CTkLabel:

    path = os.path.join(os.getcwd(),"App\\images\\upload2.png")

    img = customtkinter.CTkImage(light_image=Image.open(path),
                                dark_image=Image.open(path),
                                size=(250, 250))

    l = customtkinter.CTkLabel(master,image=img,text="")

    return l
