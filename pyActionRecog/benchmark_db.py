import glob
import os
import random


def parse_directory(path): 
    """
    Parse directories holding extracted frames from standard benchmarks
    """
    print('parse frames under folder {}'.format(path))
    frame_folders = glob.glob(os.path.join(path, '*'))

    def count_files(directory):
        lst = os.listdir(directory)
        cnt_list = len(lst)
        return cnt_list

    # check RGB
    rgb_counts = {}
    dir_dict = {}
    for i,f in enumerate(frame_folders):
        cnt = count_files(f)
        k = f.split('/')[-1]
        rgb_counts[k] = cnt
        dir_dict[k] = f

        if i % 200 == 0:
            print('{} videos parsed'.format(i))

    print('frame folder analysis done')
    return dir_dict, rgb_counts


def build_split_list(split_tuple, frame_info, split_idx, shuffle=False):
    split = split_tuple[split_idx]

    def build_set_list(set_list):
        rgb_list = list()
        for item in set_list:
            frame_dir = frame_info[0][item[0]]
            rgb_cnt = frame_info[1][item[0]]
            rgb_list.append('{} {} {}\n'.format(frame_dir, rgb_cnt, item[1]))
        if shuffle:
            random.shuffle(rgb_list)
        return rgb_list

    train_rgb_list = build_set_list(split[0])
    test_rgb_list = build_set_list(split[1])
    return train_rgb_list, test_rgb_list


# Dataset specific split file parse
def parse_ucf_splits():
    data_path='/datasets/home/15/015/hayyubi/ActionRecognition/data'
    class_ind = [x.strip().split() for x in open(data_path + '/ucf101_splits/classInd.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        items = line.strip().split('/')
        label = class_mapping[items[0]]
        vid = items[1].split('.')[0]
        return vid, label

    splits = []
    for i in range(1, 4):
        train_list = [line2rec(x) for x in open(data_path + '/ucf101_splits/trainlist{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open(data_path + '/ucf101_splits/testlist{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits
