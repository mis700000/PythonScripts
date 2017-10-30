In [44]:
class base():
    
    x  =8   ##102569 
    
    def __init__(self) :
        self.__A = 1
        self.B = 2
    
    def getA(self):
        return self.__A

    def getB(self):
        return self.B   ###o/p : 2
    
    def getB(self, BB):
        return self.B + BB


class child(base):
    
    def getB(self):
        return self.B + 1   #o/p:3
    
    def methdArgs(self, *args) :
        for i in args:
            print(i)
    
    def methdKwrgs(self, **Kwargs) :
        print(Kwargs)
        
#obj1 = child()
#obj1.methdArgs([1,2,3], [4,5,6])
#obj1.methdKwrgs({'A'})


class Sample():
    p =1
    
    def C(self):
        return self.p

obj3 = Sample()
dir(obj3)
Out[44]:
['C',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'p']
In [20]:
m=n= 3
matrix        =[[1,2,3],[4,5,6],[7,8,9]] 
searchNumber    = 9
print(enumerate(matrix).__sizeof__())
for rowIndex,rowArray in enumerate(matrix) :
    if searchNumber <= rowArray[-1] :
        print([ (rowIndex,columnindex) for columnindex,value in enumerate(rowArray) if value== searchNumber ])
    
    else :
         continue
24
[(2, 2)]
24
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
In [47]:
l = [1,2,3,4,5,6]
#for i in l:
#    if (i%2 == 0):
#        print(i)
        
[ i for i in l if i%2 == 0]
[<o/p expresion>  <input sequence>  <condition chekcing>]
2
4
6
Out[47]:
[2, 4, 6]
In [49]:
l = [8,9,10]
print(l)

for i in enumerate(l):
    print(i)
[8, 9, 10]
(0, 8)
(1, 9)
(2, 10)
In [ ]:
 