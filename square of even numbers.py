#square of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#using lis comprehension
square_of_even = [x**2 for x in numbers if (lambda n:n%2==0)(x)]
print(square_of_even)
