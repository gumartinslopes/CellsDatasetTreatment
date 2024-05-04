import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os 
ORIGINAL_FOLDER = './CellsDataset/original'
GT_FOLDER = './CellsDataset/labels'
SEGMENTD_FOLDER = './CellsDataset/segmented'

def main():
    for file in os.listdir(ORIGINAL_FOLDER):
        original = np.asarray(Image.open(ORIGINAL_FOLDER + '/'+ file))
        mask = np.asarray(Image.open(GT_FOLDER + '/' + file).convert('L'))
        masked = cv2.bitwise_and(np.asarray(original), np.asarray(original), mask=np.asarray(mask))
        Image.fromarray(masked).save(SEGMENTD_FOLDER + '/' + file)

if __name__ == '__main__':    
    main()
