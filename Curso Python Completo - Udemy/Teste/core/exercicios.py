# st = 'Print only the words that start with s in this sentence'
# split_string = st.split()
# for l in split_string:
#     if l[0] == 's':
#         print(l)
    
# for a in range(0,10,1):
#     if a %2 == 0:
#         print(a)

# lista = list(range(1,50,1))
# for x in lista:
#     if x %3 == 1:
#         continue
#     if x %3 == 0:
#         print(x, 'é divisivel por 3')

# st = 'Print every word in this sentence that has an even number of letters'
# split_st = st.split()
# for l in split_st:
#     tam = len(l)
#     if tam %2 == 0:
#         print(l, 'é par')
#     else:
#         print('É impar')

# lista2 = list(range(1,101,1))
# for x in lista2:
#     if x %3 == 0:
#         print(x,'fizz')
#     elif x %5 == 0:
#         print(x,'Buzz')
#     elif x %3 == 0 and x %5 == 0:
#         print(x,'FizzBuzz')

st = 'Create a list of the first letters of every word in this string'
split_st = st.split()
lista_vazia = []
for x in split_st:
    x[0] += lista_vazia
    
print(lista_vazia)