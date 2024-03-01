import os
import re


def get_system_ip():
    file_name = "output.txt"
    os.system("ipconfig > " + file_name)

    with open(file_name) as F:
        read = F.read()

    os.remove(file_name)

    pattern = """   IPv4 Address. . . . . . . . . . . : (.+)
   """

    try:
        return re.findall(pattern,read)[0]
    except :
        return None

