import cv2
import os

def create_folder(folder_path):
    '''Creates a folder if does not exists.'''
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
def binarize_images_on_folder(input_folder_path:str, output_folder_path:str):
    create_folder(output_folder_path)
    for file in os.listdir(input_folder_path):
        # Loads the image
        color_image = cv2.imread(f'{input_folder_path}/{file}')
        # Converts to grayscale
        gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        # Saves the image
        cv2.imwrite(f'{output_folder_path}/{file}', gray_image)

def main():
    binarize_images_on_folder('../NegativeMasks','../GrayNegativeMasks')

if __name__ == '__main__':
    main()