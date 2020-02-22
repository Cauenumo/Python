t = (12,13,14)
# print(t[0])

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Huskie', name='Sam')

print(sam.age)