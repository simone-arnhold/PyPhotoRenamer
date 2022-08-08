"""
renamer_new.py

This script automatically renames the files in a specified folder X based on:
-   the number of pictures per each item in the folder (pictures_per_magazine(type: int))
-   a txt list of titles, in a csv format or in a each-line-an-item format (function read_titles());
        the txt list must be called titles.txt and be placed in the root folder.

The result will be:
each item in the folder renamed as [item1.jpg, item1B.jpg, item1C.jpg, item2.jpg, item2B.jpg, item2C.jpg...]

An error will be raised if the expected number of items does not correspond with the actual number of items
to be renamed.

"""


import os
import string

from natsort import os_sorted
from pathlib import Path

root = Path(r"C:\Users\Sim\Desktop\Salvatore di Stefano 2")
folder = "Tex Raccoltine Serie Bianca"
pictures_per_magazine = 4


images_folder = root / folder
titles_file = root / "titles.txt"

print("")
print("Image folder:\t", images_folder)
print("Titles file:\t", titles_file)


# read titles
def read_titles(_titles_file):
    with open(_titles_file) as f:
        _number_list = f.read().splitlines()
        if "," in _number_list[0] and len(_number_list) == 1:
            # convert to list
            _number_list = _number_list[0].split(", ")
        return _number_list


number_list = read_titles(titles_file)
print(number_list, "-> length:", len(number_list))


def create_list_of_titles(_pictures_per_magazine):
    if not isinstance(_pictures_per_magazine, int):
        raise TypeError()
    # letters = list(string.ascii_uppercase)[0:_pictures_per_magazine]
    letters = list(string.ascii_uppercase)[1:_pictures_per_magazine]
    elaborated_list = [n for n in number_list]
    for number in number_list:
        for letter in letters:
            elaborated_list.append(number + "-" + letter)
    elaborated_list = os_sorted(elaborated_list)
    print("\nelaborated list: ", elaborated_list, "-> length:", len(elaborated_list))
    return elaborated_list


create_list_of_titles(pictures_per_magazine)


def create_list_special():
    letters = "e"
    elaborated_list = []
    for n in number_list:
        for l in letters:
            elaborated_list.append(n + l)
    elaborated_list = os_sorted(elaborated_list)
    return elaborated_list


def rename_images(_images_folder, _pictures_per_magazine):
    new_names = create_list_of_titles(_pictures_per_magazine)
    images = os.listdir(_images_folder)
    # print(images, len(images))
    for im in images:
        os.rename(os.path.join(_images_folder, im),
                  os.path.join(_images_folder, new_names[images.index(im)]) + ".jpg")


# TEST
number_of_mags = len(os.listdir(images_folder)) / pictures_per_magazine
print(len(number_list), " vs", int(number_of_mags))

if input("Are you sure that you want to continue and rename those files? (y/n) ") != "y":
    print("Process aborted. Quitting.")
    exit()

if len(number_list) != number_of_mags:
    raise ValueError("Number of mags do not correspond with the expected number: {0} previsti vs {1} con foto presenti"
                     .format(len(number_list), number_of_mags))
else:
    rename_images(images_folder, pictures_per_magazine)

