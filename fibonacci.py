def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1) + factorial(n-2)
    
print(factorial(4))