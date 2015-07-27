import os
from hurry.filesize import size

NEW_DIR = "E:\English Movies"
BASE_DIR = "D:\English Movies"
SEPARATOR = "\\"


def verify(directory_name):
    return os.path.isdir(directory_name)


def get_duplicates(base_dir, new_dir):
    original_files = os.listdir(base_dir)
    new_files = os.listdir(new_dir)
    for filename in new_files:
        if filename in original_files:
            print "DUPLICATE : ", filename
            print base_dir + SEPARATOR + filename
            original_size = get_size(base_dir + SEPARATOR + filename)
            new_size = get_size(new_dir + SEPARATOR + filename)
            print "original: %d\t\t\t\tnew: %d" % (original_size, new_size)


def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            if not (f.endswith(".url") or f.endswith(".srt") or f.endswith("sub")):
                fp = os.path.join(dirpath, f)
                total_size += size(os.path.getsize(fp))
    return total_size


def main(base_dir, new_dir):
    can_proceed = verify(base_dir) & verify(new_dir)
    if can_proceed:
        duplicate_titles = get_duplicates(base_dir, new_dir)
        print duplicate_titles


main(BASE_DIR, NEW_DIR)
