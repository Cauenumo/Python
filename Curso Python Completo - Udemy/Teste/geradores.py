'''def gencubes(n):
    for num in range(n):
        yield num ** 3

for x in gencubes(10):
    print(x)'''

'''def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b
        
for num in genfib(10):
    print(num)'''

def gensquares(n):
    for x in range(n):
        yield x ** 2

for x in gensquares(10):
    print(x)
