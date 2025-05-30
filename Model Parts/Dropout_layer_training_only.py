import torch
import torch.nn as nn

class Customdropoutlayer(nn.Module):
    def __init__(self, dropout_rate=0.5):
        super(Customdropoutlayer, self).__init__()
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        if self.training:
            return x * torch.bernoulli(torch.full(x.shape, 1 - self.dropout_rate)) / (1 - self.dropout_rate)
        else:
            # During evaluation, we do not apply dropout
            return x
        return x