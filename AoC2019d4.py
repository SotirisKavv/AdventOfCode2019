import re

possible = []

for x in range(387638,919123):
	if len(str(x))==6 and ''.join(sorted(str(x)))==str(x):
		for digit in str(x):
			if str(x).count(digit)==2:
				possible.append(x)
				break

print(possible)
print(len(possible))