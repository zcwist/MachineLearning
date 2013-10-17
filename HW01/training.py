while(condition):
	for i in range(0,D):
		p=0
		for j in range(0,D[i]):
			p += w[j]*x[j]
		if (y[i] * p <= 0):
			for j in range(0,D[i]):
				w[j] += alpha*y[i]*x[j]
