import torch 
from torch.utils.data import DataLoader
from torchvision import datasets ,transforms 

transformation = transforms.Compose ([
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(0.5,))
])

train_dataset= datasets.MNIST(root="./data", train=True , download=True , transform=transformation)
test_dataset= datasets.MNIST(root="./data", train=False , download=True , transform=transformation)

train_loader = DataLoader(train_dataset,batch_size=32,shuffle =True)
test_loader = DataLoader(test_dataset,batch_size=32,shuffle=False)
print(f"Training Data Size :{len(train_dataset)}")
print(f"Test Data Size :{len(test_dataset)}")