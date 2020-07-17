import os
import json
import sys
import numpy as np
from PIL import Image

read_directory = r"C:\Users\fangy\AppData\Local\Packages\CanonicalGroupLimited." \
                 r"UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\root\leaf\data\femnist\data\all_data_modified"
write_directory = r"C:\Users\fangy\AppData\Local\Packages\CanonicalGroupLimited." \
                  r"UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\root\leaf\data\femnist\data\all_data_modified_image"

if not os.path.isdir(write_directory):
    os.makedirs(write_directory)

for file_name in os.listdir(read_directory):
    print("Processing file {}".format(file_name))

    with open(os.path.join(read_directory, file_name), "r") as f_read:
        data = json.load(f_read)
        for user_name in data["users"]:
            user_data = data["user_data"][user_name]
            for image, label in zip(user_data["x"], user_data["y"]):
                #print("user_name: {}, label: {}, image: {}".format(user_name, label, image))
                image = np.array([pixel * 255 for pixel in image], dtype=np.uint8)
                image = np.reshape(image, (28, 28))
                image = Image.fromarray(image, 'L')
                image.save(os.path.join(write_directory, "{}_{}.png".format(user_name, label)))

