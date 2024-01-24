from tensorflow.keras.preprocessing.image import ImageDataGenerator
from .LoadModel import load_model
import os
import shutil
import numpy as np

# Image size
__image_size = (150, 150)

__CLASS_TYPES = ['BrainTumor', 'KidneyStone', 'LungCancer']

def __generate_image(test_dir):
    test_datagen = ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=__image_size,
        shuffle = False,
        class_mode='categorical',
        batch_size=1,
        seed=111
        )

    filenames = test_generator.filenames
    nb_samples = len(filenames)

    return test_generator,nb_samples



def __add_prepare_image(image_path):
    """
    return test dir path
    """

    test_dir = "test_dir"
    os.mkdir(test_dir)
    s_test_dir = "test2"
    os.mkdir(os.path.join(test_dir,s_test_dir))

    main_path = os.path.split(image_path)[1]

    shutil.move(image_path,os.path.join(test_dir,s_test_dir,main_path))

    return test_dir



def __delete_dir(dir_path,image_path):

    test_dir = "test_dir"
    s_test_dir = "test2"
    main_path = os.path.split(image_path)[1]
    shutil.move(os.path.join(test_dir,s_test_dir,main_path),image_path)
    
    shutil.rmtree(dir_path)



def predict_image(image_path,h5_path,json_path) :
    """
    return image type
    """
    # prepare image 
    test_dir = __add_prepare_image(image_path)

    # load model form LoadModel.py
    model = load_model(h5_path,json_path)
    test_generator,nb_samples = __generate_image(test_dir)

    # predict
    predict = model.predict_generator(test_generator,steps = nb_samples)

    # clear
    __delete_dir(test_dir,image_path)

    predict_index = np.argmax(predict)

    return __CLASS_TYPES[predict_index]



#p = predict_image(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\notumor\Te-no_0057.jpg",r"D:\Parsia Works\python\Project\AI\BrainTumors\model.h5",r"D:\Parsia Works\python\Project\AI\BrainTumors\model.json")
#print(p)