"""
@author: yang
"""
import torch
from torch.utils.data import Dataset
import numpy as np
import os
import pathlib
from PIL import Image


class CustomDataset(Dataset):
    def __init__(self, read_directory):
        self.root = read_directory

        path_loc = pathlib.Path(read_directory)
        if not path_loc.exists():
            raise Exception('The path provided is incorrect!')

        list_of_images = os.listdir(read_directory)
        self.image_paths = list_of_images

    def __getitem__(self, index):
        file_name = self.image_paths[index]
        image_info, _ = file_name.split(".")
        user_name, label = image_info.rsplit("_", 1)

        img = Image.open(os.path.join(self.root, file_name))
        img_np = np.array(img)

        # Scale the values to range -1 to 1
        img_np = (img_np - 127.5) / 127.5

        ret_dict = {
            "image": torch.FloatTensor(img_np),
            "user_name": user_name,
            "label": label
        }

        return ret_dict

    def __len__(self):
        return len(self.image_paths)

    def __str__(self):
        return 'Dataset details - \nRoot Location : {}\nSize : {}'.format(
            self.root, self.__len__())