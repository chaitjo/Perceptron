import sys
test = False
train = False
if  sys.argv[1] == 'test' : test = True
esle if sys.argv[1] == 'train' : train = True

trainingData = open("training.txt", "r")

with open("constants.txt", "r") as constants:
	num_nodes = int(constants.readline()[:-1])
	bias_factor = float(constants.readline()[:-1])
	learn_rate = float(constants.readline()[:-1])

weight = []
inputNodes = []

try:
	with open("weights.txt", "r") as weights:
		inputWeight = weights.readline()
		while inputWeight:
			weight.append(float(inputWeight[:-1]))
			inputWeight = weights.readline()
except IOError:
	for i in range(num_nodes):
		weight.append(1.0)

inputLine = trainingData.readline()
while inputLine:
	inputLine = inputLine[:-1].split()
	inputNodes = inputLine[:-1]
	outputNode = inputLine[-1]

	# Weighted Sum function
	wSum = -bias_factor
	for i in range(num_nodes):
		wSum += int(inputNodes[i]) * weight[i]

	# Activation function
	if wSum >= 0 : prediction = 1
	else : prediction = -1

	# Weight update rule - gradient descent method
	for i in range(num_nodes):
		weight[i] += learn_rate * (int(outputNode) - prediction) * int(inputNodes[i])

	inputLine = trainingData.readline()

with open("weights.txt", "w") as weights:
	for i in range(num_nodes):
		weights.write(str(weight[i])+'\n')

trainingData.close()
