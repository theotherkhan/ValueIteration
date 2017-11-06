# ValueIteration

### Case 1: Windless

##### Value Function:

|   	| 0    	| 1    	| 2    	| 3    	| 4    	| 5    	| 6    	|
|---	|------	|------	|------	|------	|------	|------	|------	|
| 0 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -3.0 	| -3.0 	| -3.0 	|
| 1 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -2.0 	| -2.0 	|
| 2 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -1.0 	| -1.0 	|
| 3 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -1.0 	| 0.0  	|
| 4 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -1.0 	| -1.0 	|
| 5 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -2.0 	| -2.0 	|
| 6 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -3.0 	| -3.0 	| -3.0 	|

##### Policy for Case 1:

|   	| 0 	| 1 	| 2 	| 3  	| 4  	| 5  	| 6 	|
|---	|---	|---	|---	|----	|----	|----	|---	|
| 0 	| E 	| E 	| E 	| SE 	| S  	| S  	| S 	|
| 1 	| E 	| E 	| E 	| E  	| SE 	| S  	| S 	|
| 2 	| E 	| E 	| E 	| E  	| E  	| SE 	| S 	|
| 3 	| E 	| E 	| E 	| E  	| E  	| E  	| + 	|
| 4 	| E 	| E 	| E 	| E  	| E  	| NE 	| N 	|
| 5 	| E 	| E 	| E 	| E  	| NE 	| N  	| N 	|
| 6 	| E 	| E 	| E 	| NE 	| N  	| N  	| N 	|

### Case 2: Weak Wind

##### Value Function:


##### Policy for Case 2:



### Changing the Wind Factor

To modify the wind factor (0 for none, 1 for 1 offset, 2 for 2, etc...), open valueIteration.py in your favorite editor and modify the value of the variable windFactor on line 9. 

### Compilation and Run

* We compiled the project with Python 3.6.0
* To run the project, run the command ./run.sh
    * note: this may install a few packages if you don't already have them
* Our script assumes your python 3 is aliased as 'python3'

### Authors

* Hasan Khan hk4cd
* Zachary Danz zsd4yr