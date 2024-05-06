import os
from PIL import Image
import numpy as np
import cv2
INPUT_FOLDERPATH = '../NegativeMasks'
OUTPUT_FOLDERPATH ='../BinarizedMasks'
if __name__ == '__main__':
    for file in os.listdir(INPUT_FOLDERPATH):
        img =cv2.imread(f'{INPUT_FOLDERPATH}/{file}', cv2.IMREAD_GRAYSCALE)
        #img = np.asarray(Image.open())
        limiar, binary_img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
        inverted_img = cv2.bitwise_not(binary_img)
        Image.fromarray(inverted_img).save(f'{OUTPUT_FOLDERPATH}/{file}')