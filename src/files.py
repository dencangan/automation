"""
File handling type functions.
"""

import os
import shutil
import re
from typing import Union
from datetime import datetime


def arrange_files(folder_directory: str,
                  misc_folder_name: str = "others") -> None:
    """
    Arrange files and put them in folders according to their extension type.

    Parameters
    ----------
    folder_directory
        Folder to arrange files.
    misc_folder_name
        Folder to store anything else without file extension, creates default "others" folder.

    """
    if not os.path.exists(os.path.join(folder_directory, misc_folder_name)):
        os.makedirs(os.path.join(folder_directory, misc_folder_name))

    lst_files = os.listdir(folder_directory)
    lst_file_end = [x[-4:] for x in lst_files]
    lst_file_ext = [y for y in lst_file_end if re.search("^[.]", y)]

    for ext in lst_file_ext:
        if ext[1:].isalpha() is True:
            print(f"{ext} is an extension")
        else:
            lst_file_ext.remove(ext)
            print(f"{ext} is not an extension")

    # drop duplicates
    lst_file_ext = list(set(lst_file_ext))

    for folder in lst_file_ext:
        try:
            os.makedirs(os.path.join(folder_directory, folder))
        except FileExistsError:
            print(f"Extension {folder} already exists.")

    for file in lst_files:
        for file_ext in lst_file_ext:
            if file[-4:] == file_ext:
                shutil.move(os.path.join(folder_directory, file), os.path.join(folder_directory, file_ext))

    lst_all_files = os.listdir(folder_directory)

    lst_misc_files = [x for x in lst_all_files if x not in lst_file_ext]

    for misc_file in lst_misc_files:
        shutil.move(os.path.join(folder_directory, misc_file), os.path.join(folder_directory, "others"))


def list_file_exts(folder_directory: str,
                   ext: str = "exe") -> list:
    """Returns a list of files of specified extension."""
    return [os.path.join(folder_directory, x) for x in os.listdir(folder_directory) if x.endswith(ext)]


def check_file_exists(file: Union[list, str]) -> None:
    """Checks if file or list of files exists."""
    if isinstance(file, str):
        file = [file]
        # Testing all directories
        for f in file:
            assert os.path.exists(f), f"{f} not found"


def check_last_modified(file: Union[list, str]):
    """Checks last modified info for files."""

    if isinstance(file, str):
        file = [file]

    def get_file_time(f):
        return datetime.utcfromtimestamp(int(os.path.getmtime(f))).strftime("%Y%m%d")

    for f in file:
        print(get_file_time(f))


def copy_move(source_dir: str,
              des_dir: str,
              is_copy: bool = True) -> None:
    """
    Copy or move files

    Parameters
    ----------
    source_dir
        Directory to copy/move file from.
    des_dir
        Destination to copy/move file to.
    is_copy
        If True, copies file, else cuts file.

    """
    if is_copy:
        shutil.copy(source_dir, des_dir)
    else:
        shutil.move(source_dir, des_dir)


if __name__ == '__main__':
    arrange_files(folder_directory=r"C:\Users\Dencan Gan\Downloads")