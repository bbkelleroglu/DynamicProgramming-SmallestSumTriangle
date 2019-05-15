# Minimum Sum Path in a Triangle
I designed a dynamic programming algorithm and implemented it with Python to find the smallest sum in a descent from the triangle apex to its base through a sequence of adjacent numbers in an equilateral triangle with n numbers in its base.


In the below example, n is 4 and smallest sum path is shown in circles.

<img width="485" alt="Screen Shot 2019-05-15 at 20 46 44" src="https://user-images.githubusercontent.com/47689166/57801215-e937fa80-775b-11e9-9a8b-b7cc4a671b1c.png">

General approach for this kind of problem is to start at the bottom and work your way up. Therefore, i took the bottom row and adding each number to the row.

Sample Execution:
For tree :
[2]
[5, 4]
[1, 4, 7]
[8, 6, 9, 6]

Smallest sum : 14

or 

For tree:
[2]
[5, 4]
[7, 4, 1]
[8, 2, 9, 6]
[11, 3, 8, 8, 6]
Smallest sum : 15

Have fun :)




