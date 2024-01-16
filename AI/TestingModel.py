from BrainTumors import BrainTumorsPredictImage
from LungCancer import LungCancerPredictImage
import os
import time

def clear(): os.system("cls" or "clear")

start = time.time()
anser1 = BrainTumorsPredictImage(r"D:\Parsia Works\python\Project\AI\BrainTumors\datasets\Testing\notumor\Te-no_0144.jpg")
_time1 = time.time() - start


start = time.time()
anser2 = LungCancerPredictImage(r"D:\Parsia Works\python\Project\AI\TestingData\Lung-Benign_Tissue.jpeg")
_time2 = time.time() - start

os.system("cls" or "clear")


print(30*"-")
print()
print(f"Time    : {_time1}")
print(f"Predict : {anser1}")
print()
print(30*"-")
print()
print(f"Time    : {_time2}")
print(f"Predict : {anser2}")
print()
print(30*"-")

# OUTPUT:
# ------------------------------
# 
# Time    : 1.099116325378418
# Predict : notumor
# 
# ------------------------------
# 
# Time    : 0.705603837966919
# Predict : Lung-Benign_Tissue
# 
# ------------------------------

