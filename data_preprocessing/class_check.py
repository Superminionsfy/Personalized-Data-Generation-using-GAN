import os
import json
import matplotlib.pyplot as plt
import numpy as np


def plot_image(image_list):
    np_arr = np.array(image_list)
    np_arr = np.reshape(np_arr, (28, 28))
    plt.imshow(np_arr, cmap='gray')
    plt.show()


read_directory = r"C:\Users\fangy\AppData\Local\Packages\CanonicalGroupLimited." \
                 r"UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\root\leaf\data\femnist\data\all_data_modified"


class_range = 100
with open(os.path.join(read_directory, "all_data_0.json")) as f_read:
    data = json.load(f_read)

    for class_index in range(class_range):
        image_plotted = False

        for user_name in data["users"]:
            if image_plotted:
                break

            user_data = data["user_data"][user_name]
            for index, cur_class in enumerate(user_data["y"]):
                if cur_class == class_index:
                    image_list = user_data["x"][index]
                    plot_image(image_list)
                    image_plotted = True
                    print("Current class index is {}.".format(class_index))
                    break

        if not image_plotted:
            print("Current class index {} does not exist".format(class_index))
