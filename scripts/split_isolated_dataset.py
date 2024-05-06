import os
import random
import shutil
import math

TRAINING_PATH = '../IsolatedCellsDataset/training'
TESTING_PATH = '../IsolatedCellsDataset/testing'
ALL_PATH = '../IsolatedCellsDataset/original/all'

def create_folder(folder_path):
    '''Creates a folder if does not exists.'''
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
def split_data(origin_path:str,dest_path:str, split: float):
    files = os.listdir(origin_path)
    random.shuffle(files)
    split_limit = math.floor(len(files) * split)
    create_folder(f'{dest_path}/training')
    create_folder(f'{dest_path}/test')
    # Assigning training data
    for file in files[:split_limit] :
        with open(f'{origin_path}/{file}','rb') as origin_file:
            with open(f'{dest_path}/training/{file}','wb') as  dest_file:
                shutil.copyfileobj(origin_file, dest_file)
    # Assigning test data
    for file in files[split_limit:] :
        with open(f'{origin_path}/{file}','rb') as origin_file:
            with open(f'{dest_path}/test/{file}','wb') as  dest_file:
                shutil.copyfileobj(origin_file, dest_file)
def main():
    split_data(ALL_PATH + '/0', '../IsolatedCellsDataset/original', 0.5)
        
if __name__ == '__main__':
    main()