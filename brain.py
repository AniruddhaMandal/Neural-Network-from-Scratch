import numpy as np

class Network:
	def __init__(self,layers):
		self.biases = [np.random.rand(y,1) for y in layers[1:]]
		self.weights = [np.random.rand(y,x) for x,y in zip(layers[:-1], layers[1:])]

	def feedforward(self,a):
		for w,b in zip(self.weights,self.biases):
			a = sigmoid(np.dot(w,a)+b)

		return a

	


def sigmoid(z):
	return 1.0/(1.0+np.exp(-z))