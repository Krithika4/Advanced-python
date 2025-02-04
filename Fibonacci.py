#Fibonacci
fibonacci = lambda n:([fib.append(fib[-1] + fib[-2]) or fib for fib in [[0,1]] for _ in range(n-2)][-1][:n])
print(fibonacci(10))