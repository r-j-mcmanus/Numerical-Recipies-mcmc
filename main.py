"""
	15.8.3 MCMC: A worked example

	At the beginning of an experiment, events occure Posson randomly
	 with a a mean rate lambda_1, but only every step_1 th event is 
	 recoreded. Then, at time t_change the mean rate changes to 
	 lambda_2, but now only every step_2 th event is recoreded. We 
	 are given the times t0, ..., tN-1 of the N recoreded events.

	What are the best fit values for lambda_i, step_i and t_change
"""

import state
import utility

"""
To begin we generate the data:
"""

lambda_1_true = 1
lambda_2_true = 3
t_change_true = 100
step_1_true = 1
step_1_true = 1
total_number_of_data = 200

"""
	As k = 1, we have that the data follows an exponential distribution.

	p(tau | lambda) = lambda exp(- lambda tau)

	where tau = t(i+k) - t(i) is the time step between events
"""




print(data)

