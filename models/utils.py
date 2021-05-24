import torch
import torch.nn as nn

from functools import reduce
from operator import mul

class Resize(nn.Module):
    def __init__(self, shape):
        super(Resize, self).__init__()
        self.shape = shape

    def forward(self, x):
        return nn.functional.interpolate(x, size=self.shape, mode='nearest') #mode='bilinear', align_corners=True)

class LevelAdapter(nn.Module):
    def __init__(self, mapping, shape):
        super(LevelAdapter, self).__init__()
        self.shape = shape
        self.mapping = mapping

        self.zero = None

    def set_zero(self, x):
        self.zero = torch.zeros_like(x[:, 0:1, :, :])

    def forward(self, x):
        if(self.zero is None or self.zero.size(0) != x.size(0)):
            self.set_zero(x)
        layers = []
        d, w, h = self.shape
        for i in range(d):
            if(i in self.mapping):
                idx = self.mapping.index(i)
                layers.append(x[:, idx:idx+1])
            else:
                layers.append(self.zero)
        x = torch.cat(layers, dim=1)
        return x
