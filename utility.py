
import numpy as np

from scipy.special import gammaln

def LogFactorial(n):
	return gammaln(n+1)

def makeData(state, total_number_of_data):
	"""
	As k = 1, we have that the data follows an exponential distribution.

	p(tau | lambda) = lambda exp(- lambda tau)

	where tau = t(i+k) - t(i) is the time step between events
	"""
	lambda_1_true = state.lambda_1
	lambda_2_true = state.lambda_2
	t_change_true = state.t_change
	step_1_true = state.step_1
	step_2_true = state.step_2

	data = []
	t_accumulative = 0
	no_events_since_last_recording = 0
	while len(data) < total_number_of_data and t_accumulative <= t_change_true:
		dt = 1/lambda_1_true * np.log(lambda_1_true / np.random.uniform())
		t_accumulative += dt 
		no_events_since_last_recording += 1
		if no_events_since_last_recording == step_1_true:
			no_events_since_last_recording = 0
			data.append(t_accumulative)
		if t_accumulative >= t_change_true:
			break

	no_events_since_last_recording = 0
	while len(data) < total_number_of_data:
		dt = 1/lambda_1_true * np.log(lambda_1_true / np.random.uniform())
		t_accumulative += dt 
		no_events_since_last_recording += 1
		if no_events_since_last_recording == step_2_true:
			no_events_since_last_recording = 0
			data.append(t_accumulative)

	return data