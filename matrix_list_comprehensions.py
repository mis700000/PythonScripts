'''
You are given an n x m matrix with the following properties. Numbers are increasing from left to right,
 and the last number in a previous row is less then the first number in the next row 
 Example: 1 2 3 4 5 6 7 8 9 Write a method that given the matrix and a number return the row,
 column of the number if it exists in the matrix.
 Using the above matrix 4 would return (1,0), 8 would return (2,1). The solution should have a less 
 than n^2 runtime. Ask for BigOh runtime complexity, and why. 
 '''



#Method 2 : In this we used list comphrensions

matrix=[[1,2,3],[4,5,6],[7,8,9]] 

searchNumber    = 9

[(index, row.index(val)) for index, row in enumerate(matrix) if  searchNumber <= row[-1] and searchNumber in row]
'''for i in l:
#    if (i%2 == 0):
#        print(i)
        
[ i for i in l if i%2 == 0]
[<o/p expresion>  <input sequence>  <condition chekcing>]
'''