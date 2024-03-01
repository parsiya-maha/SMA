import pyAesCrypt
import os

buffer_size = 64*1024

def _encryptFile(full_path , password ):
    new_path = full_path+".aes"
    pyAesCrypt.encryptFile(full_path,new_path,password,buffer_size)

    os.remove(full_path)
    os.rename(new_path,full_path)



def _decryptFile(full_path , password):
    new_path = full_path+"_decrypted"
    pyAesCrypt.decryptFile(full_path,new_path,password,buffer_size)

    os.remove(full_path)
    os.rename(new_path,full_path)



#_encryptFile("D:\Parsia Works\python\Project\login.txt","201521784")
#_decryptFile("D:\Parsia Works\python\Project\login.txt","201521784")



