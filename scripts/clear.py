import shutil
import argparse 

CROPPED_PATH = '../AugmentedCellsDataset/crop'  
ISOLATED_BINARIZED_PATH = '../IsolatedCellsDataset/binarized'
ISOLATED_ORIGINAL_PATH = '../IsolatedCellsDataset/original'

def create_parser():
    parser = argparse.ArgumentParser(description='Cleaning argument parser')
    parser.add_argument('--dataset', help='Dataset path')
    return parser.parse_args()

def main():
    args = create_parser()
    if args.dataset == 'cropped':
        shutil.rmtree(CROPPED_PATH)
    elif args.dataset == 'isolated_binarized':
        shutil.rmtree(ISOLATED_BINARIZED_PATH)
    elif args.dataset == 'isolated_original':
        shutil.rmtree(ISOLATED_ORIGINAL_PATH)
    else:
        print('No dataset selected!')
if __name__ == '__main__':
    main()