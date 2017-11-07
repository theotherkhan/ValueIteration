## Hasan Khan, hk4cd | Zach Danz, zsd4yr
## Value Iteration
from pandas import * # Makes 2D arrays render nice in terminal using DataFrame
import numpy as np
import matplotlib.pyplot as plt
global marked
global windFactor
global FINAL_STATE

########################################## EDIT THESE ##########################
windFactor = 1 # set to 0, 1, or 2
northerlyWindPattern = (0,0,0,0,0,0,0) #describes where wind factor is active 
southerlyWindPattern = (0,0,0,1,1,1,0) #note wind is given by the direction it is coming from
easterlyWindPattern  = (0,0,0,0,0,0,0)
westerlyWindPattern  = (0,0,0,0,0,0,0)
FINAL_STATE = (3,6) # Y, X -- row,col
SHOW_PLOT = True
################################################################################

global normalDirs 
global northFDirs
normalDirs = {".":".", "W":"W", "E":"E", "S":"S", 
	"N":"N","SE":"SE", "NE":"NE", "SW":"SW", "NW":"NW"}

DELTA = 10
## Board dimensions
bHeight = 7
bWidth = 7

def findUtility(currPos):
	print (currPos)
	row,col = currPos
	#print " \n CURRENT POSITION: (",x,",",y,"), CURR VALUE: ", board[x][y] 
	
	if marked[row][col] == 1:
		#print "		Already marked this position"
		return board[row][col]

	marked[row][col] = 1
	currentReward = -1

	if currPos == FINAL_STATE:
		#print "HIT FINAL STATE!*******************************"
		currentReward = 0
		board[row][col] = 0
		return board[row][col]

	#print "Neighbors of this pos: ", neighbors
	allRewards = []

	neighbors, ways = findNeighbors(board, currPos)

	for rogers in neighbors:
		if rogers != False :
			print("rogers not false:", rogers)
			allRewards.append(1*findUtility(rogers))
		
	bestReward = 0
	
	if len(allRewards)>0:
		bestReward = max(allRewards)

	PROB = 1.0
	utility = currentReward+(PROB*bestReward)

	#print "\tUtility of ", currPos, " is :", utility
	print ("utility:", utility)
	board[row][col] = utility

	return board[row][col]	


def findNeighbors(board, currPos):
	### Finds and returns all eligible neighbors of the current position

	row, col = currPos

	windChangesYourStay = False

	if windFactor !=0:
		if (((northerlyWindPattern[col] == 1) != (southerlyWindPattern[col] == 1)) or
			((easterlyWindPattern [row] == 1) != (westerlyWindPattern [row] == 1))):
			print("\twind changes your stay position")
			windChangesYourStay = True

		if northerlyWindPattern[col] == 1: 	
			if row+windFactor <= bHeight-1:
				row = row+windFactor
		if southerlyWindPattern[col] == 1:
			if row-windFactor >= 0:
				row = row-windFactor
		
		if easterlyWindPattern [row] == 1:
			if col-windFactor >= 0:
				col = col-windFactor
		if westerlyWindPattern [row] == 1:
			if col+windFactor <= bWidth-1:
				col = col+windFactor
		#print "	\t~wind~, new curr position:", x, y
		

	n = [] ## a list of coordinate tuples of eligible neighbors
	dirs = []
	
	addN = False
	addE = False
	addS = False
	addW = False


	if windChangesYourStay == True:
		n.append((row, col)) #self
		desiredDir = "."
		dirs.append(normalDirs[desiredDir])
	

	if row > 0: #North
		n.append((row-1, col))
		desiredDir = "N"
		dirs.append(normalDirs[desiredDir])
		addN = True
	

	if row < bHeight-1: #South
		n.append((row+1, col))
		desiredDir = "S"
		dirs.append(normalDirs[desiredDir])
		addS = True
	

	if col > 0: #West
		n.append((row, col-1))
		desiredDir = "W"
		dirs.append(normalDirs[desiredDir])
		addW = True
	

	if col < bWidth-1: #East
		n.append((row, col+1))
		desiredDir = "E"
		dirs.append(normalDirs[desiredDir])
		addE = True
	

	if addN and addE: #Northeast
		n.append((row-1, col+1))
		desiredDir = "NE"
		dirs.append(normalDirs[desiredDir])
	
	if addS and addE: #Southeast
		n.append((row+1, col+1))
		desiredDir = "SE"
		dirs.append(normalDirs[desiredDir])
	

	if addN and addW: #Northwest
		n.append((row-1, col-1))
		desiredDir = "NW"
		dirs.append(normalDirs[desiredDir])
	
	if addS and addW: #Southwest
		n.append((row+1, col-1))
		desiredDir = "SW"
		dirs.append(normalDirs[desiredDir])
	
	#n.append((x, y)) Dont need to do this, accouned for in findUtility
	return n, dirs

def drawPlot(numBoard):
	if SHOW_PLOT == True:
		cmap = plt.cm.Blues
		img = plt.imshow(numBoard, cmap=cmap)
		plt.xlabel('X Coords')
		plt.ylabel('Y Coords')
		#fig = plt.figure()
		plt.show()
		#fig.savefig('plot.png', bbox_inches='tight')

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
	currPos = (0, 0) #stored Y, X
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

if(SHOW_PLOT == True):
	drawPlot(np.array(board))