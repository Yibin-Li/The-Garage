import numpy as np
def least_square(a,b):
	"""
	least square problem ax = b 
	takes a and b, return x
	"""
	return np.dot(np.dot(np.linalg.inv(np.dot(a.T, a)), a.T), b)

a = np.array([[1, 1, 1],
			[0, 1, 1],
			[0, 1, 1],
			[0, 0, 1],
			[0, 0, 1]])

a2 = np.array([[1, 1, -1],
			[0, 1, -1],
			[1, 0, 0],
			[1, -1, 1],
			[0, -1, 1]])

a3 = a2[:, :2]
print(a3)			
b = np.array([1, -1, 0, 1, 0]).T			
print(np.dot(a3, least_square(a3,b)))

def gramschmidt(A):
	"""
	Applies the Gram-Schmidt method to A
	and returns Q and R, so Q*R = A.
	"""
	R = np.zeros((A.shape[1], A.shape[1]))
	Q = np.zeros(A.shape)
	for k in range(0, A.shape[1]):
		R[k, k] = np.sqrt(np.dot(A[:, k], A[:, k]))
		Q[:, k] = A[:, k]/R[k, k]
		for j in range(k+1, A.shape[1]):
			R[k, j] = np.dot(Q[:, k], A[:, j])
			A[:, j] = A[:, j] - R[k, j]*Q[:, k]
	return Q, R

y, x = gramschmidt(a)
#print(np.dot(A, least_square(A,b)))
print(y)
print()
print(x)
def cro(signal1, signal2):
	"""
	correlate signal2 to signal1
	The function returns correlation
	"""
	return [np.correlate(signal1, np.roll(signal2,k))[0] for k in range(len(x))]

def OMP(sparsity, measurements, A):
	"""
	The basic equation is Ax = measurements but with x sparse  
	Sparsity is the number of valid entries in x
	Takes vector measurements and vector A and returns vector x
	>>> A = np.array([[1, 1, 0, -1],
			[1, 0, -1, 0],
			[0, 1, 1, 1]])
	>>> measurements = np.array([[4, 6, 3]]).T
	>>> OMP(2, measurements, A)
	array([6.33333333, 0., 0., 2.66666667])
	"""
	r = measurements.copy()
	indices = []
	
	# Threshold to check error. If error is below this value, stop.
	THRESHOLD = 0.1
	
	# For iterating to recover all signal
	i = 0
	
	while i < sparsity and np.linalg.norm(r) > THRESHOLD: 
		# Calculate the correlations
		#print('%d - '%i,end="",flush=True)
		corrs = A.T.dot(r)

		# Choose highest-correlated pixel location and add to collection
		best_index = np.argmax(np.abs(corrs))
		indices.append(best_index)

		# Build the matrix made up of selected indices so far
		Atrunc = A[:, indices]

		# Find orthogonal projection of measurements to subspace
		# spanned by recovered codewords
		b = measurements
		xhat = np.linalg.lstsq(Atrunc, b)[0]  

		# Find component orthogonal to subspace to use for next measurement
		r = b - Atrunc.dot(xhat)
		
		i = i + 1
	result = np.zeros(len(A[0]))
	for i in indices:
		result[i] = xhat[0]
		xhat = xhat[1:]
	return np.array(result)