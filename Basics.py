import torch
import numpy as np

x = torch.ones(5, requires_grad=True)
print(x)


# Running operations on GPU or CPU, if changes are made in numpy which runs in cpu
# Then those changes are applied to pytorch modules too since they are using the same memory
# To avoid this we need to run pytorch on GPU, but this is only possible with CUDA support 
# Hence the 'if' check

# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     x = torch.ones(5, device=device)
#     y = torch.ones(5)
#     y = y.to(device)
#     z = x + y
#     z = z.to("cpu")

# print(x)
# print(y)
# print(z)

# z += 1

# print(x)
# print(y)
# print(z)

# Basic commands and testing - mostly math operations

# x = torch.rand(4,4)
# print(x)
# # dimension of tensors (all in one line)
# y = x.view(16)
# # dimension of tensors (spread in two lines)
# y = x.view(-1, 8)
# print(y.size())

# x = torch.rand(5,3)
# print(x)
# # all items from a column
# print(x[:,0])
# # all items from a row
# print(x[:1,:])
# # tensor from exact position
# print(x[:1,1])
# # specific tensor value (can only by used if single item)
# print(x[:1,1].item())

# x = torch.rand(2,3)
# y = torch.rand(2,3)


# z = x - y
# z = torch.add(x, y)
# z = torch.mul(x, y)
# z = torch.div(x, y)
# print(z)

# y = x + y
# y.add_(x)
# y.mul_(y)
# y.div_(y)
# print(y)
