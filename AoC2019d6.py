#		globals
starmap = {}
path1 = {}
path2 = {}
step = []

#		functions
def road_length(spot, path):
	count = 0
	while spot != 'COM':
		count += 1
		path[spot] = starmap[spot]
		spot = starmap[spot]
	return count

#		test
test = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']

#		main
f = open('inputd6')

for line in f:
 	step.append(line)

for instruct in step:	#step/test
	planets = instruct.split(')')
	starmap[planets[1][:-1]] = planets[0]


you_l = road_length('YOU', path1)
san_l = road_length('SAN', path2)

common = set(path1) & set(path2)

print(you_l + san_l - 2*len(common) - 2)
