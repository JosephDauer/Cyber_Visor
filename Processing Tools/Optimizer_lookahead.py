import torch
from torch.optim import Adam

class Lookahead:
    def __init__(self, base_optimizer,k=5, alpha=0.5):
        self.optimizer = base_optimizer
        self.k = k
        self.alpha = alpha

    def step(step):
        pass

base_optimizer = Adam(model.parameters(), lr=0.001)
optimizer = lookahead(base_optimizer)