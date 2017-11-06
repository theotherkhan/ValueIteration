## Hasan Khan, hk4cd | Zach Danz, zsd4yr
## Value Iteration
from pandas import * # Makes 2D arrays render nice in terminal using DataFrame
global marked
global windFactor
global FINAL_STATE

########################################## EDIT THESE ##########################
windFactor = 1 # set to 0, 1, or 2
northerlyWindPattern = (0,0,0,0,0,0,0) #describes where wind factor is active 
southerlyWindPattern = (0,0,0,1,1,1,0) #note wind is given by the direction it is coming from
easterlyWindPattern  = (0,0,0,0,0,0,0)
westerlyWindPattern  = (0,0,0,0,0,0,0)
FINAL_STATE = (3,6) # Y, X
################################################################################

global normalDirs 
global northFDirs
normalDirs = {	"W":"W", 	"E":"E", 	"S":"S", 	"N":"N",	"SE":"SE", 	"NE":"NE", 	"SW":"SW", 	"NW":"NW"}

DELTA = 10
## Board dimensions
bHeight = 7
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

	#print "Neighbors of this pos: ", neighbors
	allRewards = []

	neighbors, ways = findNeighbors(board, currPos)

	for rogers in neighbors:
		if rogers != False:
			allRewards.append(1*findUtility(rogers))
	allRewards.append(board[x][y])
		
	bestReward = 0
	
	if len(allRewards)>0:
		bestReward = max(allRewards)

	PROB = 1.0
	utility = currentReward+(PROB*bestReward)

	#print "\tUtility of ", currPos, " is :", utility

	board[x][y] = utility

	return board[x][y]	


def findNeighbors(board, currPos):
	### Finds and returns all eligible neighbors of the current position

	x=currPos[0]	
	y=currPos[1]

	if windFactor !=0:
		if northerlyWindPattern[x] == 1: 	
			if y-windFactor >= 0:
				y = y-windFactor
		if southerlyWindPattern[x] == 1:
			if y+windFactor < bHeight:
				y = y+windFactor
		if easterlyWindPattern [y] == 1:
			if x-windFactor >= 0:
				x = x-windFactor
		if westerlyWindPattern [y] == 1:
			if x+windFactor < bWidth:
				x = x+windFactor
		#print "	\t~wind~, new curr position:", x, y
		

	n = [] ## a list of coordinate tuples of eligible neighbors
	dirs = []
	
	addN = False
	addE = False
	addS = False
	addW = False

	if y > 0 and x>=0 and y-1>=0:  
		n.append((x, y-1)) ## North
		desiredDir = "W"
		dirs.append(normalDirs[desiredDir])
		addN = True
	else: 
		n.append(False)
		dirs.append(".")

	if y+1 < bWidth and x>=0 and y+1>=0:  
		n.append((x, y+1)) ## South
		desiredDir = "E"
		dirs.append(normalDirs[desiredDir])
		addS = True
	else: 
		n.append(False)
		dirs.append(".")

	if x+1 < bHeight and x+1>=0 and y>=0:  
		n.append((x+1, y)) ## East
		desiredDir = "S"
		dirs.append(normalDirs[desiredDir])
		addE = True 
	else: 
		n.append(False)
		dirs.append(".")

	if x > 0 and x-1>=0 and y>=0:  
		n.append((x-1, y)) ## West
		desiredDir = "N"
		dirs.append(normalDirs[desiredDir])
		addW = True
	else: 
		n.append(False)
		dirs.append(".")

	if addS and addE: 
		n.append((x+1, y+1)) ## Southeast
		desiredDir = "SE"
		dirs.append(normalDirs[desiredDir])
	else: 
		n.append(False)
		dirs.append(".")

	if addS and addW: 
		n.append((x-1, y+1)) ## Southwest
		desiredDir = "NE"
		dirs.append(normalDirs[desiredDir])
	else: 
		n.append(False)
		dirs.append(".")

	if addN and addE: 
		n.append((x+1, y-1)) ## Northeast
		desiredDir = "SE"
		dirs.append(normalDirs[desiredDir])
	else: 
		n.append(False)
		dirs.append(".")

	if addN and addW: 
		n.append((x-1, y-1)) ## Northwest
		desiredDir = "NE"
		dirs.append(normalDirs[desiredDir])
	else: 
		n.append(False)
		dirs.append(".")
	
	#n.append((x, y)) Dont need to do this, accouned for in findUtility
	return n, dirs

##########################################################
##########################################################

print("PROGRAM START")
print("\tWind Factor:", windFactor, 
	"\n\tSoutherly along columns", [i for i, x in enumerate(southerlyWindPattern) if x == 1],
	"\n\tNortherly along columns", [i for i, x in enumerate(northerlyWindPattern) if x == 1],
	"\n\tEasterly  along columns", [i for i, x in enumerate(easterlyWindPattern)  if x == 1],
	"\n\tWesterly  along columns", [i for i, x in enumerate(westerlyWindPattern)  if x == 1])

## Init board
board = [[0.0] * bWidth for i in range(bHeight)]
## board[row][col] indexing
print ("\n\t~"+"BASE ARRAY (BEFORE)~"+"\n",DataFrame(board))
## Run value iteration on loop 
for i in range (0, DELTA):
	
	marked = [[0.0] * bWidth for i in range(bHeight)]
	currPos = (0, 0)
	findUtility(currPos)
	#print ""
	#print DataFrame(board)


print ("\n\t~"+"VALUE FUNCTION( (AFTER)~"+"\n",DataFrame(board))#.to_csv())

policy = [[""] * bWidth for i in range(bHeight)]

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
print ("\n\t"+"~OPTIMAL POLICY ATTEMPT~"+"\n", DataFrame(policy))#.to_csv())