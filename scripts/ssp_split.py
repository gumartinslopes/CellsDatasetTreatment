import os 
from random import shuffle 
DATASET_PATH = '../AugmentedCellsDataset/crop/original'
TRAIN_FILE_PATH = '../AugmentedCellsDataset/crop/ids/train.txt'
TEST_FILE_PATH = '../AugmentedCellsDataset/crop/ids/val.txt'

def main():
    file_names = os.listdir(DATASET_PATH)
    shuffle(file_names)
    train_portion = 0.7
    test_portion = 1  - train_portion
    train_set_filenames = file_names[:int(len(file_names) * train_portion)]
    test_set_filenames = file_names[int(len(file_names) * train_portion):]
    with open(TRAIN_FILE_PATH,'w') as train_ids_file:
        for filename in train_set_filenames:
            train_ids_file.write(filename + '\n')

    with open(TEST_FILE_PATH,'w') as test_ids_file:
        for filename in test_set_filenames:
            test_ids_file.write(filename + '\n')
if __name__ == '__main__':
    main()