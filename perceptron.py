#loop:
	Z = -bias_factor
	for i in range(num_nodes):
		Z += inputNode[i] * weight[i]

	if Z >= 0 : h = 1
	else : h = -1

	for i in range(num_nodes):
		weight[i] += learn_rate*(y - h)*inputNode[i]