import os
from login import return_login_page
import customtkinter

def check_login_data(useername,password):
    with open(os.path.join(os.getcwd(),"App\\data.txt")) as F:
        reader = F.read()

    accs = [_ for _ in reader.strip().split("\n")]

    for acc in accs:
        if acc.split(",") == [useername,password]:
            return True

    return False


def is_login():
    with open(os.path.join(os.getcwd(),"App\\setting.txt")) as F:
        data = eval(F.read())

    return data["is_login"]


def change_is_login(_bool):
    with open(os.path.join(os.getcwd(),"App\\setting.txt")) as F:
        data = eval(F.read())

    data["is_login"] = _bool

    with open(os.path.join(os.getcwd(),"App\\setting.txt"),"w") as F:
        F.write(str(data))


def go_to_login_func(app:customtkinter.CTk):
    if is_login(): ...

    else : 
        app.withdraw()
        return_login_page().mainloop()
        change_is_login(True)
        app.deiconify()
        app.after(0, lambda:app.state('zoomed'))
        

