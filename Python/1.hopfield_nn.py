#!/usr/bin/python

import math;
import random;

def sign(x):
	if x >=0 :
		return +1;
	else:
		return -1;
	
class hopfield_nn:
	weights = [];
	dim = 0;

	def __init__(self, dim):
		self.dim = dim;
		self.weights = [[ 0 for col in xrange(dim)] for row in xrange(dim)];

	def learn(self, dataset):
		for d in dataset:
			for i in xrange(self.dim):
				for j in xrange(self.dim):
					self.weights[i][j] = self.weights[i][j] + d[i] * d[j];

	def infer(self, dataitem):
		out = dataitem;
		for epos in xrange(1000):
			pre = [0 for i in xrange(self.dim)];
			for i in xrange(self.dim):
				for j in xrange(self.dim):
					pre[i] = pre[i] + self.weights[i][j] * out[j];
				pre[i] = sign(pre[i]);
			out = pre;
		return out;
	
dataset = [[sign(random.random() - 0.5) for i in xrange(20)] for d in xrange(10)];

hnn = hopfield_nn(20);
hnn.learn(dataset);

print dataset[5];
print hnn.infer(dataset[5]);

				