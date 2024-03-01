import requests

def get_image(url:str,path_to_save:str):
    """
    **path_to_save** : with jpg 
    """
    img_data = requests.get(url).content
    with open(path_to_save, 'wb') as handler:
        handler.write(img_data)



#get_image("https://raw.githubusercontent.com/parsiya-maha/SMA/master/ForReadMe/model%20layer.png",
#"sample.jpg"
#)