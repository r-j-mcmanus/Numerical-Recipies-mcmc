class State():
	"""Contains the components of the data"""
	lambda_1 = 0
	lambda_2 = 0
	t_change = 0
	step_1 = 0
	step_2 = 0

	plog = 0

	def __init__(self, l1=0, l2=0, tc=0, k1=0, k2=0):
		lambda_1 = l1 
		lambda_2 = l2
		t_change = tc 
		step_1 = k1
		step_2 = k2 