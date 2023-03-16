import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.nn import Linear


torch.manual_seed(42)   # set a random seed

model = Linear(in_features=1, out_features=1) # use a linear model

blue_x = (torch.rand(20) * 7).reshape(-1,1)   # random floats between 0 and 7
blue_y = torch.zeros(20).reshape(-1,1)

red_x = (torch.rand(20) * 7+3).reshape(-1,1)  # random floats between 3 and 10
red_y = torch.ones(20).reshape(-1,1)

X = torch.vstack([blue_x, red_x])   # matrix of x values
Y = torch.vstack([blue_y, red_y])   # matrix of y values

epochs = 2000   # run 2000 iterations
criterion = nn.BCELoss()    # implement binary cross entropy loss function

optimizer = torch.optim.SGD(model.parameters(), lr = .1) # stochastic gradient descent

for i in range(epochs):
    optimizer.zero_grad()
    Yhat = torch.sigmoid(model(X))
    loss = criterion(Yhat,Y)
    loss.backward()
    optimizer.step()

    print(f"epoch: {i+1}")
    print(f"loss: {loss: .5f}")
    print(f"slope: {model.weight.item(): .5f}")
    print(f"intercept: {model.bias.item(): .5f}")
    print()