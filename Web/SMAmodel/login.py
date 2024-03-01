from .lock_file_AES import _encryptFile,_decryptFile


data_path = r"D:\Parsia Works\python\Project\login.txt"
data_password = "201521784"


class LoginDataset :

    def __init__(self,path:str,password):
        self.__p = path
        self.__password = password

    def __retrun_data(self):
        # decode data file
        #_decryptFile(self.__p,self.__password)

        with open(self.__p) as F:
            return_data = F.read().split("\n")

        #_encryptFile(self.__p,self.__password)

        return return_data

    
    def match_username_password(self,username:str,user_password:str) -> bool:
        user_password = str(user_password)
        username = str(username)

        for d in self.__retrun_data():

            if d.split(",") == [username,user_password]:
                return True

        return False





def make_sample_data():
    with open(data_path,"w") as F:
        F.write("parsiya,1234\nmehdi,4321")

    _encryptFile(data_path,data_password)