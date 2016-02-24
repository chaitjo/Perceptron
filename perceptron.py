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
	y = inputLine[-1]

	Z = -bias_factor
	for i in range(num_nodes):
		Z += int(inputNodes[i]) * weight[i]

	if Z >= 0 : h = 1
	else : h = -1

	for i in range(num_nodes):
		weight[i] += learn_rate*(int(y) - h)*int(inputNodes[i])

	inputLine = trainingData.readline()

with open("weights.txt", "w") as weights:
	for i in range(num_nodes):
		weights.write(str(weight[i])+'\n')

trainingData.close()
