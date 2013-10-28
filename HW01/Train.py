fileHandler = open("s1FeatureVector.txt");
vectors = []
for lines in fileHandler.readlines():
	signal = int(lines[0:lines.find("{")])
	data = eval(lines[lines.find("{"):])
	vectors.append([signal, data]);

w = {}

# pseudocode of Rosenblatt's algorithm
# for (i = 0; i < D; i ++) {
# 	p = 0;
# 	for (j = 0; j < D(i); j ++) {
# 		p += w[j] * x[j] ;
# 	}
# 	if (y[i] * p <= 0) {
# 		for (j = 0; j < D(i); j ++) {
# 			w[j] += alpha * y[i] * x[j];
# 		}
# 	
# }

alpha = 100
initialW = 1.0
count = 0
while(count < 2):
	for signal, vector in vectors:
		p = 0;
		for feature in vector:
			w[feature] = w.get(feature, initialW) 
			p += w[feature] * vector[feature]
		if (signal * p <= 0):
			for feature in vector:
				w[feature] += alpha * signal * vector[feature]
	count +=1

# total = 0
# correct = 0
# for signal, vector in vectors:
# 	for feature in vector:
# 		p += w[feature] * vector[feature]
# 	total += 1
# 	correct += 1 if(p*signal > 0) else 0

# print total
# print correct


