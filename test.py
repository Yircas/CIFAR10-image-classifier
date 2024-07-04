import matplotlib.pyplot as plt # for plotting
import numpy as np # for transformation

# PyTorch stuff
import torch # PyTorch package
import torchvision # load datasets
import torchvision.transforms as transforms # transform data
import torchvision.transforms.functional as TF
import torch.nn as nn # basic building block for neural neteorks
import torch.nn.functional as F # import convolution functions like Relu
import torch.optim as optim # optimzer

# Captum stuff
from captum.attr import IntegratedGradients
from captum.attr import Saliency
from captum.attr import DeepLift
from captum.attr import NoiseTunnel
from captum.attr import visualization as viz

# it doesn't matter, whether it outputs True or False right now
print(torch.cuda.is_available())