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
    Gambar = Image.open(os.path.join(path, 'static/dataset/'+filename))
    Gambar = Gambar.resize((510,510))

    arr = np.array(Gambar)
    img3r = np.split(arr,3)
    img_r1 = np.hsplit(img3r[0],3)
    img_r2 = np.hsplit(img3r[1],3)
    img_r3 = np.hsplit(img3r[2],3)
    
    img_1 = img_r1[0].ravel()
    img_2 = img_r1[1].ravel()
    img_3 = img_r1[2].ravel()
    img_4 = img_r2[0].ravel()
    img_5 = img_r2[1].ravel()
    img_6 = img_r2[2].ravel()
    img_7 = img_r3[0].ravel()
    img_8 = img_r3[1].ravel()
    img_9 = img_r3[2].ravel()

    h1,s1,v1 = rgb2hsv_arr(img_1)
    h2,s2,v2 = rgb2hsv_arr(img_2)
    h3,s3,v3 = rgb2hsv_arr(img_3)
    h4,s4,v4 = rgb2hsv_arr(img_4)
    h5,s5,v5 = rgb2hsv_arr(img_5)
    h6,s6,v6 = rgb2hsv_arr(img_6)
    h7,s7,v7 = rgb2hsv_arr(img_7)
    h8,s8,v8 = rgb2hsv_arr(img_8)
    h9,s9,v9 = rgb2hsv_arr(img_9)

    hueBins = [1,25,40,120,190,270,295,315,360]
    svBins = [0,0.2,0.7,1]

    h1b = np.histogram(h1,bins=hueBins)
    h2b = np.histogram(h2,bins=hueBins)
    h3b = np.histogram(h3,bins=hueBins)
    h4b = np.histogram(h4,bins=hueBins)
    h5b = np.histogram(h5,bins=hueBins)
    h6b = np.histogram(h6,bins=hueBins)
    h7b = np.histogram(h7,bins=hueBins)
    h8b = np.histogram(h8,bins=hueBins)
    h9b = np.histogram(h9,bins=hueBins)

    s1b = np.histogram(s1,bins=svBins)
    v1b = np.histogram(v1,bins=svBins)
    s2b = np.histogram(s2,bins=svBins)
    v2b = np.histogram(v2,bins=svBins)
    s3b = np.histogram(s3,bins=svBins)
    v3b = np.histogram(v3,bins=svBins)
    s4b = np.histogram(s4,bins=svBins)
    v4b = np.histogram(v4,bins=svBins)
    s5b = np.histogram(s5,bins=svBins)
    v5b = np.histogram(v5,bins=svBins)
    s6b = np.histogram(s6,bins=svBins)
    v6b = np.histogram(v6,bins=svBins)
    s7b = np.histogram(s7,bins=svBins)
    v7b = np.histogram(v7,bins=svBins)
    s8b = np.histogram(s8,bins=svBins)
    v8b = np.histogram(v8,bins=svBins)
    s9b = np.histogram(s9,bins=svBins)
    v9b = np.histogram(v9,bins=svBins)


    hsv1 = np.concatenate([h1b[0],s1b[0],v1b[0]])
    hsv2 = np.concatenate([h2b[0],s2b[0],v2b[0]])
    hsv3 = np.concatenate([h3b[0],s3b[0],v3b[0]])
    hsv4 = np.concatenate([h4b[0],s4b[0],v4b[0]])
    hsv5 = np.concatenate([h5b[0],s5b[0],v5b[0]])
    hsv6 = np.concatenate([h6b[0],s6b[0],v6b[0]])
    hsv7 = np.concatenate([h7b[0],s7b[0],v7b[0]])
    hsv8 = np.concatenate([h8b[0],s8b[0],v8b[0]])
    hsv9 = np.concatenate([h9b[0],s9b[0],v9b[0]])

    return np.array([hsv1,hsv2,hsv3,hsv4,hsv5,hsv6,hsv7,hsv8,hsv9])

