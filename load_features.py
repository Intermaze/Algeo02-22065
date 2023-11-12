import os
import numpy as np

def load_array():
    features_dir = 'dataset_features/hsv/'
    array_of_hsvfeatures = []
    for features in os.listdir(features_dir):
        namafileHSV = features_dir+features
        feat = np.load(namafileHSV)
        array_of_hsvfeatures.append([feat,features[:-4]])
    return array_of_hsvfeatures

def del_hsv():
    for item in os.listdir('dataset_features/hsv/'):
        os.remove('dataset_features/hsv/'+item)

def del_texture():
    for item in os.listdir('dataset_features/texture/'):
        os.remove('dataset_features/texture/'+item)