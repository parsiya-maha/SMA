import tensorflow as tf
import os




def predict_text(word:str , Nchr:int ,dir_path : str):

    """
    dir_path : C:\\one2_step -> dir_path="C:\\"
    """

    os.chdir(dir_path)

    loaded_model = tf.saved_model.load('one_step')

    states = None
    next_char = tf.constant([word])
    result = [next_char]

    for n in range(Nchr):
        next_char, states = loaded_model.generate_one_step(next_char, states=states)
        result.append(next_char)

    return tf.strings.join(result)[0].numpy().decode("utf-8")



t = predict_text("شاه",500,r"D:\Parsia Works\python\Project\AI\Shahnameh")

with open('sample.txt','w',encoding="utf-8") as F:
    F.write(t)