import numpy as np

class MLP:
    def __init__(self, pnum, rate=0.1, beta=1):
        ### pnum means the number of perceptron in network ###
        self.pnum = pnum
        self.LR = rate
        self.Beta = beta
        #self.randsort = range(pd)
        #np.random.shuffle(self.randsort)


    def GoForward(self, x, y, T):
        i = 0
        ori_v = np.zeros(np.shape(x)[1])
        ### init weight ###
        ### weight of Hidden layer ###
        # @_@ every perceptron has a weight vector, pnum perceptrons concatenate as a matrix #
        wh_matrix = np.random.random(np.shape(x)[1] * pnum)
        wh_matrix = np.reshape(wh_matrix, (np.shape(x)[1], pnum))
        #np.shape(wh_matrix) = (np.shape(x)[1], pnum)
        ### weight of Output layer ###
        wo_matrix = np.random.random(np.shape(x)[1] * pnum)
        np.shape(wo_matrix) = (np.shape(x)[1], pnum)
        ###############################

        randsort = range(np.shape(x)[0])
        np.random.shuffle(randsort)
        train_x = np.array(x)
        train_y = np.array(y)
        train_x = train_x[randsort, :]
        train_y = train_y[randsort, :]

        while i < T:
            ### hidden layer number (h, g) ###
            h_array = np.dot(train_x, self.wh.T)
            g_alpha = 1/(1+exp(-1*self.Beta*h_alpha))
            ### output layer 
            h_
        return True

