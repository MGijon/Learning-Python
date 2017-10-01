import math

'''
	Para no Hard-codear el nombre de la clase, OBTENDREMOS ESTE MEDIANTE EL ATRIBUTO '__NAME__' DE LA CLASE 'TYPE()'
'''

class Circulo(object):	

	def __init__(self, radio):
		self.radio = radio

	@property
	def area(self):
		return math.pi * 2 * self.radio

	def __str__(self):

		clase = type(self).__name__ 		# AQUÍ TENEMOS EL NOMBRE DE LA CLASE
		mensaje = '{0} de radio {1} y área {2}'.format(clase, self.radio, self.area)
		return mensaje

c = Circulo(12)

print(c)



#####################  MORALEJA ###########################################################
#                      ---------                                                          #
#                                                                                         #
#			__str__ : PARA USUARIOS                                                       # 
#           __repr–– : PARA DESARROLLADORES                                               #
#                                                                                         #
###########################################################################################