
"""

The proposal generator aims to pick points in parameter space
of the model, but it knows nothing of the data. 

In principle any generator will do, but such a generator
time untill convergence will be unusably large. 

As such one must consider the problem at hand when constructing 
a generator.

The parameters of our model are the two tep sizes and the two
expected lambda parameters, as well as the transion time.

As lambda is continuous, it makes sence to sample points near the
point we currently have. 

Howver, k is both discreat and small, leading to any change in it
being propotionally large and hence unlikly. 

Note that what the data offers as a continuous parameter is the mean 
rate of events lambda / k. 

Hence we have two steps, a step in lambda and a step in lamnda /k .

"""

import numpy as np

class Proposal_Generator:

	def __init__(self, logstep):
		self.log_step = logstep

	def generate(self, state_1, state_2):
		r = np.random.uniform()
		#we pick 0.9 as we expect a lot more changes in lambda than in k
		if (r<0.9):
			q_ratio = self.__Log_normal_step_k_cont(state_1, state_2)
		else:
			self.__change_step_1(state_1, state_2)
			self.__change_step_2(state_1, state_2)
			q_ratio = 1 #why?
		return q_ratio

	def __Log_normal_step_k_cont(self, state_1, state_2):
		#change lambda and t_change with a log normal distribution
		state_2.lambda_1 = state_1.lambda_1 * np.exp(self.log_step * np.random.normal() )
		state_2.lambda_2 = state_1.lambda_2 * np.exp(self.log_step * np.random.normal() )
		state_2.t_change = state_1.t_change * np.exp(self.log_step * np.random.normal() )
		#keep k fixed
		state_2.step_1 = state_1.step_1
		state_2.step_2 = state_1.step_2

		q_ratio = ( state_2.lambda_1 *state_2.lambda_2 * state_2.t_change ) / ( state_1.lambda_1 *state_1.lambda_2 * state_1.t_change )
		return q_ratio

	def __change_step_1(self, state_1, state_2):
		r = np.random.uniform()

		if (r<0.5):
			state_2.step_1 = state_1.step_1
		elif (r<0.75):
			state_2.step_1 = state_1.step_1+1
		else:
			state_2.step_1 = max(state_1.step_1-1,1)
		#holding lmabda  / k const 
		state_2.lambda_1 = state_2.step_1 * state_1.lambda_1 / state_1.step_1

	def __change_step_2(self, state_1, state_2):
		r = np.random.uniform()
		
		if (r<0.5):
			state_2.step_2 = state_1.step_2
		elif (r<0.75):
			state_2.step_2 = state_1.step_2 + 1
		else:
			state_2.step_2 = max(state_1.step_2 - 1, 1)
		state_2.lambda_2 = state_2.step_2 * state_1.lambda_2 / state_1.step_2
