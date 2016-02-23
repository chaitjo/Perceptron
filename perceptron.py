trainingData = open("training.txt", "r")

num_nodes = 2		# TODO : function to find this out
bias_factor = 1
learn_rate = 0.5

weight = []
inputNodes = []

with open("weights.txt", "r") as weights:
	for i in range(num_nodes):
		weight[i] = weights.readline()[:-1]

while inputLine:
	inputNodes, y = inputLine.split()[:-1], inputLine.split[-1]

	Z = -bias_factor
	for i in range(num_nodes):
		Z += inputNodes[i] * weight[i]

	if Z >= 0 : h = 1
	else : h = -1

	for i in range(num_nodes):
		weight[i] += learn_rate*(y - h)*inputNodes[i]

	inputLine = trainingData.readline()[:-1]

with open("weights.txt", "w") as weights:
	for i in range(num_nodes):
		weights.writeline(weight[i])