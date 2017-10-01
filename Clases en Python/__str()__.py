class Triangulo(object):

	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	@property
	def area(self):
		return (self.base * self.altura) / 2.0

t = Triangulo(2, 3)

print(t)								# <__main__.Triangulo object at 0x10a1fd208>

print("Área: " + str(t.area))			# Observemos que área es un atrubuto, no un método...

print('\'_\'')

''' La función __str__() debe devolver la cadena de texto que se muestra por pantalla si llamamos a la función str(). 
	Esto es lo que hace Python cuando usamos 'print'.
'''

class Triangulo2(object):

	def __init__(yo, base, altura):
		yo.base = base
		yo.altura = altura

	@property
	def area(self):
		return (self.base * self.altura) / 2.0

	def __str__(self):
		mensaje = 'Triángulo de base {0} y altura {1}'.format(self.base, self.altura)
		return mensaje

t2 = Triangulo2(10,21)

print(str(t2))

print('Área: ' + str(t2.area))



#####################  MORALEJA ###########################################################
#                      ---------                                                          #
#                                                                                         #
#			__str__ : PARA USUARIOS                                                       # 
#           __repr–– : PARA DESARROLLADORES                                               #
#                                                                                         #
###########################################################################################