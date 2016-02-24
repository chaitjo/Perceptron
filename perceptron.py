import sys
train = True
test = False
if len(sys.argv) >= 2 and sys.argv[1] == 'test' : 
	test = True
	train = False

if test: data = open("testingData.txt", "r")
else: data = open("trainingData.txt", "r")

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

inputLine = data.readline()
while inputLine:
	inputLine = inputLine[:-1].split()
	if test: inputNodes = inputLine
	else:
		inputNodes = inputLine[:-1]
		outputNode = inputLine[-1]

	# Weighted Sum function
	wSum = -bias_factor
	for i in range(num_nodes):
		wSum += int(inputNodes[i]) * weight[i]

	# Activation function
	if wSum >= 0 : prediction = 1
	else : prediction = -1

	if train:
		# Weight update rule
		# based on gradient descent method
		for i in range(num_nodes):
			weight[i] += learn_rate * (int(outputNode) - prediction) * int(inputNodes[i])

	if test:
		# Writing prediction to output file
		with open("output.txt", "a") as output:
			for i in range(num_nodes):
				output.write(str(inputNodes[i]) + ' ')
			output.write(str(prediction) + '\n')

	inputLine = data.readline()

if train:
	# Writing updated weights to weights.txt
	with open("weights.txt", "w") as weights:
		for i in range(num_nodes):
			weights.write(str(weight[i])+'\n')

data.close()
