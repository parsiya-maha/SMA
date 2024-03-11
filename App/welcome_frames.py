import customtkinter
import webbrowser
from funcs import go_to_login_func


welcome_text1 = """
We are Mr.Doctor
Welcome to our project.

We are working on 3 models :

    - Brain Tumors
    - Kidney Stone
    - Lung Cancer

And 2 sub model but practical :

    - To Recognize
    - To Recognize And Predict

We can said To 
'Recognize And Predict' model
is one pipeline of 'To Recognize' model 
and last 3 models.

click for more about models :
"""



def option_frame_text1(master)->customtkinter.CTkFrame :
    text = customtkinter.CTkLabel(master,
                                text=welcome_text1,
                                justify='left',
                                font=("calibri",15))
    return text


def more_info_btn(master)->customtkinter.CTkButton:

    btn = customtkinter.CTkButton(master,
            text="more info",
            command=lambda : webbrowser.open("https://github.com/parsiya-maha/SMA/blob/master/README.md"))

    return btn


welcome_text2 = """
Mr.Doctor tried to make our models as 
efficient as possible.

To use all 5 models, login first.
"""

def option_frame_text2(master)->customtkinter.CTkFrame :
    text = customtkinter.CTkLabel(master,
                                text=welcome_text2,
                                justify='left',
                                font=("calibri",15))
    return text


def go_to_login(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Login",
                                 command=lambda :go_to_login_func(app))     
    return btn


welcome_text3 = """
We hope you enjoy our app.                    
- Parsiya Hassanzadeh
- Mohamad Mehdi Khodaie
"""


def option_frame_text3(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=welcome_text3,
                                justify='left',
                                font=("calibri",15))
    return text



