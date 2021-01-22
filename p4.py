import numpy as np

inputs = [[1,2,3,2.5],
		  [2.0,5.0,-1.0,20],
		  [-1.5,2.7,3.3,-0.8]]

class Layer_Dense:
	def __init__(self,n_inputs,n_neurons):
		self.weights =  np.random.rand(n_neurons,n_inputs)
		self.biases = np.random.rand(1,n_nurons)
	def 