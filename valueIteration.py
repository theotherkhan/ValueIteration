## Hasan Khan, hk4cd | Zach Danz, zyds4
## Value Iteration

def noWind():

	currPos = (0, 0)
	findUtility(currPos)

	return 0

def findUtility(currPos):
	x, y = currPos
	#print "curr position: ", x, y
	
	if marked[x][y] == 1:
		return board[x][y]

	marked[x][y] = 1
	#print "marked:", marked
	
	currentReward = -1
	if currPos == (3,6):
		currentReward = 0


	#print "currentReward:", currentReward
	neighbors = findNeighbors(board, currPos)
	#print "neighbors of ", currPos, "are: ", neighbors
	allRewards = []
	

	#calculate action values, based on the given neighbors
	#for k in range (0, len(neighbors)):
		
	if (neighbors[0] != False):
		allRewards.append(1*findUtility(neighbors[0]))
	
	if (neighbors[1] != False):
		allRewards.append(1*findUtility(neighbors[1]))
	
	if (neighbors[2] != False):	
		allRewards.append(1*findUtility(neighbors[2]))
	
	if (neighbors[3] != False):
		allRewards.append(1*findUtility(neighbors[3]))	
	
	if (neighbors[4] != False):
		allRewards.append(1*findUtility(neighbors[4]))
	
	if (neighbors[5] != False):
		allRewards.append(1*findUtility(neighbors[5]))
	
	if (neighbors[6] != False):
		allRewards.append(1*findUtility(neighbors[6]))

	if (neighbors[7] != False):
		allRewards.append(1*findUtility(neighbors[7]))
	
	allRewards.append(board[x][y])
		
	bestReward = 0
	
	if len(allRewards)!=0:
		#print "allRewards of ", currPos, ":", allRewards
		bestReward = max(allRewards)	

	#print "bestAction: ", bestReward 
	utility = currentReward+(1*bestReward)

	#print "utility of ", currPos, " is :", utility
	board[x][y] = utility
	return board[x][y]
	

def findNeighbors(board, currPos):
	''' Finds and returns all eligible neighbors of the current position'''

	x=currPos[0]	
	y=currPos[1]

	n= [] ## a list of coordinate tuples of eligible neighbors
	## Structure: [ N, S, E, W]

	if y != 0:  n.append((x, y-1)) # North
	else: n.append(False)

	if y+1 < bLength:  n.append((x, y+1)) # South
	else: n.append(False)

	if x+1 < bWidth:  n.append((x+1, y))
	else: n.append(False)

	if x != 0:  n.append((x-1, y))
	else: n.append(False)


	if y+1 < bLength and x+1 < bWidth: n.append((x+1, y+1)) 
	else: n.append(False)

	if y+1 < bLength and x != 0: n.append((x-1, y+1))
	else: n.append(False)

	if y!=0 < bLength and x+1 < bWidth: n.append((x+1, y-1))
	else: n.append(False)

	if y!=0 < bLength and x != 0: n.append((x-1, y-1))
	else: n.append(False)

	#n.append((x, y))
	return n  

## Value Iteration #######################################
from pandas import *

global marked

bLength = 7
bWidth = 7

#board = [[-1] * bLength for i in range(bWidth)]
board = [[0] * bLength for i in range(bWidth)]

marked = [[0] * bLength for i in range(bWidth)]
board[3][6] = 0 

print DataFrame(board)

for i in range (0, 6):
	noWind()
	marked = [[0] * bLength for i in range(bWidth)]
print DataFrame(board)

for i in range (0, 10):
	noWind()
	marked = [[0] * bLength for i in range(bWidth)]
print DataFrame(board)

for i in range (0, 15):
	noWind()
	marked = [[0] * bLength for i in range(bWidth)]
print DataFrame(board)
#noWind()
#noWind()

#print DataFrame(board)



