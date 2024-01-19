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
# path for brain Tumor
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

###### But the layout of each layer in all models is as follows:
---
![model layer](https://raw.githubusercontent.com/parsiya-maha/SMA/master/ForReadMe/model%20layer.png)
######
---
###### As you can see, we have used layers `Conv2D` ,`MaxPooling2D` ,`Flatten` ,`Dense` and `Dropout`.

