# **Having a project in the local space**
---
###### You have two solutions :
###### `1.` On the main page of the project (on GitHub), click the Code button and then in the box that opens, click the last option, Download ZIP, to start downloading the zip file of the project for you.
###### For example, in the image below:

![download zip](https://raw.githubusercontent.com/parsiya-maha/SMA/master/ForReadMe/DownloadZipGitHub.jpg)
---

###### `2.` In the second solution, first you must have installed the git program and then copy the project address as shown in the picture below:

![project url](https://raw.githubusercontent.com/parsiya-maha/SMA/master/ForReadMe/GitProjectUrl.jpg)

###### Then open your cmd and type the following code (Before running the code, go to the desired address to install the project there):

```cmd
git clone https://github.com/parsiya-maha/SMA.git
```


# **How to use AI from SMA**
---
###### `AI` Library has classes for various tumors and cancers. Each of the classes has a method for predicting images, whose names can be obtained from the following way:

`method name` = `(The name of the disease)` + `"PredictImage"`

###### for example :
```py
from AI.BrainTumors import BrainTumorsPredictImage
from AI.LungCancer import LungCancerPredictImage
from AI.KidneyStone import KidneyStonePredictImage
```

###### The only input these methods ask for is the address of the desired photo for prediction.
```py
# path for Brain Tumor
path1 : str = ...
# path for Lung Cancer
path2 : str = ...
# path for Kidney Stone
path3 : str = ...

res1 = BrainTumorsPredictImage(path1)
res2 = LungCancerPredictImage(path2)
res3 = KidneyStonePredictImage(path3)
```

###### Also, each of them has a method that returns their compiled model. For them, the following method should be used to obtain their names:

`method name` = `(The name of the disease)` + `"LoadModel"`

###### for example :
```py
from AI.BrainTumors import BrainTumorsLoadModel
from AI.LungCancer import LungCancerLoadModel
from AI.KidneyStone import KidneyStoneLoadModel
```

###### But another possibility of our program is to diagnose the disease, that is, which cancer or tumor this photo is related to, you can use the `ToRecognize` class from the `AI` section:

```py
from AI.ToRecognize import ToRecognizePredictImage
from AI.ToRecognize import ToRecognizeLoadModel

res = ToRecognizePredictImage(image_path : str)
```

###### The second line of code is related to loading the model. As you can see, we only need the photo storage address for prediction.

###### But this is not the end of the work and we made a combination of ToRecognize model and cancer detection models (`Brain Tunors` , `Kidney Stone` and `Lung Cancer`) which works as a pipeline:

###### `1.` First, the photo is entered into the ToRecognize model and the type of cancer is determined.
###### `2.` Now that the type of cancer is known, the photo goes to the model related to the disease and then the exact form of the cancer is known.

###### For better understanding, this pipeline works like this:
```py
                                   | BrainTumors |
pipeline(img) = ToRecognize(img) + | KidneyStone | models
                                   | LungCancer  |
```

###### In fact, the output of the ToRecognize model along with the photo itself becomes the inputs of three other models :
```py
                                  | BrainTumors |
ToRecognizeAndPredictImage(img) = | KidneyStone | ( img , ToRecognize(img) )
                                  | LungCancer  |
```

###### But you can use this feature with this piece of code:
```py
from AI import ToRecognizeAndPredictImage

res = ToRecognizeAndPredictImage(image_path : str)
```
###### As you can see, the `ToRecognizeAndPredictImage` function has only one input, which is the photo address.

---
###### But the layout of each layer in all models is as follows:
![model layer](https://raw.githubusercontent.com/parsiya-maha/SMA/master/ForReadMe/model%20layer.png)
###### As you can see, we have used layers `Conv2D` ,`MaxPooling2D` ,`Flatten` ,`Dense` and `Dropout`.

