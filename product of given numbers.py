#product of given numbers
#Initializing number list
from functools import reduce
number = [2, 3, 4, 5]

#Using reduce with lambda to calculate product
product = reduce(lambda x,y:x*y,number)
print(product)