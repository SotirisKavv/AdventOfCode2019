f = open('inputd3')

wirelines = f.read().split('\n')

instructions = {'R': [0 , 1], 'L': [0 , -1], 'U': [1 , 0], 'D': [-1 , 0],}
init_pos = [0, 0]

def move_wire(wire):
	wire = wire.split(',')
	line = {}
	pos_x, pos_y, secs_to_arrive = 0, 0, 0
	for instruction in wire:
		for o in range(int(instruction[1:])):
			pos_x += instructions[instruction[0]][0]
			pos_y += instructions[instruction[0]][1]
			secs_to_arrive += 1
			line[pos_x, pos_y] = secs_to_arrive
	return line

#tests
test1=['R8,U5,L5,D3','U7,R6,D4,L4']
test2=['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']
test3=['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']

# # line1 = move_wire(test3[0])
# line2 = move_wire(test3[1])

line1 = move_wire(wirelines[0])
line2 = move_wire(wirelines[1])

crosses = line1.keys() & line2.keys()

print(crosses)

distance = []

for points in crosses:
	distance.append(abs(line1[points])+abs(line2[points]))

print(sorted(distance)[0])
