import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os 
ORIGINAL_FOLDER = '../CellsDataset/original'
MASK_FOLDER = '../BinarizedMasks'
SEGMENTD_FOLDER = '../NegativeSegmentation'
INVERSE_SEGMENTATION_FOLDER = '../CellsDataset/inverted_segmentation'

def main():
    for file in os.listdir(MASK_FOLDER):
        original = np.asarray(Image.open(ORIGINAL_FOLDER + '/'+ file))
        mask = np.asarray(Image.open(MASK_FOLDER + '/' + file).convert('L'))
        masked = cv2.bitwise_and(np.asarray(original), np.asarray(original), mask=np.asarray(mask))
        #inv_masked = cv2.bitwise_and(np.asarray(original), np.asarray(original), mask=np.asarray(mask - 255))
        Image.fromarray(masked).save(SEGMENTD_FOLDER + '/' + file)
        #Image.fromarray(inv_masked).save(INVERSE_SEGMENTATION_FOLDER + '/' + file)

if __name__ == '__main__':    
    main()
