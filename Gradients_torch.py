# 1 ) Design model (input, output size, forward pass)
# 2 ) Construct loss and optimizer
# 3 ) Training loop
#   - forward pass: compute prediction
#   - backward pass: gradients
#   - update weights

import torch
import torch.nn as nn

# f = w * x

#f = 2 * x
X = torch.tensor([[1],[2],[3],[4]], dtype=torch.float32)
Y = torch.tensor([[2],[4],[6],[8]], dtype=torch.float32)

X_test = torch.tensor([5], dtype=torch.float32)
n_samples, n_features = X.shape
print(n_samples, n_features)

input_size = n_features
output_size = n_features

#w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

#model prediction
#def forward(x):
#    return w * x

model = nn.Linear(input_size, output_size)

class LinearRegression(nn.Module):

    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        # define layers
        self.lin = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.lin(x)

model = LinearRegression(input_size, output_size)

# gradient
# Mean squared = 1/N * (w*x - y)**2
#dJ/dw = 1/N 2x (w*x -y)

print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

#training
learning_rate = 0.02
n_iters = 500

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(n_iters):
    # prediction = forward pass
    y_pred = model(X)

    # loss
    l = loss(Y, y_pred)

    # gradients = backward pass
    l.backward() # dl/dw

    #update weights
    optimizer.step()

    # zero gradients
    optimizer.zero_grad()

    if epoch % 50 == 0:
        [w, b] = model.parameters()
        print(f'epoch {epoch+1}: w = {w[0][0].item():.3f}, loss = {l:.8f}')


print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')
