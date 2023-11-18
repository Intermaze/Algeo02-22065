import numpy as np
from PIL import Image
import os
import math
from numba import njit

@njit
def rgb2hsv(r,g,b):
    r = r/255 ; g=g/255 ; b=b/255
    cmax = max(r,g,b)
    cmin = min(r,g,b)
    diff = cmax-cmin
    hue = 0
    s = 0
    v = cmax
    if diff==0:
        pass
    elif cmax==r:
        hue=((g-b)/diff)%6
    elif cmax==g:
        hue=((b-r)/diff)+2
    elif cmax==b:
        hue=((r-g)/diff)+4
    hue = hue*60

    if cmax!=0:
        s = diff/cmax
    
    return hue,s,v

@njit
def rgb2hsv_nparray(arr):
    return np.array([rgb2hsv(item[0],item[1],item[2]) for sub in arr for item in sub])

@njit
def rgb2hsv_arr(arr):
    X = int(len(arr)/3)
    fillthisin = np.zeros(X)
    fillthisin2 = np.zeros(X)
    fillthisin3 = np.zeros(X)
    for i in range(0,X,1):
        h,s,v = rgb2hsv(arr[3*i],arr[(3*i)+1],arr[(3*i)+2])
        fillthisin[i] = h
        fillthisin2[i] = s
        fillthisin3[i] = v
    return fillthisin,fillthisin2,fillthisin3


def getHistogram(filename):
    path = os.getcwd()
    sizeReso = 512
    blocking = 4
    Gambar = Image.open(os.path.join(path,'static/dataset/'+filename))
    Gambar = Gambar.resize((sizeReso,sizeReso))
    hueBins = [1,25,40,120,190,270,295,315,360]
    svBins = [0,0.2,0.7,1]
    arr = np.array(Gambar)
    img = np.split(arr,blocking)
    img_hsplitted = [np.hsplit(i,blocking) for i in img]
    img_ravel = []
    for i in range(blocking):
        for j in range(blocking):
            img_ravel.append(img_hsplitted[i][j].ravel())
    hsvarr = [rgb2hsv_arr(i) for i in img_ravel]
    histogram = [np.concatenate([np.histogram(i[0],bins=hueBins)[0],np.histogram(i[1],bins=svBins)[0],np.histogram(i[2],bins=svBins)[0]]) for i in hsvarr]
    return histogram

def getHistogramFromUpload(filename):
    path = os.getcwd()
    sizeReso = 512
    blocking = 4
    Gambar = Image.open(os.path.join(path,'static/uploads/'+filename))
    Gambar = Gambar.resize((sizeReso,sizeReso))
    hueBins = [1,25,40,120,190,270,295,315,360]
    svBins = [0,0.2,0.7,1]
    arr = np.array(Gambar)
    img = np.split(arr,blocking)
    img_hsplitted = [np.hsplit(i,blocking) for i in img]
    img_ravel = []
    for i in range(blocking):
        for j in range(blocking):
            img_ravel.append(img_hsplitted[i][j].ravel())
    hsvarr = [rgb2hsv_arr(i) for i in img_ravel]
    histogram = [np.concatenate([np.histogram(i[0],bins=hueBins)[0],np.histogram(i[1],bins=svBins)[0],np.histogram(i[2],bins=svBins)[0]]) for i in hsvarr]
    return histogram


@njit
def cosineSimiliarity(vector1, vector2):
    AB = 0
    lenA = 0
    lenB = 0
    for i in range(len(vector1)):
        AB += vector1[i]*vector2[i]
    for i in range(len(vector1)):
        lenA += vector1[i]**2
    for i in range(len(vector2)):
        lenB += vector2[i]**2
    lenA = math.sqrt(lenA)
    lenB = math.sqrt(lenB)
    return AB/(lenA*lenB)

@njit
def cosineSimilarityByColor(vecA,vecB):
    similarity = 0
    elementCount = len(vecA)
    for i in range(elementCount):
        similarity+= cosineSimiliarity(vecA[i],vecB[i])
    return(similarity/elementCount)

def colorSimilarityValueAndFilename(hsvfeatures,imghist):
    key =[]
    for feat in hsvfeatures:
        similarity  = cosineSimilarityByColor(feat[0],imghist)
        if similarity>=0.6:
            key.append([round(similarity*100,3),feat[1]])
    key.sort(reverse=True)
    return key

@njit
def rgbtograyscale(r,g,b):
    return 0.299*r+0.587*g+0.114*b

@njit
def rgbtograyscale_array(array):
    return [[int(rgbtograyscale(i[0],i[1],i[2])) for i in j] for j in array]

@njit
def GCLMMat(data):
    size = 256
    framework = np.zeros((size,size))
    for i in range(0,len(data)):
        for j in range(0,len(data[0])-1):
            framework[data[i][j]-1][data[i][j+1]-1] += 1
    return framework

@njit
def symmetricGCLM(gclmmatrix):
    transposed = gclmmatrix.transpose()
    framework = transposed+gclmmatrix
    return framework

@njit
def normalizeGCLM(gclmmatrix):
    sum_content = gclmmatrix.sum()
    return gclmmatrix*(1/sum_content)

@njit
def createThreeFeature(matrixNorm):     # Create contrast, homogeneity, and entropy from normalize matrix
    contrast = 0
    homogeneity = 0
    entropy = 0
    for i in range (len(matrixNorm)):
        for j in range (len(matrixNorm[0])):
            contrast = float(contrast + matrixNorm[i][j]*(i-j)*(i-j))
            homogeneity = float(homogeneity + (matrixNorm[i][j]/(1+(i-j)*(i-j))))
            if matrixNorm[i][j] != 0:
                entropy = float(entropy + (matrixNorm[i][j]*(math.log(matrixNorm[i][j]))))
    entropy *= -1
    return [contrast, homogeneity, entropy]

def getTextureFeature(filename):    
    path = os.getcwd()
    image = Image.open(os.path.join(path, 'static/dataset/'+filename))
    image = np.array(image)
    dataset_grayscale_matrix = np.array(rgbtograyscale_array(image))
    dataset_glcm_matrix = GCLMMat(dataset_grayscale_matrix)
    dataset_symmetric_matrix = symmetricGCLM(dataset_glcm_matrix)
    dataset_normalized_matrix = normalizeGCLM(dataset_symmetric_matrix)
    dataset_feature = createThreeFeature(dataset_normalized_matrix)
    return dataset_feature

def getTextureFeatureFromUpload(filename):
    path = os.getcwd()
    image = Image.open(os.path.join(path, 'static/uploads/'+filename))
    image = np.array(image)
    dataset_grayscale_matrix = np.array(rgbtograyscale_array(image))
    dataset_glcm_matrix = GCLMMat(dataset_grayscale_matrix)
    dataset_symmetric_matrix = symmetricGCLM(dataset_glcm_matrix)
    dataset_normalized_matrix = normalizeGCLM(dataset_symmetric_matrix)
    dataset_feature = createThreeFeature(dataset_normalized_matrix)
    return dataset_feature

def getAllCosineSimiliarity(dataset_texture_features, main_img):
    key =[]
    for feat in dataset_texture_features:
        similarity  = cosineSimiliarity(feat[0],main_img)
        if similarity>=0.6:
            key.append([100*similarity,feat[1]])
    key.sort(reverse=True)
    return key