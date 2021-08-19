
def factorial(x):
	if x == 1: # Base case
		return 1
	else:
		subproblem_result = factorial(x-1) # Divide
		return x * subproblem_result # Combine

print(factorial(5))
