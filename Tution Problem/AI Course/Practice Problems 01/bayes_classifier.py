import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm
from scipy.stats import multivariate_normal

class PolyX:
    def __init__(self, degree, use_constant=True):
        self.degree = degree
        self.use_constant = use_constant

    def transform(self, X):
        m, n = X.shape
        if self.use_constant:
            Xext = np.zeros((m, n*self.degree+1))
            Xext[:, 0] = 1
            k = 2
        else:
            Xext = np.zeros((m, n*self.degree))
            k = 1

        for p in range(1, self.degree+1):
            for j in range(n):
                Xext[:, k-1] = X[:, j]**p
                k += 1

        return Xext

def load_data(data_file, delimiter=None):
    """
    Load the data from a .txt file. Last column is the target variable, while the rest are the features.
    """
    # Load the data from the file
    # By default, genfromtxt assumes delimiter=None, 
    # meaning that the line is split along white spaces (including tabs)
    # and that consecutive white spaces are considered as a single white space.
    
    
    # Split the data into X and Y
    
    
    return X, Y


def split_data(X, Y, train_fraction):
    """
    Split the data into training and testing sets.
    """
   
    
    return 
  


def reorder_data(X, Y):


    
    return 


def gauss_plot(mean, cov, color_string, *varargs):
    # plot an ellipse indicating a Gaussian distribution using the given plot style string
    if len(mean) > 2:
        raise ValueError('Can only plot 2-dimensional Gaussians')

    theta = np.arange(0, 2*np.pi, 0.01)
    circle = np.array([np.sin(theta), np.cos(theta)]).T
    ell = np.dot(circle, sqrtm(cov))
    ell += np.ones(ell.shape) * mean

    plt.plot(mean[0], mean[1], color_string + 'x')
    plt.plot(ell[:,0], ell[:,1], color_string, *varargs)
    #plt.show()

def get_color(idx):
    # Get a color based on the index
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    if idx >= len(colors):
        raise ValueError('Not enough colors')
    return colors[idx % len(colors)]


class BayesClassifier:
    def __init__(self, mode=None):
        self.means = None
        self.covs = None
        self.classes = None
        self.mode = mode


    def fit(self, X, Y):
        # Get the unique classes
        self.classes = np.unique(Y)
        # Calculate the mean and covariance of each class
        self.means = []
        self.covs = []
        for i, cls in enumerate(self.classes):
            idx = np.where(Y == cls)[0]
            mean = np.mean(X[idx, :], axis=0)
            cov = np.cov(X[idx, :].T)
            self.means.append(mean)
            self.covs.append(cov)
        #if self.mode == 'equal':
            

    def predict(self, X):
        # Predict the class of each point
        Ypred = np.zeros(X.shape[0])
        for i in range(X.shape[0]):
            # Calculate the probability of each class
            probs = []
            for j in range(len(self.classes)):
                prob = multivariate_normal.pdf(X[i, :], self.means[j], self.covs[j])
                probs.append(prob)
            # Assign the class with the highest probability
            Ypred[i] = self.classes[np.argmax(probs)]
        return Ypred

    def score(self, X, Y):
        Ypred = self.predict(X)
        return np.mean(Ypred == Y)
    
    def draw_decision_boundary(self, X, Y, polyx=None, nsamples=100, outfile=None):
        # Draw the decision boundary
        # First, get the range of the data
        xmin, xmax = np.min(X[:, 0]), np.max(X[:, 0])
        ymin, ymax = np.min(X[:, 1]), np.max(X[:, 1])
        # Create a meshgrid
        offset = 0.1 * (xmax - xmin)
        x = np.linspace(xmin - offset, xmax + offset, nsamples)
        y = np.linspace(ymin - offset, ymax + offset, nsamples)
        X1, X2 = np.meshgrid(x, y)
        # Predict the class of each point in the meshgrid
        Z = np.zeros(X1.shape)
        for i in range(X1.shape[0]):
            for j in range(X1.shape[1]):
                # Calculate the probability of each class
                probs = []
                for k in range(len(self.classes)):
                    if polyx:
                        rst = polyx.transform(np.array([[X1[i, j], X2[i, j]]]))
                        prob = multivariate_normal.pdf(rst[0], self.means[k], self.covs[k])
                    else:
                        prob = multivariate_normal.pdf([X1[i, j], X2[i, j]], self.means[k], self.covs[k])
                    probs.append(prob)
                # Assign the class with the highest probability
                Z[i, j] = self.classes[np.argmax(probs)]

        # Plot the decision boundary
        plt.contourf(X1, X2, Z, alpha=0.3)
        for i, cls in enumerate(self.classes):
            idx = np.where(Y == cls)[0]
            plt.scatter(X[idx, 0], X[idx, 1], c=get_color(i))
            mean = np.mean(X[idx, :], axis=0)
            cov = np.cov(X[idx, :].T)
            gauss_plot(mean, cov, get_color(i))

        plt.show()
        if outfile:
            plt.savefig(outfile)


# # Exercise (1.1)



# # Exercise (1.2)



# Exercise (1.4)



# # Exercise (1.5)



# # Exercise (1.6)



# Exercise (1.7)




