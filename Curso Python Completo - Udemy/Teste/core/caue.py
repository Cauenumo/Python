def modulo(x):
    if ( x < 0):
        x = -x
    return x

# print(modulo(5))

# n = -5
# print(modulo(n))
# print(-5)

# def adiciona(lista):
#     lista.append(9)

# l = [] 
# adiciona(l)
# print(l)

# def maior(x, p):
#     if x > p:
#         print('{} é maior do que {}'.format(x,p))
#     else:
#         print('{} é maior do que {}'.format(p,x))

# print(maior(25,58))

def maiors(a,b,c):
    if a > b and a > c:
        print('{} é maior que {} e {}'.format(a,b,c))
    elif b > a and b > c:
        print('{} é maior que {} e {}'.format(b,a,c))
    else:
        print('{} é maior que {} e {}'.format(c,b,a))

print(maiors(5,2,13))