# def func():
#     return 1 

# print(func())

# # s = 'Globla variable'

# def func2():
#     print(locals())

# print(func2())

def hello(nome='Cauê'):
    print('Olá,'+nome)

    def tudobem():
        print('Tudo bem?')

    def comovoceesta():
        print('Como voce está?')
    
    print(locals())

print(hello())