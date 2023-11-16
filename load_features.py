import os
import numpy as np

def load_array_hsv():
    features_dir = 'dataset_features/hsv/'
    array_of_hsvfeatures = []
    for features in os.listdir(features_dir):
        namafileHSV = features_dir+features
        feat = np.load(namafileHSV)
        array_of_hsvfeatures.append([feat,features[:-4]])
    return array_of_hsvfeatures

def load_array_texture():
    features_dir = 'dataset_features/texture/'
    array_of_texture_features = []
    for features in os.listdir(features_dir):
        namafile_texture = features_dir+features
        feat = np.load(namafile_texture)
        array_of_texture_features.append([feat,features[:-4]])
    return array_of_texture_features

def del_hsv():
    for item in os.listdir('dataset_features/hsv/'):
        os.remove('dataset_features/hsv/'+item)

def del_texture():
    for item in os.listdir('dataset_features/texture/'):
        os.remove('dataset_features/texture/'+item)