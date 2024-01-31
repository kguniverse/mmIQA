import argparse
import random

# def parse_args():
#     parser = argparse.ArgumentParser(description='Training for Blind Image Quality Assessment')
#     parser.add_argument('config', help='config file path')

def main(cfg):
    folder_path = {
        'live': 'LIVE/',
        'csiq': 'CSIQ/',
        'tid2013': 'TID2013/',
        'livec': 'LIVEC/',
        'koniq-10k': 'KonIQ-10k/',
        'cid2013': 'CID2013/',
        'kadid-10k':'kadid10k/',
        'SPAQ':'SPAQ/'
    }

    img_num = {
        'live': list(range(0, 29)),
        # 'csiq': list(range(0, 30)),
        # 'tid2013': list(range(0, 25)),
        # 'livec': list(range(0, 1162)),
        # 'koniq-10k': list(range(0, 10073)),
        # 'cid2013': list(range(0, 6)),
        # 'kadid-10k': list(range(0, 81)),
        # 'SPAQ': list(range(0, 11124))
    }

    # add prefix
    for _, folder in folder_path.items():
        folder = 'data/' + folder

    sel_num = img_num[cfg.dataset]

    for i in range(cfg.train_num):
        print("Round %d" % i)

        # shuffle
        random.shuffle(sel_num)
        train_index = sel_num[0:int(round(0.8 * len(sel_num)))]
        test_index = sel_num[int(round(0.8 * len(sel_num))):len(sel_num)]

        

    

if __name__ == '__main__':
    main()

