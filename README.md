# Overview
This is a Python implementation of the <a href="https://en.wikipedia.org/wiki/Perceptron#Learning_algorithm">Perceptron algorithm</a>. I wanted to write my own artificial neural network to gain an understanding of how they work and started with the simplest one. I make use of no external libraries and the code, although easy to understand, is not very efficient. It uses .txt files!

A Perceptron is used to define a hyperplane which divides the input space into two half-spaces and can be used to make binary classification.

![perceptron](https://raw.githubusercontent.com/ckjoshi9/Perceptron/master/img/perceptron.png)

##### About the files
* `perceptron.py` : Python script used to run the algorithm.
* `constants.txt` : Used to read constant values for the algorithm- number of input nodes, bias factor and learning rate.
* `trainingData.txt` : Each line contains an input vector + subsequent output, used to train the perceptron.
* `testingData.txt` : Each line contains an input vector for which the classification has to be made.
* `weights.txt` : Used to read weights for each node of the input vector. Gets created/overwritten on training.
* `output.txt` : Contains input vector + predicted output combinations for the test data.

# Learning Boolean Functions
A boolean function is a two-class classification problem- the inputs are binary and the output is 1 if the corresponding function value is true and 0 otherwise.

Functions like AND and OR are linearly separable and are solvable using the perceptron. A perceptron implementing the AND function can be found in the `/res` folder. The OR can also be implemented by [modifying](https://github.com/ckjoshi9/Perceptron#usage) the `trainingData.txt` file.

![AND](https://raw.githubusercontent.com/ckjoshi9/Perceptron/master/img/AND.jpg)

Functions like XOR cannot be solved with the simple perceptron because their graphs are not linearly separable. Hence, there is no single line/hyperplane that can divide the input space into two classes. Note that a [multilayer perceptron (MLP)](https://en.wikipedia.org/wiki/Multilayer_perceptron) can be used to solve problems like the XOR.

![XOR](https://raw.githubusercontent.com/ckjoshi9/Perceptron/master/img/XOR.jpg)

# Usage
Modify the values in `constants.txt`, `trainingData.txt` and `testingData.txt` to your own data.

Then, train the perceptron algorithm using the following command (This will create/overwrite `weights.txt`):
```
python perceptron.py
```

Run the algorithm on the test data using the following command (This will create `output.txt`):
```
python perceptron.py test
```
