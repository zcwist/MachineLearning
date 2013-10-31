import Learning
import Evaluation

for order in range(1,6):
	print "Learning without: No.%d Data" %order
	Learning.learnWithOut(order)
	print "Aplly to No.%d Data"
	print "Result:"
	Evaluation.evaluate(order)
	print "------------------"
