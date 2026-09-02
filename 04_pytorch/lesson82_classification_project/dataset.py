import torch
from torch.utils.data import Dataset

class ClassificationDataset(Dataset):
    def __int__(self, sample_per_class=100):
        class0 = (torch.randn(sample_per_class,2) * 0.6 + torch.tensor([-2.0,-2.0]))
        class1 = (torch.randn(sample_per_class,2) * 0.6 + torch.tensor([0.0,2.0]))
        class2 = (torch.randn(sample_per_class,2) * 0.6 + torch.tensor([2.0,-1.0]))
        self.x = torch.cat([class0,class1,class2], dim=0)

        labels0 = torch.zeros(sample_per_class, dtype = torch.long)
        labels1 = torch.ones(sample_per_class, dtype = torch.long)
        labels2 = torch.full((sample_per_class),2,dtype=torch.long)
        self.y = torch.cat([labels0,labels1,labels2], dim = 0)

        def __len__(self):
            return len(self.x)

        def __getitem__(self, index):
            return (self.x[index], self.y[index])

dataset = ClassificationDataset()
print(dataset.x.shape)
print(dataset.y.shape)
print(dataset.y.dtype)