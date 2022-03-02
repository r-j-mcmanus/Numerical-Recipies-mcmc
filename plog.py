from utility import LogFactorial

import numpy as np

class Log_Probability_Calculator():
	"""
	The probability of a given set of data can be very small,
	easily seen when the number of data points is large.
	As a result to prevent numerical problems, we work with the
	log of the probability

	As p(tau | lambda, k) = f(lambda,k) * tau**(k-1) * e**(- lmabda k)
	and P(D|x) = Pi_(t_i<t_c) p(tau_i | lambda_1, k_1) * Pi_(t_i>t_c) p(tau_i | lambda_2, k_2)

	We see that logP contains the sum of tau and the sum of log tau
	"""

	event_number = 0
	event_cumulative_times = []
	event_cumulative_log_delta_times = []

	def __init__(self,  data):
		self.event_number = len(data)
		
		"""
		as p is a function of the summation of delta time and 
		log delta time, we compute these from the start for conveniance.

		Note that the data is already in the form of time since the start
		"""
		self.event_cumulative_times = data

		self.event_cumulative_log_delta_times = [np.log(data[0])]
		for i in range(1,self.event_number):
			self.event_cumulative_log_delta_times.append(self.event_cumulative_log_delta_times[-1]+np.log(data[i]-data[i-1]))

		print("event_cumulative_times", self.event_cumulative_times)

	def find_log_probability(self, state):
		# finding where to change from one distribtuion to the next
		for i in range(len(self.event_cumulative_times)):
			if self.event_cumulative_times[i] >= state.t_change:
				event_number_lower = i #number of events that happen before the distribtuion change
				event_number_upper = len(self.event_cumulative_times) - event_number_lower #number of events that happen after the distribtuion change
				sum_lower = self.event_cumulative_times[i]
				sum_upper = self.event_cumulative_times[-1] - sum_lower
				sum_log_lower = self.event_cumulative_log_delta_times[i]
				sum_log_upper = self.event_cumulative_log_delta_times[-1] - sum_log_lower
				break

		log_probability = 0

		log_probability += event_number_lower * ( state.step_1 * np.log(state.lambda_1) - LogFactorial(state.step_1-1))
		log_probability += (state.step_1 - 1) * sum_log_lower
		log_probability += -state.lambda_1 * sum_lower

		log_probability += event_number_upper * ( state.step_2 * np.log(state.lambda_2) - LogFactorial(state.step_2-1))
		log_probability += (state.step_2 - 1) * sum_log_upper
		log_probability += -state.lambda_2 * sum_upper

		return log_probability