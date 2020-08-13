# Personalized Data Generation using GAN

The code for personalized data generation using GAN, which is used GAN to generate user-specified missing data.

## Code Structure

The repo includes 4 folders:
- CollaGAN: The code for CollaGAN, which is proposed in [CollaGAN : Collaborative GAN for Missing Image Data Imputation](https://arxiv.org/abs/1901.09764)
- data: Including a custom PyTorch dataloader to load our FeMNIST dataset
- data_preprocessing: Code for investigating and pre-processing the data
- kmeans_image_generation: The main part of the code, which used kmeans to group user and use GAN to generate missing image for each cluster.

We mainly use code in `data_preprocessing` and `kmeans_image_generation` as we finally choose kmeans with GAN as our preferred method.

## How to Run the Code

Before running the code, please get the dataset first by the following steps:
1. Clone the repo [leaf](https://github.com/TalwalkarLab/leaf)
2. In `leaf/data`, there is a folder called `femnist`. Switch to that folder.
3. Run `./preprocess.sh -s niid --sf 1.0 -k 0 -t sample` to get the full dataset.

For more infomation, please read the README in folder `femnist` and refer to [LEAF: A Benchmark for Federated Settings](https://arxiv.org/abs/1812.01097)

After the dataset is ready, you could:
- Run code under `data_preprocessing` to do the investigation on the dataset
- Use kmeans to do the clustering and generate new images for missing data

And here are detailed steps to run experiments mentioned in our final report:
1. Run `kmeans.ipynb` first to read the dataset, split images based on kmeans cluster and get user assignment. Run `kmeans.ipynb` for at least 2 target_class if you want to run the final image generation step.
2. Run `dcgan.ipynb` to train dcgan on each cluster
3. Run `cluster_verification.ipynb` to verify the trained Generator and see if the generated images are still in the same cluster
4. Run `image_generation.ipynb` to load trained Generator and generate new images for specified users.

For running ipynb files you need a Jupyter Notebook client. For each notebook, simply set the hyper-parameters and run all cells in it. The hyper-parameters are specified at the top of the files.

`.ipynb` files already included our sample output, so please feel free to check it before running the code

## Environment

For running the code, you need python environment and a Jupyter Notebook client. For training the GAN, a CUDA device is needed.

We recommend using `conda` to manage your Python packages. For running the code, you need the packages below:
- PyTorch
- json
- Pillow
- numpy
- sklearn
- collections
- pickle
- torchvision
- matplotlib

## Reference
- Lee, Dongwook, et al. "CollaGAN: Collaborative GAN for missing image data imputation." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2019.
- Caldas, Sebastian, et al. "Leaf: A benchmark for federated settings." arXiv preprint arXiv:1812.01097 (2018).
- “DCGAN Tutorial.” DCGAN Tutorial - PyTorch Tutorials 1.6.0 Documentation, pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html.
