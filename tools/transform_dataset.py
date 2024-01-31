# copy to the root of reproduce folder
from dataloader.dataset_folders import LIVEFolder
import shutil
import os
import random
import json

def create_folder_if_not_exist(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def make_dataset(dst, dataset):
    create_folder_if_not_exist(dst)
    datalist = []
    for i in range(len(dataset)):
        _, label, filename = dataset[i]
        dst_path = shutil.copy2(filename, dst)
        datalist.append(dict(img_path=dst_path, img_label=float(label)))
        
    return datalist

def main():
    indexs = list(range(0, 29))
    random.shuffle(indexs)
    train_index = indexs[0:int(round(0.8 * len(indexs)))]
    test_index = indexs[int(round(0.8 * len(indexs))):len(indexs)]
    train_live_dataset = LIVEFolder(root='data/LIVE', index=train_index, transform=None, patch_num=1)
    test_live_dataset = LIVEFolder(root='data/LIVE', index=test_index, transform=None, patch_num=1)
    final_ann_info = {}
    metainfo = {}
    final_ann_info['metainfo'] = metainfo

    train_dst = '../data/LIVE/train'
    test_dst = '../data/LIVE/test'
    create_folder_if_not_exist(train_dst)
    create_folder_if_not_exist(test_dst)
    create_folder_if_not_exist('../data/LIVE/annotations')

    train_datalist = make_dataset(train_dst, train_live_dataset)
    train_ann_info = dict(metainfo={}, data_list=train_datalist)
    with open('../data/LIVE/annotations/train.json', 'w') as f:
        json.dump(train_ann_info, f)
    
    test_datalist = make_dataset(test_dst, test_live_dataset)
    test_ann_info = dict(metainfo={}, data_list=test_datalist)
    with open('../data/LIVE/annotations/test.json', 'w') as f:
        json.dump(test_ann_info, f)


if __name__ == '__main__':
    main()