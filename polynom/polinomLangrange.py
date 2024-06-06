class polinomLangrange:
    def __init__(self, x, y, xi):
        self.x = x
        self.y = y
        self.xi = xi

    def hitung(self):
        n = len(self.x)
        yi = 0
        for i in range(n):
            li = 1
            for j in range(n):
                if i != j:
                    li *= (self.xi - self.x[j]) / (self.x[i] - self.x[j])
            yi += li * self.y[i]
        return yi