## Hasan Khan, hk4cd | Zach Danz, zyds4
## Value Iteration

def noWind():

	currPos = (0, 0)
	findUtility(currPos)

def findUtility(currPos):
	x, y = currPos
	print " \n CURRENT POSITION: (",x,",",y,"), CURR VALUE: ", board[x][y] 
	
	if marked[x][y] == 1:
		print "		Already marked this position"
		return board[x][y]

	marked[x][y] = 1
	#print "marked:", marked
	
	currentReward = -1

	if currPos == (3,6):
		#print "HIT FINAL STATE!*******************************"
		currentReward = 0
		utility = currentReward
		board[x][y] = utility
		return board[x][y]

	#print "currentReward:", currentReward
	neighbors = findNeighbors(board, currPos)
	print "Neighbors of this pos: ", neighbors
	allRewards = []

	#calculate action values, based on the given neighbors
	# [N, S, E, W, NE, NW, SE, SW]

	#print "		Finding utilities of nieghbors..."
		
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

	print "	UTILITY of ", currPos, " is :", utility

	board[x][y] = utility

	return board[x][y]	

def findNeighbors(board, currPos):
	''' Finds and returns all eligible neighbors of the current position'''

	x=currPos[0]	
	y=currPos[1]

	if windFactor !=0 and x in range (3,6): 	
		if y-windFactor >= -2:
			y = y-windFactor
			print "		~wind~, new curr position: ", x, y

	n= [] ## a list of coordinate tuples of eligible neighbors
	## Structure: [N, S, E, W | SE, SW, NE, NW]

	if y > 0 and x>=0 and y-1>=0:  
		n.append((x, y-1)) # North
		#print "		appending north"
	else: n.append(False)

	if y+1 < bLength and x>=0 and y+1>=0:  
		n.append((x, y+1)) # South
		#print "		appending south"
	else: n.append(False)

	if x+1 < bWidth and x+1>=0 and y>=0:  
		n.append((x+1, y)) # East
		#print "		appending east" 
	else: n.append(False)

	if x > 0 and x-1>=0 and y>=0:  
		n.append((x-1, y)) # West
		#print "		appending west"
	else: n.append(False)


	if y+1 < bLength and x+1 < bWidth and x+1>=0 and y+1>=0: 
		n.append((x+1, y+1)) # Southeast
		#print "		appending southeast"
	else: n.append(False)

	if y+1 < bLength and x > 0 and x-1>=0 and y+1>=0: 
		n.append((x-1, y+1)) # Southwest
		#print "		appending southwest"
	else: n.append(False)

	if y > 0 and x+1 < bWidth and x+1>=0 and y-1>=0 : 
			n.append((x+1, y-1))
			#print "		appending northeast"
	else: n.append(False)

	if y > 0 and x > 0 and x-1>=0 and y-1>=0: 
			n.append((x-1, y-1))
			#print "		appending northwest"
	else: n.append(False)

	#n.append((x, y))
	return n  

##########################################################
##########################################################

from pandas import *

global marked
global windFactor

bLength = 7
bWidth = 7

windFactor = 1


board = [[0] * bLength for i in range(bWidth)]
board[2][5] = 5
#board[row][col]
print DataFrame(board)

#'''

for i in range (0, 1):
	
	marked = [[0] * bLength for i in range(bWidth)]
	#board[6][3] = 0
	#marked[3][6] = 1
	noWind()
	print ""
	print DataFrame(board)
#'''





