fileHandler = open("FVWithoutNo.1.txt");
vectors = []
for lines in fileHandler.readlines():
	signal = int(lines[0:lines.find("{")])
	data = eval(lines[lines.find("{"):])
	vectors.append([signal, data]);
fileHandler.close();


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

alpha = 1
initialW = 1.0

itertimes = 40 #
count = 0
err = 1 #amount of errors in each iterator
while(err!=0 and count<=itertimes):
	err = 0;
	for signal, vector in vectors:
		p = 0;
		for feature in vector:
			w[feature] = w.get(feature, initialW) 
			p += w[feature] * vector[feature]
		if (signal * p <= 0):
			err += 1
			for feature in vector:
				w[feature] += alpha * signal * vector[feature]
	count +=1

print err, count

#clear w
zero = []
for key in w:
	if w[key] == 0:
		zero.append(key)
for feature in zero:
	del w[feature]

fileHandler = open("weights.txt",'w')
fileHandler.write(str(w))
fileHandler.close()





