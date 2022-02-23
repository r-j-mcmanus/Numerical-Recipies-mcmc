"""
	15.8.3 MCMC: A worked example

	At the beginning of an experiment, events occure Posson randomly
	 with a a mean rate lambda_1, but only every step_1 th event is 
	 recoreded. Then, at time t_change the mean rate changes to 
	 lambda_2, but now only every step_2 th event is recoreded. We 
	 are given the times t0, ..., tN-1 of the N recoreded events.

	What are the best fit values for lambda_i, step_i and t_change
"""

from state import State
from plog import Log_Probability_Calculator
from utility import makeData

true_state = State(1,3,100,1,1)
start_state = State(2,4,200,2,2)

data = makeData(true_state)
print(data)


log_Probability_Calculator = Log_Probability_Calculator(data)
print(log_Probability_Calculator.find_probability(start_state))


