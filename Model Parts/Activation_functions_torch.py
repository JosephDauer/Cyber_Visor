import torch
import torch.nn.functional as F

#GeLU activations *
x = F.gelu(inputs)
#Swish activations
x = inputs * torch.sigmoid(inputs)
#Mish activations
x = inputs * torch.tanh(F.softplus(inputs))
#ReLU activations *
x = F.relu(inputs)
#Leaky ReLU activations *
x = F.leaky_relu(inputs, negative_slope=0.01)
#PReLU activations *
x = F.prelu(inputs, weight)
#ELU activations
x = F.elu(inputs, alpha=1.0)
#SELU activations
x = F.selu(inputs)
#Softplus activations *
x = F.softplus(inputs, beta=1, threshold=20)
#Softshrink activations
x = F.softshrink(inputs, lambd=0.5)
#Softsign activations
x = F.softsign(inputs)
#Tanhshrink activations
x = F.tanhshrink(inputs)
#Threshold activations
x = F.threshold(inputs, threshold=0.5, value=0)
#Hardtanh activations
x = F.hardtanh(inputs, min_val=-1, max_val=1)
#Hardshrink activations
x = F.hardshrink(inputs, lambd=0.5)
#LogSoftmax activations *
x = F.log_softmax(inputs, dim=1)
#Softmax activations *
x = F.softmax(inputs, dim=1)
#Sigmoid activations
x = torch.sigmoid(inputs)
#Tanh activations
x = torch.tanh(inputs)
#Softmin activations
x = F.softmin(inputs, dim=1)
#Softmax2d activations
x = F.softmax2d(inputs)
#Softmax3d activations
x = F.softmax3d(inputs)
#Softmax4d activations
x = F.softmax4d(inputs)
#Softmax5d activations
x = F.softmax5d(inputs)