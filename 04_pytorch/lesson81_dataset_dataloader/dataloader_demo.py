from torch.utils.data import DataLoader

from custom_dataset import RegressionData

dataset = RegressionData()

loader = DataLoader(dataset, batch_size=4, drop_last = True)

for batch_index, (x, y) in enumerate(loader):
    print("batch", batch_index)
    print("x:", x.shape)
    print("y:", y.shape)