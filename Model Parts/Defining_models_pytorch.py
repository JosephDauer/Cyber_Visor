import torch
import torch.nn as nn

class SimpleNN(nn.Modules):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.dropout = nn.Droptout(0.2)
        self.fc2 = nn.Linear(5, 2)
    
    def forward(self, x):
        x = torch.relu(self.fcl(x))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        x = torch.softmax(self.fc3(x), dim=1)
        return x
model = SimpleNN()