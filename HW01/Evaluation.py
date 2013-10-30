fileHandler = open("s5FeatureVector.txt");
vectors = []
for lines in fileHandler.readlines():
	signal = int(lines[0:lines.find("{")])
	data = eval(lines[lines.find("{"):])
	vectors.append([signal, data]);
fileHandler.close();

fileHandler = open("weights.txt");
w = eval(fileHandler.read())


tp = 0 #true positive
fp = 0 #false positive
fn = 0 #false negative
tn = 0 #true negative

for signal, vector in vectors:
	p = 0
	for feature in vector:
		p += w.get(feature, 0.0) * vector[feature]
	if (signal > 0 and p > 0): 
		tp += 1.0
	elif (signal < 0 and p > 0): 
		fp += 1.0
	elif (signal < 0 and p < 0): 
		tn += 1.0
	else: 
		fn += 1.0

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1score = 2 * precision * recall / (precision + recall)
print "precision = %f" %precision
print "recall = %f" %recall
print "f1 score = %f" %f1score
