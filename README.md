# Overview
This is a Python implementation of the <a href="https://en.wikipedia.org/wiki/Perceptron#Learning_algorithm">Perceptron algorithm</a>. It is the simplest form of an artificial neural network which can be used to make binary classifications.

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
