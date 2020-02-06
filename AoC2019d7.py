from itertools import permutations

def intcode(testArray, codes):
	count = 0
	i = 0
	while (count<len(testArray)):
		if testArray[count]%100==1:
			a = testArray[testArray[count+2]] if testArray[count]//1000==0 else testArray[count+2]
			temp = testArray[count]%1000
			b = testArray[testArray[count+1]] if temp//100==0 else testArray[count+1]
			testArray[testArray[count+3]] =  a + b
			count += 4
		elif testArray[count]%100==2:
			a = testArray[testArray[count+2]] if testArray[count]//1000==0 else testArray[count+2]
			temp = testArray[count]%1000
			b = testArray[testArray[count+1]] if temp//100==0 else testArray[count+1]
			testArray[testArray[count+3]] =  a * b
			count += 4
		elif testArray[count]%100==3:
			value = codes[0 if not i else 1]
			testArray[testArray[count+1]] = value
			i = 1
			count += 2
		elif testArray[count]%100==4:
			codes[1] = testArray[testArray[count+1]] if testArray[count]//100==0 else testArray[count+1]
			count += 2
		elif testArray[count]%100==5:
			a = testArray[testArray[count+2]] if testArray[count]//1000==0 else testArray[count+2]
			temp = testArray[count]%1000
			b = testArray[testArray[count+1]] if temp//100==0 else testArray[count+1]
			count = a if b!=0 else count+3
		elif testArray[count]%100==6:
			a = testArray[testArray[count+2]] if testArray[count]//1000==0 else testArray[count+2]
			temp = testArray[count]%1000
			b = testArray[testArray[count+1]] if temp//100==0 else testArray[count+1]
			count = a if b==0 else count+3
		elif testArray[count]%100==7:
			a = testArray[testArray[count+2]] if testArray[count]//1000==0 else testArray[count+2]
			temp = testArray[count]%1000
			b = testArray[testArray[count+1]] if temp//100==0 else testArray[count+1]
			testArray[testArray[count+3]] = 1 if b < a else 0
			count+=4
		elif testArray[count]%100==8:
			a = testArray[testArray[count+2]] if testArray[count]//1000==0 else testArray[count+2]
			temp = testArray[count]%1000
			b = testArray[testArray[count+1]] if temp//100==0 else testArray[count+1]
			testArray[testArray[count+3]] = 1 if b == a else 0
			count+=4
		elif testArray[count]%100==99:
			break
		else:break
	return codes[1]


#test
#array = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#array = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
#array = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
array = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#array = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

amplifiers = [5,6,7,8,9]
comb = list(permutations(amplifiers))

# f = open('inputd7')
# array=list(map(int, f.readline().split(',')))

outcomes = []
for nums in comb:
	for num in nums:
		code = [num, 0]
		start = intcode(array, code)
	outcomes.append(start)

print(max(outcomes))

