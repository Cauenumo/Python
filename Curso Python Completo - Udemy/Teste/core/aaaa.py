#  def primeira_funcao():
#     """
#     printa "olá, mundo"
#     """
#     print('Olá mundo')

# primeira_funcao()

# def somar(num1, num2):
#     print(num1+num2)

# somar(1,2)

# def primo(num):
#     def divisivel(a,b):
#         return a %b
#     for n in range(2, num):
#         if divisivel(num, n) == 0:
#             print('Não é primo')
#             break 
#     else:
#         print('primo')

# primo(87)
    
# def gensquares(N):
#     for x in range(N):
#        print(x ** 2)
# print(gensquares(10))


# def verifica(n):
#     if n in lista:
#         print('na lista')
#     else:
#         print('fora da lista')


# lista =[1,2,3,4,5,6] 
# print(verifica(7))

# def vol(rad):
#     volume = (4/3) * 3.14 * (rad*3)
#     return volume

# print(vol(10))

# def ran_check(num, low, high):
#     if num in list(range(low,high + 1 )):
#         return True
#     else:
#         return False 
# print(ran_check(11,1,10))

# def up_low(s):
#     up = 0
#     low = 0

#     for x in s:
#         if x.isupper():
#             up +=1
#         elif x.islower:
#             low +=1
#         else:
#             continue
    
#     print('Número de caracteres maiúsculos: {}'.format(up))
#     print('Número de caracteres minúsculos: {}'.format(low))

# s = 'CauÊ Nunes MoreiRa'

# print(up_low(s))

# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total

# l = [1,2,3,4,5]
# print(multiply(l))

# def palindrome(s):
#     return s == s[::-1]

# frase = 'subi no on ibus'
# print(palindrome(frase))

