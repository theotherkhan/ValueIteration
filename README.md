# ValueIteration

### Case 1: Windless

##### Value Function:

|   	| 00    | 01   	| 02   	| 03   	| 04   	| 05    | 06    |
|---	|------	|------	|------	|------	|------	|------	|------	|
| 00 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -3.0 	| -3.0 	| -3.0 	|
| 01 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -2.0 	| -2.0 	|
| 02 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -1.0 	| -1.0 	|
| 03 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -1.0 	| 0.0  	|
| 04 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -1.0 	| -1.0 	|
| 05 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -2.0 	| -2.0 	| -2.0 	|
| 06 	| -6.0 	| -5.0 	| -4.0 	| -3.0 	| -3.0 	| -3.0 	| -3.0 	|

##### An Optimal Policy for Case 1:

|   	| 00 	| 01 	| 02 	| 03  	| 04  	| 05    | 06 	|
|---	|---	|---	|---	|----	|----	|----	|---	|
| 00 	| E 	| E 	| E 	| SE 	| S  	| S  	| S 	|
| 01 	| E 	| E 	| E 	| E  	| SE 	| S  	| S 	|
| 02 	| E 	| E 	| E 	| E  	| E  	| SE 	| S 	|
| 03 	| E 	| E 	| E 	| E  	| E  	| E  	| + 	|
| 04 	| E 	| E 	| E 	| E  	| E  	| NE 	| N 	|
| 05 	| E 	| E 	| E 	| E  	| NE 	| N  	| N 	|
| 06 	| E 	| E 	| E 	| NE 	| N  	| N  	| N 	|

##### Another Optimal Policy for Case 1:

|   	| 00 	| 01 	| 02 	| 03  	| 04  	| 05  	| 06 	|
|---	|---	|---	|---	|----	|----	|----	|---	|
| 00 	| E 	| E 	| E 	| SE 	| S  	| S  	| S 	|
| 01 	| E 	| E 	| E 	| E  	| SE 	| S  	| S 	|
| 02 	| E 	| `SE`	| E 	| E  	| E  	| SE 	| S 	|
| 03 	| E 	| E 	| E 	| E  	| E  	| E  	| + 	|
| 04 	| E 	| E 	| E 	| E  	| E  	| NE 	| N 	|
| 05 	| E 	| E 	| E 	| E  	| NE 	| N  	| N 	|
| 06 	| E 	| E 	| E 	| NE 	| N  	| N  	| N 	|

Notice the change in X1,Y2 from E to SE. Many permutations such as this can be created by modifying places such as this. In general this scenario exists when there is more than one equal neighbor with the optimal next value; in this case, there are 3 '-4' nodes next to the '-5' in question, and so picking any of the 3 of them is valid for an optimal solution. 

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