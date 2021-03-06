import torch
import torch.nn as nn
import torch.nn.functional as F


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=2):
        super(LSTM, self).__init__()

        self.hidden_size = hidden_size; self.num_layers = num_layers

        # init lstm
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, dropout=0.2)
        # init hidden state
        self.reset_hidden()


    def reset_hidden(self):
        self.hidden = (torch.zeros(self.num_layers, 1, self.hidden_size).cuda(),
            torch.zeros(self.num_layers, 1, self.hidden_size).cuda())

    def forward(self, inputs):
        x, self.hidden = self.rnn(inputs, self.hidden)
        x = x[-1] # take last elem in seq

        return x
