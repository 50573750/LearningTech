#!/usr/bin/python

import math
import random

class LDA_Gibbs:
	corpus = [];
	dim_topic = 0;
	topics = [];
	doc_topic = [];
	word_topic = map();
		
	def __init__(self, dim_topic, corpus):
		self.dim_topic = dim_topic;
		self.corpus = corpus;
		for doc in self.corpus:
			doc_vec = map();
			for item in doc:
				doc_vec[item] = random.randint()%dim_topic;
			self.topics.append(doc_vec);
	
		doc_topic = [[0 for i in xrange(dim_topic)] for i in doc_topic];
		word_topic = map();
		for (ind,doc) in enumerate(self.corpus):
			for item in doc:
				doc_topic[ind][self.topics[ind][item]] = doc_topic[ind][self.topics[ind][item]] + 1;
				word_topic[item][self.topics[ind][item]] = word_topic[item][self.topics[ind][item]] + 1;
				
	def sampling(self):
		