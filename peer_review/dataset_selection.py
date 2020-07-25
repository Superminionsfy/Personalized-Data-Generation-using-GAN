import os
import json

# This code is for dataset selection. FEMNIST dataset is a dataset with not only digits but also letters.
# And it has different numbers of samples for each user of each digit.
# Our goal: select one sample for each user of each digit.
# You can download the dataset here: https://github.com/TalwalkarLab/leaf

# Replace the read_directory and write directory with your own directories
read_directory = r"C:\Users\fangy\AppData\Local\Packages\CanonicalGroupLimited." \
                 r"UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\root\leaf\data\femnist\data\all_data"
write_directory = r"C:\Users\fangy\AppData\Local\Packages\CanonicalGroupLimited." \
                  r"UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\root\leaf\data\femnist\data\all_data_modified"

# The 10 indexes for digits in the original dataset has been verified in our test code.
only_keep_digits = True
digit_class_indexes = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if not os.path.isdir(write_directory):
    os.makedirs(write_directory)

for file_name in os.listdir(read_directory):
    print("Processing file {}".format(file_name))

    with open(os.path.join(read_directory, file_name), "r") as f_read:
        data = json.load(f_read)
        data_save = {"users": [], "num_sample": [], "user_data": {}}
        # The data structure is kept as the same as the FEMNIST dataset.
        for user_name in data["users"]:
            user_data = data["user_data"][user_name]
            new_user_data = {"x": [], "y": []}
            # The "x", "y" here represents to the sample and the digit label for this sample respectively,
            # which is the same as the FEMNIST dataset.
            image_class_set = set()
            num_sample = 0
            for index, image_class in enumerate(user_data["y"]):
                if only_keep_digits and image_class not in digit_class_indexes:
                    continue

                if image_class not in image_class_set:
                    image_class_set.add(image_class)
                    cur_image = user_data["x"][index]
                    new_user_data["x"].append(cur_image)
                    new_user_data["y"].append(image_class)
                    num_sample += 1
            data_save["users"].append(user_name)
            data_save["num_sample"].append(num_sample)
            data_save["user_data"][user_name] = new_user_data

        with open(os.path.join(write_directory, file_name), "w") as f_write:
            json.dump(data_save, f_write)
