import numpy as np
#Param Declare Later, Algorithm First

class Perceptron:
    def __init__(self, p, r=0.1):
        self.w = np.random.random(p)
        self.LR = r
        self.DecisionFunction = np.zeros(p)

    def updateW(self, w, x, y, y0):
        return (w+self.LR*(y-y0)*x)

    def training(self, x, y, T):
        train_x, train_y = np.array(x), np.array(y)
        for i in range(T):
            ### Count Every Row ###
            for m in range(train_x.shape[0]):
                fire = np.dot(train_x[m,:], self.w.T)
                y0 = 1 if fire>0 else 0
                self.w = self.updateW(self.w, train_x[m, :], y[m], y0)
            print self.w

    def testing(self, x):
        fire = np.dot(x, self.w)
        return map(lambda x: 1 if x>0 else 0, fire)

