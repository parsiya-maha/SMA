import customtkinter,os
from PIL import Image


def check_login_data(useername,password):
    with open(os.path.join(os.getcwd(),"App\\data.txt")) as F:
        reader = F.read()

    accs = [_ for _ in reader.strip().split("\n")]

    for acc in accs:
        if acc.split(",") == [useername,password]:
            return True

    return False


def return_login_page()->customtkinter.CTk:
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    app = customtkinter.CTkToplevel()
    app.geometry("700x400")
    app.title("Mr.Doctor - Login")


    # load image
    path = os.path.join(os.getcwd(),"App\\images\\login.png")

    login_image = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(250, 250))

    customtkinter.CTkLabel(app,image=login_image,text="").pack(side="right")

    customtkinter.CTkLabel(app,text="Mr.Doctor Login",font=("...",30,"bold")).pack(pady=(45,25))


    frame = customtkinter.CTkFrame(app,width=400)
    frame.pack(side="top",padx=15)

    # login frame
    customtkinter.CTkLabel(frame,text="username",anchor="w",font=("...",20)
    ).grid(row=0,column=0,padx=(20,30),pady=30)

    username = customtkinter.CTkEntry(frame,font=("...",20),width=250)
    username.grid(row=0,column=1,padx=(20,30),pady=(30,10))


    customtkinter.CTkLabel(frame,text="password",anchor="w",font=("...",20)
    ).grid(row=1,column=0,padx=(20,30),pady=30)

    password = customtkinter.CTkEntry(frame,font=("...",20),width=250,show="*")
    password.grid(row=1,column=1,padx=(20,30))

    def check():
        if check_login_data(username.get(),password.get()) :
            app.destroy()
            app.quit()
            

        else :
            submit_btn.configure(text="Try agine")

    submit_btn = customtkinter.CTkButton(app,
                                        text = "Submit",
                                        font = ("...",15,"bold"),
                                        width = 420,
                                        height=150,
                                        command = check)
    submit_btn.pack(pady=40)

    app.resizable(0,0)

    return app


