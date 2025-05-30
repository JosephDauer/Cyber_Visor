
class SimpleNN (nn.module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fcl=nn.Linear(784, 128) #input into hidden layer (28x28 experimentation if input)
        self.dropout=nn.Dropout(0.2) #dropout for regulization
        self.fcl2=nn.Linear(128, 64) #2nd hidden layer
        self.fc3=nn.Linear(64, 10) #output layer

    def forward(self, x):
        x=F.relu(self.fcl(x)) #ReLU alayer activation
        x=self.dropout(x)
        x=F.relu(self.fc2(x))
        x=F.log_softmax(self.fc3(x), dim=1) #log softmax for class
        return x
