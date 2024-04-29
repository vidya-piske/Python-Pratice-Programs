x = 10
def func():
    global x
    x += 5
    return x
    
print(func())