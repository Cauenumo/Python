# x = 1


# while x <= 20:
#     print('O valor de x é:', x)
#     x += 1

# n = 1
# l = []

# while True:
#     l += [n]
#     n += 1
#     if n > 10:
#         break
# print(l)     

ate = 10 
n = 0

while n < ate:
    n += 1
    if n % 2 == 1:
        continue
    if n % 2 == 0:
        print(n, 'é par')