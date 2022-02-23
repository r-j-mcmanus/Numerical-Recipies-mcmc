import state
import utility


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
	event_cumulative_delta_times = [0]
	event_cumulative_log_delta_times = [0]

	def __init__(self,  data):
		event_number = len(data)
		
		#as p is a function of the summation of delta time and log delta time, we compute these from the start for conveniance
		for i in range(1,event_number):
			event_cumulative_delta_times.append(data[i]-data[0])
			event_cumulative_log_delta_times.append(event_cumulative_log_delta_times[-1]+np.log(data[i]-data[i-1]))

	def find_probability(self, state):

		total_time = 0
		change_index = 0
		#where do change lambda
		for i in range(len(event_delta_times)):
			total_time += event_delta_times[i];
			if total_time > state.t_change:
				event_number_lower = i
				event_number_upper = len(event_delta_times) - event_number_lower
				sum_lower = event_cumulative_delta_times[i]
				sum_upper = event_cumulative_delta_times[-1] - sum_lower
				sum_log_lower = event_cumulative_log_delta_times[i]
				sum_log_upper = event_cumulative_log_delta_times[-1] - sum_log_lower

		probability = 0

		probability += event_number_lower * ( state.step_1 * np.log(state.lambda_1) - LogFactorial(state.step_1-1))
		probability += (state.step_1 - 1) * sum_log_lower
		probability += -state.lambda_1 * sum_lower

		probability += event_number_upper * ( state.step_2 * np.log(state.lambda_2) - LogFactorial(state.step_2-1))
		probability += (state.step_2 - 1) * sum_log_upper
		probability += -state.lambda_2 * sum_upper

		return probability