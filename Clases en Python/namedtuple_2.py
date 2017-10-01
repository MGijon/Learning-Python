''' Typename: el primer argumento de namedtuple es el nombre que tendrá la clase, 
	--------- independientemente del nombre que le asignemos en nuestro código.
'''

import collections 

cls = collections.namedtuple('Punto', 'x y z')
print(cls)												# <class '__main__.Punto'>
print('Nombre de la clase: ' + cls.__name__)			# Nombre de la clase: Punto

p = cls(4, 3, 2)
print(p)												# Punto(x=4, y=3, z=2)

''' CLASES HEREDADAS: AÑADIRLES FUNCINOALIDADES
    -----------------
'''

import math

PUNTO = collections.namedtuple('PUNTO', 'x y z')

class Point(PUNTO):

	def distancia(self, other):
		''' Distancia entre dos puntos '''
		x_axis = (self.x - other.x) ** 2
		y_axis = (self.y - other.y) ** 2
		z_axis = (self.z - other.z) ** 2

		return math.sqrt(x_axis + y_axis + z_axis)

p1 = Point(3, 1, 2)
p2 = Point(42, 142, 41)

print(p1)												# Point(x=3, y=1, z=2)
print(p2)												# Point(x=42, y=142, z=41)

print('Distancia entre los puntos: ' + str(p1.distancia(p2)))  # Distancia entre los puntos: 151.4034345713465
