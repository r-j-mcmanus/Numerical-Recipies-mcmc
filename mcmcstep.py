from state import State

import numpy as np

def MCMC_Step(number_of_steps, start_state, log_Probability_Calculator, proposal_Generator):
	log_probability_current = log_Probability_Calculator.find_log_probability(start_state)
	sugested_state = State(0,0,0,0,0)
	acceptence_number=0

	for i in range(0,number_of_steps):
		q_ratio = proposal_Generator.generate(start_state,sugested_state)
		
		log_probability_sugested = log_Probability_Calculator.find_log_probability(sugested_state)
		acceptance_probability = min (1 , q_ratio * np.exp( log_probability_sugested - log_probability_current ) )
		
		r = np.random.uniform()
		if (r < acceptance_probability):
			start_state = sugested_state
			log_probability_current = log_probability_sugested
			acceptence_number += 1

	return acceptence_number