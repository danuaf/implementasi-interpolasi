import numpy as np

class polinomNewton:
    def __init__(self, x, y, xi):
        self.x = x
        self.y = y
        self.xi = xi

    def hitung(self):
        n = len(self.x)
        divided_diff = np.zeros((n, n))
        divided_diff[:, 0] = self.y
        
        for j in range(1, n):
            for i in range(n - j):
                divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (self.x[i + j] - self.x[i])
        
        yi = 0
        for i in range(n):
            term = divided_diff[0, i]
            for j in range(i):
                term *= (self.xi - self.x[j])
            yi += term
        return yi