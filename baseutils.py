import os, sys

def maybe_create_dir(dir):
    if os.path.exists(dir):
        return
    os.makedirs(dir)


def maybe_copy_dir_struct(src_dir, dst_dir):
    maybe_create_dir(dst_dir)
    for o in os.listdir(src_dir):
        if os.path.isdir(os.path.join(src_dir, o)):
            maybe_copy_dir_struct(os.path.join(src_dir, o), os.path.join(dst_dir, o))

