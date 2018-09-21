def combination (set_num, input_list):
	""" Return all non-repeated possible combination 
		(a list of lists) of given set number.
	
	>>> combination(2, ["1", "2", "3", "4"])
	[["1", "2"], ["1", "3"], ["1", "4"], ["2", "3"], ["2", "4"], ["3", "4"]]
	
	>>> combination(1, ["4", "2", "1"])
	[["4"], ["2"], ["1"]]
	
	"""
	result = []
	if input_list is None or len(input_list) == 0:
		return "Invalid input. The input is empty or none."
	elif (set_num > len(input_list)):
		return "Invalid combination. Partition number is greater than the length of input"
	
	if (set_num == 1):
		for x in input_list:
			e = list(x)
			result.append(e)
		return result
	for i in range(len(input_list)):
		further_result = combination(set_num - 1, input_list[i + 1:])
		for k in further_result:
			e = list(input_list[i])
			result.append(e + k)
	return result

print(combination(3, ["2", "3", "4", "5", "9", "1", "6", "7"]))
