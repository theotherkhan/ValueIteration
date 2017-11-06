## Hasan Khan, hk4cd | Zach Danz, zyds4
## Value Iteration
from pandas import * # Makes 2D arrays render nice in terminal using DataFrame
global marked
global windFactor
global FINAL_STATE

########################################## EDIT THESE ##########################
windFactor = 2 # set to 0, 1, or 2
FINAL_STATE = (3,6)
################################################################################

## Board dimensions
bLength = 7
bWidth = 7

def findUtility(currPos):
	x, y = currPos
	#print " \n CURRENT POSITION: (",x,",",y,"), CURR VALUE: ", board[x][y] 
	
	if marked[x][y] == 1:
		#print "		Already marked this position"
		return board[x][y]

	marked[x][y] = 1
	currentReward = -1

	if currPos == FINAL_STATE:
		#print "HIT FINAL STATE!*******************************"
		currentReward = 0
		board[x][y] = 0
		return board[x][y]

	neighbors, ways = findNeighbors(board, currPos)
	#print "Neighbors of this pos: ", neighbors
	allRewards = []

	
	##Finding utilities of nieghbors
	## [N, S, E, W, NE, NW, SE, SW]
		
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

	utility = currentReward+(1*bestReward)

	#print "\tUtility of ", currPos, " is :", utility

	board[x][y] = utility

	return board[x][y]	


def findNeighbors(board, currPos):
	### Finds and returns all eligible neighbors of the current position

	x=currPos[0]	
	y=currPos[1]

	if windFactor !=0 and x in range (3,6): 	
		if y-windFactor >= 0:
			y = y-windFactor
			#print "	\t~wind~, new curr position:", x, y

	n = [] ## a list of coordinate tuples of eligible neighbors
	dirs = []
	
	## Structure: [N, S, E, W, SE, SW, NE, NW]
	addN = False
	addE = False
	addS = False
	addW = False

	if y > 0 and x>=0 and y-1>=0:  
		n.append((x, y-1)) ## North
		dirs.append("W")
		addN = True
	else: 
		n.append(False)
		dirs.append(".")

	if y+1 < bLength and x>=0 and y+1>=0:  
		n.append((x, y+1)) ## South
		dirs.append("W")
		addS = True
	else: 
		n.append(False)
		dirs.append(".")

	if x+1 < bWidth and x+1>=0 and y>=0:  
		n.append((x+1, y)) ## East
		dirs.append("S")
		addE = True 
	else: 
		n.append(False)
		dirs.append(".")

	if x > 0 and x-1>=0 and y>=0:  
		n.append((x-1, y)) ## West
		dirs.append("N")
		addW = True
	else: 
		n.append(False)
		dirs.append(".")

	if addS and addE: 
		n.append((x+1, y+1)) ## Southeast
		dirs.append("SE")
	else: 
		n.append(False)
		dirs.append(".")

	if addS and addW: 
		n.append((x-1, y+1)) ## Southwest
		dirs.append("SE")
	else: 
		n.append(False)
		dirs.append(".")

	if addN and addE: 
		n.append((x+1, y-1)) ## Northeast
		dirs.append("NE")
	else: 
		n.append(False)
		dirs.append(".")

	if addN and addW: 
		n.append((x-1, y-1)) ## Northwest
		dirs.append("NW")
	else: 
		n.append(False)
		dirs.append(".")
	#n.append((x, y)) Dont need to do this, accouned for in findUtility
	return n, dirs

##########################################################
##########################################################

## Init board
board = [[0] * bLength for i in range(bWidth)]
## board[row][col] indexing
print "\n\t~"+"VALUE ITER INPUT~"+"\n",DataFrame(board)
## Run value iteration on loop 
for i in range (0, 10):
	
	marked = [[0] * bLength for i in range(bWidth)]
	currPos = (0, 0)
	findUtility(currPos)
	#print ""
	#print DataFrame(board)

print "\n\t~"+"VALUE ITER OUTPUT~"+"\n",DataFrame(board)

policy = [[0] * bLength for i in range(bWidth)]

for i in range (0, len(board)):
	for j in range (0, len(board[0])):
		neighbors, ways = findNeighbors(board, (i,j))
		val = board[i][j]
		neighbors = [x for x in neighbors if x != False]
		ways = [x for x in ways if x != "."]
		neighborBoard = []
		for neighbor in neighbors:
			neighborBoard.append(board[neighbor[0]][neighbor[1]])
		maximum = max(neighborBoard)
		direction = ways[neighborBoard.index(maximum)]
		#print direction
		policy[i][j] = direction

policy[FINAL_STATE[0]][FINAL_STATE[1]] = "+"
print "\n\t"+"~POLICY~"+"\n",DataFrame(policy)