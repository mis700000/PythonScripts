

'''
You are given an n x m matrix with the following properties. Numbers are increasing from left to right,
 and the last number in a previous row is less then the first number in the next row 
Example: 1 2 3 4 5 6 7 8 9 Write a method that given the matrix and a number return the row,
column of the number if it exists in the matrix. Using the above matrix
 4 would return (1,0), 8 would return (2,1). The solution should have a less than n^2 runtime.
 Ask for BigOh runtime complexity, and why. 
'''




'''
I have done in two ways :

Method 1 :  Here will compare the matrix values only if the last element of matrix row value is 
greater than or equal to input search, by this way we no need to traverse all the elements .
'''

m*n matrix 

m=n= 3

matrix        =[[1,2,3],[4,5,6],[7,8,9]] 

searchNumber    = 9

for rowIndex,rowArray in enumerate(matrix) :

    if val <= rowArray[-1] :

        print([ (rowIndex,columnindex) for columnindex,value in enumerate(rowArray) if value== searchNumber ])

    

    else :

         continue          




