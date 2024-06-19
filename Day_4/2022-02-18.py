import torch




x = torch.ones(5)


if torch.cuda.is_available():
    device = torch.device('cuda')