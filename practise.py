# def func(x, y=2, z=3):
#     return x+y+z

# print(func(1))

def func(s):
    return [i for i in s if i % 2==0]

print(func([1,2,3,4]))