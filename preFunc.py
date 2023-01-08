import numpy as np
class PreFunc:
    def __init__(self, function, x, y, a):
        self.function = function
        self.x = x
        self.y = y
        self.a = a

    def calc(self, data):
        self.data = data

        out = self.a*self.function(2*self.data - self.x) - self.y
        # (2/25)*(self.data)*(self.data-10)
        return out