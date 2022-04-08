#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import hashlib
import os


def print_dir_tree_list(path, relativepath=""):

    try:
        relativepath += os.path.basename(path) + "/"

        dir_list = os.listdir(path)

        for e in dir_list:
            if os.path.isdir(path + "/" + e):  # folders
                print(e + "\t" + "<dir>")
                print_dir_tree_list(path + "/" + e, relativepath)
            else:  # links and files
                print(e + "\t" + relativepath + e + "\t" + get_md5_sum_hex(path + "/" + e))

    except FileNotFoundError:
        print("Exception: Path '" + path + "' not found.")

    except NotADirectoryError:
        print("Exception: Entered Argument '" + path + "' is not a directory.")


def get_md5_sum_hex(filepath):

    try:
        with open(filepath, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)

        return file_hash.hexdigest()

    except PermissionError:
        return "Exception: No permission for MD5-Calculation"


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Print file names and folders recursively starting from an initial path.')
    parser.add_argument('folderpath', metavar='path', type=str,
                        help='path to show')
    args = parser.parse_args()
    print_dir_tree_list(args.folderpath)

else:
    args = ""
