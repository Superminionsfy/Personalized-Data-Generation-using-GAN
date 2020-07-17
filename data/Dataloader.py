import torch
from data.CustomDataset import CustomDataset


class DataLoader:
    def __init__(self, read_directory, batch_size):
        self.read_directory = read_directory
        self.batch_size = batch_size

    def get_data_loader(self):
        dataset = CustomDataset(self.read_directory)
        data_loader = torch.utils.data.DataLoader(dataset, batch_size=self.batch_size, shuffle=True)

        return data_loader
