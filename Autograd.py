import torch

# Autograd package and learning gradience
# Gradience are essential for model optimization

# Default value for grad is false, changing it to true will give tensors grad_fn function
# That corresponds whatever actions they are performing


# weights = torch.ones(4, requires_grad=True)

# for epoch in range(5):
#     model_output = (weights*3).sum()

#     model_output.backward()

#     print(weights.grad)

#     weights.grad.zero_()


# x = torch.randn(3, requires_grad=True)
# print(x)


# Dropping gradient
# x.requires_grad_(False)
# x.detach()
# with torch.no_grad():

# x.requires_grad_(False)
# print(x)
# y = x.detach()
# print(y)
# with torch.no_grad():
#     z = x +2
#     print(z)

# y = x +2
# print(y)
# z = y*y*2
# # z = z.mean()
# print(z)

# v = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float32)

# z.backward(v)
# print(x.grad)
