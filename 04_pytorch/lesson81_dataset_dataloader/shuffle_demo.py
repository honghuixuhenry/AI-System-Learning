import torch

from torch.utils.data import Dataset, DataLoader

class NumberDataset(Dataset):
    def __int__(self):
        self.data = torch.arange(10)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

dataset = NumberDataset()

loader = DataLoader(dataset, batch_size=2, shuffle=True)

for batch in loader:
    print(batch)