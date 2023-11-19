import numpy as np
from PIL import Image
import os
import time
from extraction_func import *
start_time = time.time()

dataset_dir = 'static/dataset/'
for images in os.listdir(dataset_dir):
    path = 'static/dataset/'
    if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
        path += str(images)
    img = Image.open(path)
    HIST = getHistogram(images)
    TextureFeature = getTextureFeature(images)
    namafile_color = "dataset_features/hsv/"+images+".npy"
    namafile_texture = "dataset_features/texture/"+images+".npy"
    np.save(namafile_color,HIST)
    np.save(namafile_texture, TextureFeature)

img_count = len(os.listdir(dataset_dir))
end_time = time.time()
execution_time = end_time - start_time
string_output = str("Extracted "+str(img_count)+" images in "+str(-1*execution_time)+" seconds")
print("Extracted %d images in %.3f seconds" % (img_count,execution_time))
