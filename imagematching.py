# -*- coding: UTF-8 -*-


import cv2
import numpy as np


 #perceputal hash algorithm
def pHash(image):
    image = cv2.resize(image,(32,32), interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('image', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    # convert the gray to float
    dct = cv2.dct(np.float32(image))
#     print(dct)
    # The 8*8 values on the left corner represents the lowest frequency of the image.
    dct_roi = dct[0:8,0:8]
    avreage = np.mean(dct_roi)
    hash = []
    for i in range(dct_roi.shape[0]):
        for j in range(dct_roi.shape[1]):
            if dct_roi[i,j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash

#average hash algorithm
def aHash(image):

    image=cv2.resize(image,(8,8),interpolation=cv2.INTER_CUBIC)
    #convert to gray
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    avreage = np.mean(image)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash

#differnet hash algorithm
def dHash(image):
    #9*8
    image=cv2.resize(image,(9,8),interpolation=cv2.INTER_CUBIC)
    #convert to gray
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     print(image.shape)
    hash=[]
    #
    for i in range(8):
        for j in range(8):
            if image[i,j]>image[i,j+1]:
                hash.append(1)
            else:
                hash.append(0)
    return hash

#calculate hamming distance
def Hamming_distance(hash1,hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num
if __name__ == "__main__":
    image_file1 = '/Users/gaoyue/PycharmProjects/pythonProject/venv/a.png'
    image_file2 = '/Users/gaoyue/PycharmProjects/pythonProject/venv/b.png'

    img1 = cv2.imread(image_file1)
    img2 = cv2.imread(image_file2)
    
# convert the image 90 degree
    imgconvert=np.rot90(img2)



    hash1 = pHash(img1)
    hash2 = pHash(img2)
    hash3=pHash(imgconvert)



    dist = Hamming_distance(hash1, hash2)
    dist2= Hamming_distance(hash1,hash3)

    #calculate the similarity based on distance
    similarity = 1 - dist * 1.0 / 64
    similarity2 = 1 - dist2 * 1.0 / 64

    dist = str(dist)
    dist2 = str(dist2)

    similarity=str(similarity)
    similarity2=str(similarity2)


    print('The distance is ：' + dist)
    print('The similarity is ：' + similarity)
    print('The distance2 is ：' + dist2)
    print('The similarity2 is ：' + similarity2)
