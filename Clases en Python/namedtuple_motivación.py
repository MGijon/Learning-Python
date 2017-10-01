# en ocasiones necesitamos definir unq clase únicamente para almacenar valores...

class Punto_1(object):
	''' Punto (x, y, z) en un espacio tridimensional '''

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

p_1 = Punto_1(1, 2, 3)

print(p_1.x)

'''Aunque no hayamos hecho nada con __init__ lo hemos tenido que definir.
   Como no tenemos ni __str__ ni __repr__ no podemos imprimir siquiere
   el objeto por pantalla de la forma que esperaríamos.
'''

print(p_1)					# <__main__.Punto_1 object at 0x10932d2e8>

'''Tampoco podemos comparar dos puntos sin definir __eq__, ya que sin él
   Python comparará posiciones de memoria.
'''

p_2 = Punto_1(2132,1312, 132)

print(p_1 == p_2)			# False, están evidentemente en posiciones de memoria diferentes

# para ver QUE CMPARA POSICIONES DE MEMORIA EN LUGAR DE LOS PUNTOS, haremos que estos sean iguales...

p_3 = Punto_1(1, 2, 3) 		# = p_1

print(p_1 == p_3)			# False !!!!!!!!!!!!!!!!!!!!!!!!!


class Punto_2(object):
	''' Punto (x, y, z) en un espacio tridimensional '''

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		args = (type(self).__name__, self.x, self.y, self.z)
		return '{0}({1}. {2}, {3})'.format(*args)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

print(p_1 == p_2)			# False

p_3 = Punto_1(1, 2, 3) 		# = p_1

print(p_1 == p_3)			# Debería ser True... pero no sé por qué no...


''' en ualquie caso hemos tenido que utilizar muchos métodos mágicos para esto, con namedtuples no lo ahorraremos '''