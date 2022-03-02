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
from proposal import Proposal_Generator
from mcmcstep import MCMC_Step

true_state = State(3,2,10,5,1)
start_state = State(3,2,10,5,1)

"""
the data is a series of times t_i, the time since the start 
of the experiment that the event happened
"""
data = makeData(true_state,10)

print(data)

log_Probability_Calculator = Log_Probability_Calculator(data)
print("log probability", log_Probability_Calculator.find_log_probability(start_state))

proposal_Generator = Proposal_Generator(0.01) 

start_state.print()

#MCMC_Step(10, start_state, log_Probability_Calculator, proposal_Generator)

#start_state.print()