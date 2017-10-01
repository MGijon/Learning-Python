''' __REPR()__: Nos devuelve una cadena de texto con la representación única de un objeto. Es útil, por ejemplo, a la hora de depurar un error.
    ------------

    A la representación única accedemos de dos formas: con la función repr() o con las dobles comillas hacia atrás (``).

    Si __repr()__ no está definido, Python en lugar de darnos un error nos generará una representación automática del objeto, 
    indicando el nombre de su clase y su posición en la memoria.
'''

class Triangulo(object):

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def __str__(self):
		clase = type(self).__name__
		mensaje = '{0} con base {1} y altura {2}.'.format(clase, self.base, self.altura)
		return mensaje

t = Triangulo(12, 124)

print(t)
print('en este caso no hemos definido __repr()__, Python lo generará automáticamente...')
print(repr(t))

import math

class Circulo(object):

	def __init__(self, radio):
		self.radio = radio

	@property
	def area(self):
		return 2 * math.pi * self.radio

	def __str__(self):
		clase = type(self).__name__
		mensaje = '{0} de radio {1} y área {2}'.format(clase, self.radio, self.area)
		return mensaje

	def __repr__(self):
		clase = type(self).__name__	
		mensaje = '{0}({1})'.format(clase, self.radio)
		return mensaje

c = Circulo(131)

print(c)								# Circulo de radio 131 y área 823.0972752405258

print(repr(c))							# Circulo(131)

print(eval(repr(c)))					# Circulo de radio 131 y área 823.0972752405258



#####################  MORALEJA ###########################################################
#                      ---------                                                          #
#                                                                                         #
#			__str__ : PARA USUARIOS                                                       # 
#           __repr–– : PARA DESARROLLADORES                                               #
#                                                                                         #
###########################################################################################
