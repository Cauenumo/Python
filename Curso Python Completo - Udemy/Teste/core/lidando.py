# try:
#     file = open('testfile', 'w')
#     file.write('testando')
# except IOError:
#     print('Erro ao tratar o arquivo.')
# else:
#     print('Não houve erro')

# try:
#     f = open('testfile', 'w')
#     f.wirte('testando')
# except:
#     print('')
# finally:
#     print('rodou')

# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except:
#     print('Não é possivel multiplicar letra')


# try:
#     x = 5
#     y = 0

#     z = x/y
# except:
#     print('')
# finally:
#     print('All done!')


def ask():
    
    while True:
        try: 
            num = int(input('Insira um número inteiro: '))
            print('Obrigado, seu níumero ao quadrado é: {}'.format(num**2))
            break
        except:
            print('Carctere inválido, insira um número.')
            continue

print(ask())
