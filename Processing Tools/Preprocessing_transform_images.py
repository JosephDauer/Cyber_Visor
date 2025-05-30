#
transform = transforms.compose([
    transforms.ToTensor(), #convert image to pytorch tenser
    transforms.Normalize((0.5), (0.5)) #sales images to mean 0.5 and standard deviation 0.5
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

#load data 
train_dataset = datasets.mnist(root='data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
