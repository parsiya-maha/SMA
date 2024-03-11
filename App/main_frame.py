import customtkinter,os
from PIL import Image
from funcs import go_to_login_func




def brain_image_label(master)->customtkinter.CTkLabel:
    path = os.path.join(os.getcwd(),"App\\images\\home.png")

    my_image = customtkinter.CTkImage(light_image=Image.open(path),
                                  dark_image=Image.open(path),
                                  size=(500, 500))
    label = customtkinter.CTkLabel(master,image=my_image,text="")
    return label


text1 = """
Mr.Doctor Login
"""

def text1_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text1,
#                                justify='left',
                                font=("calibri",60,"bold"))
    return text


text2 = """
You must purchase a subscription 
to use Mr.Doctor, in order not to 
violate the rights of those who 
have purchased a subscription, 
you must first purchase a subscription 
and then enter your username and 
password in the main section of 
the program.
All features of the program are 
free for those who have purchased 
a subscription. 

"""


def text2_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text2,
                                justify='left',
                                font=("calibri",20))
    return text



def main_login(master,app)->customtkinter.CTkButton:
    return customtkinter.CTkButton(master,
                                   text="Login",
                                   font=("zv xcv",20,"bold"),
                                   height=60,
                                   corner_radius=30,
                                   command=lambda: go_to_login_func(app))


text3 = "\nCopyright © 2024 by Mr.Doctor | All Rights Reserved.\n"

def text3_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text3,
#                                justify='left',
                                font=("calibri",12,"italic"))
    return text