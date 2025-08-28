import torch
from torchvision import transforms
from glob import glob
import os
import json
from torch.utils.data import Dataset
from PIL import Image
import random


transform = transforms.ToTensor()
toPIL = transforms.ToPILImage()


def rajouter_features(img, img_burn):

    tensor = (transform(img) * 255).byte()
    tensor_burn = (transform(img_burn) * 255).byte()

    # faire des masques pour les différents niveaux de brûlé
    color_d1 = torch.tensor([181, 254, 142], dtype=tensor.dtype).view(-1, 1, 1).repeat(1, tensor.shape[1], tensor.shape[2])   # damage 1
    maskd1 = (tensor_burn == color_d1).all(dim=0)
    color_d2 = torch.tensor([254, 217, 142], dtype=tensor.dtype).view(-1, 1, 1).repeat(1, tensor.shape[1], tensor.shape[2])   # damage 2
    maskd2 = (tensor_burn == color_d2).all(dim=0)
    color_d3 = torch.tensor([254, 153, 41], dtype=tensor.dtype).view(-1, 1, 1).repeat(1, tensor.shape[1], tensor.shape[2])   # damage 3
    maskd3 = (tensor_burn == color_d3).all(dim=0)
    color_d4 = torch.tensor([204, 76, 2], dtype=tensor.dtype).view(-1, 1, 1).repeat(1, tensor.shape[1], tensor.shape[2])   # damage 4
    maskd4 = (tensor_burn == color_d4).all(dim=0)

    # rajouter feature 1 brûlé (Trees)
    color_1 = torch.tensor([57, 125, 73], dtype=tensor.dtype).view(-1, 1, 1).repeat(1, tensor.shape[1], tensor.shape[2])
    mask1 = (tensor == color_1).all(dim=0)
    tensor[:, mask1 & maskd1] = torch.tensor([13, 253, 21], dtype=tensor.dtype)[:, None]   # un vert fluo
    tensor[:, mask1 & maskd2] = torch.tensor([165, 244, 167], dtype=tensor.dtype)[:, None]   # un vert clair
    tensor[:, mask1 & maskd3] = torch.tensor([65, 166, 68], dtype=tensor.dtype)[:, None]   # un vert plus foncé
    tensor[:, mask1 & maskd4] = torch.tensor([16, 114, 20], dtype=tensor.dtype)[:, None]   # un violet très foncé

    # rajouter feature 7 brûlé (Scrub/shrub)
    color_7 = torch.tensor([223, 195, 90], dtype=tensor.dtype).view(-1, 1, 1).repeat(1, tensor.shape[1], tensor.shape[2])
    mask7 = (tensor == color_7).all(dim=0)
    tensor[:, mask7 & maskd1] = torch.tensor([242, 34, 214], dtype=tensor.dtype)[:, None]   # un rose fluo
    tensor[:, mask7 & maskd2] = torch.tensor([207, 128, 253], dtype=tensor.dtype)[:, None]   # un violet clair
    tensor[:, mask7 & maskd3] = torch.tensor([145, 64, 206], dtype=tensor.dtype)[:, None]   # un violet plus foncé
    tensor[:, mask7 & maskd4] = torch.tensor([84, 19, 121], dtype=tensor.dtype)[:, None]   # un violet très foncé

    img = toPIL(tensor)
    return img



def moving_average(x, w=10):
    smoothed = []
    for i in range(len(x)):
        start = max(0, i - w + 1)
        window = x[start:i+1]
        smoothed.append(sum(window) / len(window))
    return smoothed



class ImageDataset(Dataset):

    def __init__(self, partial_path, transform=None):
        self.transform = transform

        # get the dictionnary with the crop's infos
        with open(f'{partial_path}_data.json', 'r', encoding='utf-8') as f:
            dico = json.load(f)

        # get all image paths, attributs and classes
        self.data = []

        for path in glob(os.path.join(f"{partial_path}", "**", "*.png"), recursive=True):
            filename = os.path.basename(path)      # "crop_i.png"
            crop_name = os.path.splitext(filename)[0]   # "crop_i"

            attributs = dico[crop_name]["attributs"]
            damage = dico[crop_name]["niveau de brûlé"]

            self.data.append((path, attributs, damage))


    def __len__(self):
        return len(self.data)


    def __getitem__(self, idx):
        img_path, attribut, label = self.data[idx]

        img = Image.open(img_path).convert("RGB")

        if self.transform is not None:
            img = self.transform(img)

        attribut = torch.tensor(attribut, dtype=torch.float32)
        label = torch.tensor(label, dtype=torch.int64)

        return img, attribut, label



def random_90_rotation(img):
    angles = [0, 90, 180, 270]
    return transforms.functional.rotate(img, angle=random.choice(angles))



def get_device():
    """
    Renvoie le device à utiliser selon les disponibilités (cuda -> mps -> cpu).
    """
    if torch.cuda.is_available():
        return "cuda"
    elif torch.backends.mps.is_available():
        return "mps"
    else:
        return "cpu"

