exit()
from torch import nn

class FullyConnectedBlock(nn.Module):
    def __init__(self, in_size, hidden_size, out_size):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_size, hidden_size),
            nn.ReLU(),

            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),

            nn.Linear(hidden_size, out_size),
        )

# common way to parametrize the number of hidden layers

class FullyConnectedBlock(nn.Module):
    def __init__(self, in_size, hidden_size, hidden_layers, out_size):
        super().__init__()
        layers = []

        layers.append(nn.Linear(in_size, hidden_size))
        layers.append(nn.ReLU())

        for _ in range(hidden_layers):
            layers.append(nn.Linear(hidden_size, hidden_size))
            layers.append(nn.ReLU())

        layers.append(nn.Linear(hidden_size, out_size))

        self.net = nn.Sequential(*layers)

# a less noisy version

class FullyConnectedBlock(nn.Module):
    def __init__(self, in_size, hidden_size, hidden_layers, out_size):
        super().__init__()
        def make_layers():
            yield nn.Linear(in_size, hidden_size)
            yield nn.ReLU()

            for _ in range(hidden_layers):
                yield nn.Linear(hidden_size, hidden_size)
                yield nn.ReLU()

            yield nn.Linear(hidden_size, out_size)

        self.net = nn.Sequential(*make_layers())
