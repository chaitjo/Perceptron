# Overview
This is a Python implementation of the <a href="https://en.wikipedia.org/wiki/Perceptron#Learning_algorithm">Perceptron algorithm</a>. It is the simplest form of an artificial neural network which can be used to make binary classifications.

![perceptron](https://raw.githubusercontent.com/ckjoshi9/Perceptron/master/images/perceptron.png)

The perceptron model is an assembly of inter-connected nodes and weighted links. The output node first sums up each of its input value according to the weights of its links, compare the weighted sum against some threshold theta (the bias factor) and producse an output based on the sign of the result.

![equations](https://raw.githubusercontent.com/ckjoshi9/Perceptron/master/images/equations.png)

During training, the weight parameters are adjusted based on the <a href="https://en.wikipedia.org/wiki/Gradient_descent">gradient descent method</a>, until the outputs of the perceptron become consistent with the true outputs of training data.

For each training example (**x**, y), the predicted output h is computed. The weight parameters are updated based on the following rule - 

_**w** = **w** + L * (y - h) * **x**_ 

where L is the learning rate, such that L ∈ (0,1].

##### About the files
* `perceptron.py` : Python script used to run the algorithm.
* `constants.txt` : Used to read constant values for the algorithm- number of input nodes, learning rate and bias factor.
* `trainingData.txt` : Each line contains an input vector + subsequent output, used to train the perceptron.
* `testingData.txt` : Each line contains an input vector for which the classification has to be made. 
* `weights.txt` : Used to read weights for each node of the input vector. Gets created/overwritten on training.
* `output.txt` : Contains input vector + predicted output combinations for the test data.

# Usage
Modify the values in `constants.txt`, `trainingData.txt` and `testingData.txt` to your own data.

Then, train the perceptron algorithm using the following terminal command (This will create/overwrite `weights.txt`):
```
python perceptron.py
```

Run the algorithm on the test data using the following terminal command (This will create `output.txt`):
```
python perceptron.py test
```
