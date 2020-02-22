# class Circle(object):
#     pi = 3.14

#     # O círculo é instanciado com um raio (o padrão é 1)
#     def __init__(self, radius=1):
#         self.radius = radius 

#     # Método de cálculo da área. Observe o uso de si mesmo.
#     def area(self):
#         return self.radius * self.radius * Circle.pi

#     # Método que redefine a área
#     def setRadius(self, radius):
#         self.radius = radius

#     # Método para obter raio (Mesmo que apenas chamar .radius)
#     def getRadius(self):
#         return self.radius

# c = Circle()

# c.setRadius(3)
# print('O raio é: ',c.getRadius())
# print('A área é: ', c.area())

# l = [1,2,3]


# t = (1,2,3)
# print(type(t))

# def funcao(a,b):
#     somei = a + b
#     return somei 
# print(funcao(1,2))
# print(type(funcao))

# class Dog(object):
#     def __init__(self,raça):
#         self.raça = raça

# sam = Dog(raça='Labrador')

# frank = Dog(raça = 'Pitbull')
# print(frank.raça)

# class Dog(object):
#     species = 'mamifero'
#     def __init__(self,raça):
#         self.raça = raça
#         print(len(self.species))

#     def latir(self):
#         print("au au")

# sam = Dog(raça = 'Labrador')

# print(sam.latir())

# class Circulo(object):
#     pi = 3.14

#     def __init__(self, raio = 1):
#         self.raio = raio 
    
#     def area(self):
#         return self.raio ** 2 * self.pi
    
#     def att(self, raio):
#         self.raio = raio 
    
#     def obtemraio(self):
#         return self.raio

# c = Circulo()
# print(c.att(52))

# class Animal(object):
#     def __init__(self):
#         print('Animal criado.')

#     def quemsou(self):
#         print('Eu sou um animal')
    
#     def comer(self):
#         print('Comendo...')

# class Cachorro(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print('Cachorro criado.')
    
#     def quemsou(self):
#         print('Sou um cachorro.')
    
#     def latir(self):
#         print('Au AU')
    
# sam = Cachorro()

# print(sam.quemsou())
# print(sam.latir())

# class book():
#     def __init__(self,titulo,autor,paginas):
#         print('um livro foi criado.')
#         self.titulo = titulo 
#         self.autor = autor 
#         self.paginas = paginas

#     def __str__(self):
#         return "Titulo {}".format(self.titulo)

#     def __len__(self):
#         return self.paginas

#     def __del__(self):
#         print('livro destruido')


# l = [1,2,3]

# livro1 = book ('Python', 'Cauê', 100)

# class Line(object):

#     def __init__(Self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
    
#     def distance(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coor2 
#         return ( (x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
    
#     def slope(self):
#         x1,y1 = self.coor1
#         x2,y2 = self.coo2 
#         return float((y2-y1))/(x2-x1)

# coor
