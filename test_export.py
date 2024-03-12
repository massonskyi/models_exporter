from export import *
from rename_dataset import rename_images
import os

# rename_images("./dataset/images/") # dataset for rknn quantization

export = Export("best(1).pt", os.getcwd())
export.export("tflite", int8=True)
export.convert2rknn("tflite")
