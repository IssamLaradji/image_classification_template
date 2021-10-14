import torch
import torchvision
import os
from PIL import Image
import pprint
import tqdm, glob
import argparse
import pandas as pd
import numpy as np
from torch.utils.data import TensorDataset
from haven import haven_utils as hu
from haven import haven_wizard as hw


class Couchetard:
    def __init__(self):
        datadir = "/mnt/public/datasets2/visual_store_google_drive/"
        self.fname_list = glob.glob(os.path.join(datadir, "*", "*", "*.png"))
        self.count = 0
        self.labels = []
        self.class_dict = {}
        self.class2label = {}
        for f in self.fname_list:
            name = os.path.split(f)[-1]
            name = name[: name.index("(")]
            if name not in self.class_dict:
                self.class_dict[name] = 0
            self.labels += [name]
            self.class_dict[name] += 1
            self.class2label[name] = self.count
            self.count += 1
        self.n_classes = len(self.class_dict.keys())

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        fname = self.fname_list[idx]
        label = self.labels[idx]
        images = Image.open(fname)
        transform = torchvision.transforms.Compose(
            [
                torchvision.transforms.Resize(224),
                torchvision.transforms.ToTensor(),
            ]
        )
        return {"images": transform(images), "labels": self.class2label[label]}


def get_dataset(name, split, datadir, exp_dict, download=True):
    if name == "couchetard":
        dataset = Couchetard()

    if name == "syn":
        # get dataset and loader
        X = torch.randn(5000, 1, 28, 28)
        y = torch.randint(0, 2, (5000, 1))
        dataset = TensorDataset(X, y)
        loader = torch.utils.data.DataLoader(dataset, batch_size=256)

    if name == "mnist":
        # get dataset and loader
        train = True if split == "train" else False
        transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
        dataset = torchvision.datasets.MNIST(
            root=datadir, train=train, download=download, transform=transform
        )
        
    return dataset
