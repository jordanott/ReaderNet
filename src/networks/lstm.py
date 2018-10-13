import torch
import torch.nn as nn
import torch.nn.functional as F


class LSTM(nn.Module):
    def __init__(self, hidden_size,output_size,num_layers=2):
        super(LSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers

        self.rnn = nn.LSTM(hidden_size, hidden_size, num_layers, dropout=0.2)
        self.l1 = nn.Linear(hidden_size, output_size)

        self.reset_hidden()

    def reset_hidden(self):
        self.hidden = (torch.randn(self.num_layers, 1, self.hidden_size),torch.randn(self.num_layers, 1, self.hidden_size))

    def forward(self, inputs):
        x, self.hidden = self.rnn(inputs, self.hidden)
        x = x[-1] # take last elem in seq
        x = self.l1(x)

        return x