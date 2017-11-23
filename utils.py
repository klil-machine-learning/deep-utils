from shutil import copyfile, move
from glob import glob
import numpy as np
from baseutils import *

def copy_some(src_dir, dst_dir, split, extensions):
    g_src = glob(os.path.join(src_dir, '*.' + extensions[0]), recursive=True)
    num_src = len(g_src)
    g_dst = glob(os.path.join(dst_dir, '*.' + extensions[0]), recursive=True)
    num_dst = len(g_dst)
    num_to_copy = int(num_src * split) - num_dst

    print("src_dir: {} number of items to copy: {}".format(src_dir, num_to_copy))
    shuf = np.random.permutation(g_src)
    for i in range(num_to_copy):
        rel_path = os.path.relpath(shuf[i], src_dir)
        copyfile(shuf[i], os.path.join(dst_dir, rel_path))
        for extension in extensions[1:]:
            shuf2 = os.path.splitext(shuf[i])[0] + '.' + extension
            rel_path2 = os.path.splitext(rel_path)[0] + '.' + extension
            copyfile(shuf2, os.path.join(dst_dir, rel_path2))


def split_train(base_dir, new_dir_name, split=0.1, extensions=['jpg']):
    # this function splits train set to train & valid/test

    # create valid dirs
    train = os.path.join(base_dir, 'train')
    new_dir = os.path.join(base_dir, new_dir_name)
    maybe_copy_dir_struct(train, new_dir)

    g_train = glob(os.path.join(train, '*.' + extensions[0]), recursive=True)
    num_train = len(g_train)
    g_valid = glob(os.path.join(new_dir, '*.' + extensions[0]), recursive=True)
    num_valid = len(g_valid)

    num_valid_target = (num_train + num_valid) * split

    # print(num_train, num_valid, num_valid_target)

    num_to_move = int(num_valid_target - num_valid)
    print("number of items to move: ", num_to_move)
    shuf = np.random.permutation(g_train)
    for i in range(num_to_move):
        rel_path = os.path.relpath(shuf[i], train)
        move(shuf[i], os.path.join(new_dir, rel_path))
        for extension in extensions[1:]:
            shuf2 = os.path.splitext(shuf[i])[0] + '.' + extension
            rel_path2 = os.path.splitext(rel_path)[0] + '.' + extension
            move(shuf2, os.path.join(new_dir, rel_path2))


def gen_sample(dir, split=0.1, extensions=['jpg']):
    # this function generates sample dataset

    sample = os.path.join(dir, 'sample')
    maybe_create_dir(sample)

    train = os.path.join(dir, 'train')
    if os.path.exists(train):
        sample_train = os.path.join(sample, 'train')
        maybe_copy_dir_struct(train, sample_train)
        copy_some(train, sample_train, split=split, extensions=extensions)

    test = os.path.join(dir, 'test')
    if os.path.exists((test)):
        sample_test = os.path.join(sample, 'test')
        maybe_copy_dir_struct(test, sample_test)
        copy_some(test, sample_test, split=split, extensions=extensions)

    valid = os.path.join(dir, 'valid')
    if os.path.exists(valid):
        sample_valid = os.path.join(sample, 'valid')
        maybe_copy_dir_struct(test, sample_valid)
        copy_some(valid, sample_valid, split=split, extensions=extensions)





