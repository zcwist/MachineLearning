fileHandler = open("s1FeatureVector.txt");
for lines in fileHandler.readlines():
	signal = int(lines[0:lines.find("[")])
	data = lines[lines.find("["):]
	print type(eval(data));
