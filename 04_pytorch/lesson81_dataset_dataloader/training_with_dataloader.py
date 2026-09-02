import torch
import torch.nn as nn

from torch.utils.data import Dataset, DataLoader

class RegressionDataset(Dataset):
    def __int__(self):
        self.x = torch.arange(0,100,dtype=torch.float32).reshape(-1,1)
        self.y = (3 * self.x + 2)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        return (self.x[index], self.y[index])

class Model(nn.Module):
    def __int__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 16),
            nn.ReLU(),
            nn.Linear(16,1)
        )
    def forward(self, x):
        return self.network(x)


dataset = RegressionDataset()
loader = DataLoader(dataset, batch_size=16, shuffle = True)
model = Model()
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)

num_epochs = 100
for epoch in range(num_epochs):
    for x_batch, y_batch in loader:
        optimizer.zero_grad()
        prediction = model(x_batch)
        loss = loss_fn(prediction, y_batch)
        loss.backward()
        optimizer.step()
    if epoch % 10 == 0:
        print("epoch:", epoch, "loss:", loss.item())