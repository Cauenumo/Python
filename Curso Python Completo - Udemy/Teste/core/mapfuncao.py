#MAP

# def fahrenheit(T):
#     return (9/5) * T + 32

temp = [9,22,40,90,120]

# for t in temp:
#     print(fahrenheit(t))

# print(list(map(fahrenheit, temp)))

# print(list(map(lambda t:(9/5)*t+32,temp)))

#FILTER
pares = [1,2,3,4,8,10,11,15,16,28,24,20]

# print(list(filter(lambda x: x%2 == 0, pares)))

#ZIP

x = [1,2,3,4,87,65,84,87,96,258]
y = [4,5,6,256,245,635,85,96,256,485]

a = [1,2,3,5,5,2]
b = [2,3,25,2]
c = [2,4,2,5]
# print(list(zip(a,b,c)))

# for i in zip(x,y):
#     print(max(i))

#enumerate

lista = ['a','b','c','d']

# for number, item in enumerate(lista):
#     # print(number, ':', item)

teste = ('How long are the words in this phrase')

# quebrado = word_lengths.split()

# print(len(quebrado.split()))

def word_lengths(phrase):
    return list(map(len, phrase.split()))

print(word_lengths(teste))