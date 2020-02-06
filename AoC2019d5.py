def intcode(testArray):
	count = 0
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
			value = int(input(':'))
			testArray[testArray[count+1]] = value
			count += 2
		elif testArray[count]%100==4:
			print(testArray[testArray[count+1]] if testArray[count]//100==0 else testArray[count+1])
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


#test
#array = [3,9,8,9,10,9,4,9,99,-1,8]
#array = [3,9,7,9,10,9,4,9,99,-1,8]
#array = [3,3,1108,-1,8,3,4,3,99]
#array = [3,3,1107,-1,8,3,4,3,99]
#array = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#array = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
#array = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


f = open('inputd5')
array=list(map(int, f.readline().split(',')))

intcode(array)
print(array)
