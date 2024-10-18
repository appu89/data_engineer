# program on Factorial using functions

def factorial(n):
    fact = 1
    for i in range(1,n+1):
       fact  *= i


    return fact
print(factorial(2))
print(factorial(8))
print(factorial(5))