def getHistogramFromUpload(filename):
    path = os.getcwd()
    Gambar = Image.open(os.path.join(path, 'static/uploads/'+filename))
    Gambar = Gambar.resize((510,510))

    arr = np.array(Gambar)
    img3r = np.split(arr,3)
    img_r1 = np.hsplit(img3r[0],3)
    img_r2 = np.hsplit(img3r[1],3)
    img_r3 = np.hsplit(img3r[2],3)
    
    img_1 = img_r1[0].ravel()
    img_2 = img_r1[1].ravel()
    img_3 = img_r1[2].ravel()
    img_4 = img_r2[0].ravel()
    img_5 = img_r2[1].ravel()
    img_6 = img_r2[2].ravel()
    img_7 = img_r3[0].ravel()
    img_8 = img_r3[1].ravel()
    img_9 = img_r3[2].ravel()

    h1,s1,v1 = rgb2hsv_arr(img_1)
    h2,s2,v2 = rgb2hsv_arr(img_2)
    h3,s3,v3 = rgb2hsv_arr(img_3)
    h4,s4,v4 = rgb2hsv_arr(img_4)
    h5,s5,v5 = rgb2hsv_arr(img_5)
    h6,s6,v6 = rgb2hsv_arr(img_6)
    h7,s7,v7 = rgb2hsv_arr(img_7)
    h8,s8,v8 = rgb2hsv_arr(img_8)
    h9,s9,v9 = rgb2hsv_arr(img_9)

    hueBins = [1,25,40,120,190,270,295,315,360]
    svBins = [0,0.2,0.7,1]

    h1b = np.histogram(h1,bins=hueBins)
    h2b = np.histogram(h2,bins=hueBins)
    h3b = np.histogram(h3,bins=hueBins)
    h4b = np.histogram(h4,bins=hueBins)
    h5b = np.histogram(h5,bins=hueBins)
    h6b = np.histogram(h6,bins=hueBins)
    h7b = np.histogram(h7,bins=hueBins)
    h8b = np.histogram(h8,bins=hueBins)
    h9b = np.histogram(h9,bins=hueBins)

    s1b = np.histogram(s1,bins=svBins)
    v1b = np.histogram(v1,bins=svBins)
    s2b = np.histogram(s2,bins=svBins)
    v2b = np.histogram(v2,bins=svBins)
    s3b = np.histogram(s3,bins=svBins)
    v3b = np.histogram(v3,bins=svBins)
    s4b = np.histogram(s4,bins=svBins)
    v4b = np.histogram(v4,bins=svBins)
    s5b = np.histogram(s5,bins=svBins)
    v5b = np.histogram(v5,bins=svBins)
    s6b = np.histogram(s6,bins=svBins)
    v6b = np.histogram(v6,bins=svBins)
    s7b = np.histogram(s7,bins=svBins)
    v7b = np.histogram(v7,bins=svBins)
    s8b = np.histogram(s8,bins=svBins)
    v8b = np.histogram(v8,bins=svBins)
    s9b = np.histogram(s9,bins=svBins)
    v9b = np.histogram(v9,bins=svBins)


    hsv1 = np.concatenate([h1b[0],s1b[0],v1b[0]])
    hsv2 = np.concatenate([h2b[0],s2b[0],v2b[0]])
    hsv3 = np.concatenate([h3b[0],s3b[0],v3b[0]])
    hsv4 = np.concatenate([h4b[0],s4b[0],v4b[0]])
    hsv5 = np.concatenate([h5b[0],s5b[0],v5b[0]])
    hsv6 = np.concatenate([h6b[0],s6b[0],v6b[0]])
    hsv7 = np.concatenate([h7b[0],s7b[0],v7b[0]])
    hsv8 = np.concatenate([h8b[0],s8b[0],v8b[0]])
    hsv9 = np.concatenate([h9b[0],s9b[0],v9b[0]])

    return np.array([hsv1,hsv2,hsv3,hsv4,hsv5,hsv6,hsv7,hsv8,hsv9])


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
    sim_1 = cosineSimiliarity(vecA[0],vecB[0])
    sim_2 = cosineSimiliarity(vecA[1],vecB[1])
    sim_3 = cosineSimiliarity(vecA[2],vecB[2])
    sim_4 = cosineSimiliarity(vecA[3],vecB[3])
    sim_5 = cosineSimiliarity(vecA[4],vecB[4])
    sim_6 = cosineSimiliarity(vecA[5],vecB[5])
    sim_7 = cosineSimiliarity(vecA[6],vecB[6])
    sim_8 = cosineSimiliarity(vecA[7],vecB[7])
    sim_9 = cosineSimiliarity(vecA[8],vecB[8])
    return((sim_1+sim_2+sim_3+sim_4+sim_5+sim_6+sim_7+sim_8+sim_9)/9)

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
    return 0.29*r+0.587*g+0.114*b

@njit
def rgbtograyscale_array(array):
    return [[int(rgbtograyscale(i[0],i[1],i[2])) for i in j] for j in array]

@njit
def GCLMMat(data):
    size = data.max()
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
            key.append([round(similarity*100,3),feat[1]])
    key.sort(reverse=True)
    return key