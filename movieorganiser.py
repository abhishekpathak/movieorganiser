import os

NEW_DIR = "E:\English Movies"
BASE_DIR = "D:\English Movies"
SEPARATOR = "//"


def verify(directory_name):
    return os.path.isdir(directory_name)


def get_duplicates(base_dir, new_dir):
    original_files = os.listdir(base_dir)
    new_files = os.listdir(new_dir)
    for filename in new_files:
        if filename in original_files:
            print "DUPLICATE : ", filename
            original_size = os.path.getsize(base_dir + SEPARATOR + filename)
            new_size = os.path.getsize(new_dir + SEPARATOR + filename)
            print "original size : %d              new size : %d" % (original_size, new_size)


def main(base_dir, new_dir):
    can_proceed = verify(base_dir) & verify(new_dir)
    if can_proceed:
        duplicate_titles = get_duplicates(base_dir, new_dir)
        print duplicate_titles
