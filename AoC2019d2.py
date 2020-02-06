f = open('inputd2')

def intcode(testArray):
	count = 0
	while (count<len(testArray)):
		if testArray[count]==1:
			testArray[testArray[count+3]] = testArray[testArray[count+1]] + testArray[testArray[count+2]]
			count += 4
		elif testArray[count]==2:
			testArray[testArray[count+3]] = testArray[testArray[count+1]] * testArray[testArray[count+2]]
			count += 4
		elif testArray[count]==99:
			break
		else:break

for noun in range(100):
	for verb in range(100):
		f = open('inputd2')
		testArray=list(map(int, f.readline().split(',')))
		testArray[1] = noun
		testArray[2] = verb
		intcode(testArray)
		if testArray[0]==19690720:
			print(100*noun+verb)
			print(testArray)