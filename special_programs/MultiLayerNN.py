#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:11:35 2020

@author: arun

Neural Network for an OR Truth Table

1 1 1
1 0 1
0 1 1
0 0 0
"""

import numpy as np

class NeuralNetwork:
    
    def __init__(self, iNodes, hNodes, oNodes, lr, iterations=10000):
        self.iNodes = iNodes
        self.hNodes = hNodes
        self.oNodes = oNodes
        self.iterations = iterations
        
        # learning rate
        self.lr = lr
        
        np.random.seed(5771)
        
        # Weights
        self.W_ih = np.random.rand(self.iNodes, self.hNodes)
        self.W_ho = np.random.rand(self.hNodes, self.oNodes)
        
        # Biases
        # self.B_h = np.random.rand(self.hNodes)
        # self.B_o = np.random.rand(self.oNodes)
        
    
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1.0 - x)
        
    def status(self):
        
        print(f"This 1 hidden-layer neural network has {self.iNodes} input nodes, {self.hNodes} hidden nodes, and {self.oNodes} output nodes")
        print(f"The weights between input and hidden layer are {self.W_ih}")
        print(f"The weights between hidden and output layer are {self.W_ho}")
        # print(f"The biases of the hidden layer are {self.B_h}")
        # print(f"The biases of the output layer are {self.B_o}")
        
    def feedforward(self, input_data):
        
        # Weighted sum of inputs sent to the hidden layer
        self.WS_ih = np.dot(input_data, self.W_ih) # + self.B_h
        # Activation / Output from the hidden layer
        self.Act_ih = self.sigmoid(self.WS_ih)
        
        # Weighted sum of hidden layer inputs sent to the output layer
        self.WS_ho = np.dot(self.Act_ih, self.W_ho) # + self.B_o
        # Activation / Output from the output layer
        self.Act_ho = self.sigmoid(self.WS_ho)
        
        return self.Act_ho
    
    def backpropagation(self, inputs, target, prediction):
        
        self.output_error = target - prediction
        self.output_delta_w = self.output_error * self.sigmoid_derivative(prediction)
        # self.output_delta_b = self.sigmoid_derivative(prediction)
        self.W_ho += self.lr * np.dot(self.Act_ih.T, self.output_delta_w)
        #self.B_h += self.lr * np.matmul(self.Act_ih, self.output_delta_b)
        
        self.hidden_error = self.output_error.dot(self.W_ho.T)
        self.hidden_delta_w = self.hidden_error * self.sigmoid_derivative(self.Act_ih)
        # self.hidden_delta_b = self.sigmoid_derivative(self.Act_ih)
        self.W_ih += self.lr * np.dot(inputs.T, self.hidden_delta_w)
        # self.B_i += self.lr * np.dot(self.inputs.T, self.hidden_delta_b)
        
    def training(self, input_data, output_data):
        
        # Training data
        for iteration in range(self.iterations):
            
            # Prediction and backpropagation
            prediction = self.feedforward(input_data)
            self.backpropagation(input_data, output_data, prediction)
            print(f"iteration = {iteration}, error = {prediction - output_data}")
                

brain = NeuralNetwork(2, 3, 1, 0.75, 10000)
brain.status()
input_data = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
output_data = np.array([[1], [1], [1], [0]])
brain.training(input_data, output_data)

entry = np.array([0, 0])
result = brain.feedforward(entry)
print(result)