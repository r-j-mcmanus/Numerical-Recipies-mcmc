
import numpy as np

def makeData():
"""
	As k = 1, we have that the data follows an exponential distribution.

	p(tau | lambda) = lambda exp(- lambda tau)

	where tau = t(i+k) - t(i) is the time step between events
"""

	lambda_1_true = 1
	lambda_2_true = 3
	t_change_true = 100
	step_1_true = 1
	step_2_true = 1
	total_number_of_data = 200

	data = []
	t_accumulative = 0
	while True:
		dt = 1/lambda_1_true * np.log(lambda_1_true / np.random.uniform())
		t_accumulative += dt 
		if t_accumulative <= t_change_true:
			data.append(t_accumulative)
		else:
			break

	for i in range(len(data),total_number_of_data):
		dt = 1/lambda_1_true * np.log(lambda_1_true / np.random.uniform())
		t_accumulative += dt 
		data.append(t_accumulative)

	return data