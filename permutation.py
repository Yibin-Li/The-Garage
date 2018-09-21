import itertools
def permutation(input):
	""" 
	Do permutation on the input list. Return a list of all possible results.
	However, this algorithm is SLOW. itertools.permutations is much faster.
	
	>>> permutation([1])
	[[1]]
	
	>>> permutation([1, 2, 3])
	[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
	
	>>> len(permutation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
	3628800
	
	"""
	result = []
	
	
	if input is None or len(input) == 0:
		return "Invalid input. The input is empty or none."
	elif len(input) == 1:
		return [input]
		
	for i in input:
		new_input = input.copy()
		new_input.remove(i)
		for e in [[i] + k for k in permutation(new_input)]:
			result.append(e)
	
	return result

print(len([i for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]))
#print(len(permutation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))