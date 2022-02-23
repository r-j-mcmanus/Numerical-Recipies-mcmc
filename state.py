class State():
	"""Contains the components of the data"""
	lambda_1 = 0
	lambda_2 = 0
	t_change = 0
	step_1 = 0
	step_2 = 0

	plog = 0

	def __init__(self, l1, l2, tc, k1, k2):
		self.lambda_1 = l1 
		self.lambda_2 = l2
		self.t_change = tc 
		self.step_1 = k1
		self.step_2 = k2 