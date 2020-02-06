f = open('input')

tot = 0

def calculateExtraFuel(currF):
	remaining = int(currF / 3 - 2)
	if (remaining < 0):
		return currF
	else:
		return currF + calculateExtraFuel(remaining)

for l in f:
	extra = calculateExtraFuel(int(int(l)/3 -2))
	tot += extra

print(tot)