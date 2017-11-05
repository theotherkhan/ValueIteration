## Hasan Khan, hk4cd | Zach Danz, zyds4
## Value Iteration
from pandas import * # Makes 2D arrays render nice in terminal using DataFrame

global FINAL_STATE
FINAL_STATE = 3,6
global northerlyWind
global southerlyWind
global easterlyWind
global westerlyWind
northerlyWind = 0,0,0,0,0,0,0 
southerlyWind = 0,0,0,0,0,0,0 
easterlyWind = 0,0,0,0,0,0,0 
westerlyWind = 0,0,0,0,0,0,0 
global marked

######################## UTILITY ###########################
####################### FUNCITONS ##########################

def findUtility(currPos):
	#print "\n"
	#print DataFrame(board)
	#print DataFrame(marked)


	x = currPos[0]
	y = currPos[1]
	#print " \n CURRENT POSITION: (",x,",",y,"), CURR VALUE: ", board[x][y] 
	
	#if marked[x][y] == 1:
		#print "\tAlready marked this position"
		#return board[x][y]

	if board[x][y] > 0:
		#cd GOo	marked[x][y] = 0
		return board[x][y]

	marked[x][y] = 1
	currentReward = -1

	if currPos == FINAL_STATE:
		#print "HIT FINAL STATE!*******************************"
		currentReward = 100
		board[x][y] = 0
		return board[x][y]

	neighbors, ways = findSucessors(board, currPos)
	#print "Neighbors of this pos: ", neighbors
	allRewards = []
	
	##Finding utilities of nieghbors
	## [N, S, E, W, NE, NW, SE, SW]

	for  onceAndFutureKing in neighbors:
		if onceAndFutureKing != False :
			if marked[onceAndFutureKing[0]][onceAndFutureKing[1]] == 0: #not being calculated
				allRewards.append(1*findUtility(onceAndFutureKing))
		
	allRewards.append(board[x][y]) #stay
		
	bestReward = 0
	
	if len(allRewards)>0:
		#print "allRewards of ", currPos, ":", allRewards
		bestReward = max(allRewards)	

	utility = currentReward+(1*bestReward)

	#print "\tUtility of", currPos, "is :", utility

	board[x][y] = utility
	marked[x][y] = 0

	return board[x][y]	


def findSucessors(board, currPos):
	''' Finds and returns all eligible neighbors of the current position'''

	x=currPos[0]	
	y=currPos[1]

	n = [] ## a list of coordinate tuples of eligible neighbors
	
	## Structure: [N, S, E, W, SE, SW, NE, NW]
	dirs = []

	if y > 0 and x>=0 and y-1>=0:  
		n.append((x, y-1)) 
		dirs.append('W')	## North
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if y+1 < bLength and x>=0 and y+1>=0:  
		n.append((x, y+1))
		dirs.append('EAST')	## South
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if x+1 < bWidth and x+1>=0 and y>=0:  
		n.append((x+1, y))
		dirs.append('S')	## East
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if x > 0 and x-1>=0 and y>=0:  
		n.append((x-1, y)) 
		dirs.append('N')	## West
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if y+1 < bLength and x+1 < bWidth and x+1>=0 and y+1>=0: 
		n.append((x+1, y+1))
		dirs.append('SE')	## Southeast
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if y+1 < bLength and x > 0 and x-1>=0 and y+1>=0: 
		n.append((x-1, y+1))
		dirs.append('NE')	## Southwest
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if y > 0 and x+1 < bWidth and x+1>=0 and y-1>=0 : 
		n.append((x+1, y-1))
		dirs.append('SW')	## Northeast
	else: 
		n.append(False)
		dirs.append(u'\8635')

	if y > 0 and x > 0 and x-1>=0 and y-1>=0: 
		n.append((x-1, y-1))
		dirs.append('NW')	## Northwest
	else: 
		n.append(False)
		dirs.append(u'\8635')
	
	return n, dirs  

########################  MAIN #############################
####################### FUNCITON ###########################

## Board dimensions
bLength = 7
bWidth = 7

## Init boards
board = [[0] * bLength for i in range(bWidth)] #to store the results
marked = [[0] * bLength for i in range(bWidth)] #to store current visitation
policy = [[0] * bLength for i in range(bWidth)]
board[FINAL_STATE[0]][FINAL_STATE[1]] = 100
## board[row][col] indexing
print DataFrame(board)

## Run value iteration on loop 
for i in range (0, 1):
	currPos = (0,0)
	findUtility(currPos)
	print "\n"
	print DataFrame(board)

for i in range(0, bWidth):
	for j in range(0, bLength):
		currPos = i,j
		myValue = board[i][j]
		myDir = "."
		waystones, ways = findSucessors(board, currPos)
		for p in range(0, len(waystones)):
			path = waystones[p]
			if path != False:
				way = ways[p]
				contender = board[path[0]][path[1]]
				#print "for", i, j, "we have a value of", myValue, "and direction", myDir, "with contender", contender, "and direction", way
				if contender > myValue:
					myValue = board[path[0]][path[1]]
					myDir = way
		policy[i][j] = myDir

print "\n"
print DataFrame(policy)
