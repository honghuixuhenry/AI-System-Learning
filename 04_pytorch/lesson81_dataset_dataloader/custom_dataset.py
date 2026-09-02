import torch
from torch.utils.data import Dataset

class RegressionData(
    Dataset
):
    def __int__(self):
        self.x = torch.arange(0, 20, dtype=torch.float32).reshape(-1,1)
        self.y = (3 * self.x + 2)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        return (self.x[index], self.y[index])

    