class Persona(object):

	def __init__(self, nombre, secreto):
		self.nombre = nombre
		self._secreto = secreto 			# esta es una VARIABLE PRIVADA, aunque como veremos nada nos impide acceder a ellas

persona = Persona('Raquel', 'prefiere Perl')
print(persona.nombre)						# 'Raquel'
print(persona._secreto)						# 'prefiere Perl'

# -----------------------------------------------------------------


''' 
No podemos tener un atributo y un método que se llamen igual, ya que los métodos también son atributos.

Podemos usar variables pivadas para las variables
'''

class Persona2(object):

	def __init__(self, nombre, edad):
		self.nombre = nombre
		self._edad = edad 					# ahora puedo usar el nombre 'edad' para un método sin COLISIONES

	def edad(self):
		print(self._edad)

p = Persona2('Jose', 33)
p.edad()


# -----------------------------------------------------------------


''' VARIABLES OCULTAS: 
	
	se denotan con __ al comienzo del nombre (dos guiones bajos).

	Tomaremos el ejemplo anterior, si '_edad' lo convertimos en '__edad' no será tan fácial acceder en ocasiones
'''

class Persona3(object):
	def __init__(self, edad):
		self.__edad = edad      			 # VARIABLE OCULTA

	def edad(self):
		return(self.__edad)

pp = Persona3(24)
print(pp.edad())							# Ha accedido sin problemas a pesar de estar oculta



# -----------------------------------------------------------------
# -----------------------------------------------------------------



''' Conflicto de Nombres '''

class Habitacion(object):
	_PIN = 9312

class CamaraAcorazada(Habitacion):
	def __init__(self, PIN):
		self._PIN = PIN 

h = CamaraAcorazada(2222)				# SOBREESCRIBE la variable _PIN
print(h._PIN)							# 2222

class Habitacion2(object):
	__PIN = 9312

class CamaraAcorazada2(Habitacion2):
	def __init__(self, PIN):
		self.__PIN = PIN

	'''
	Utilizando __PIN la variable es AUTOMÁTICAMENTE RENOMBRADA COMO _Habitacion2__PIN y _CamaraAcorazada2__PIN respectivamente
	'''
p2 = CamaraAcorazada(2222)

#print(p2._CamaraAcorazada2__PIN)       # debería funcionar, aunque no le da la gana hacerlo, min 25 aprox
#print(p2._Habitacion__PIN)


class CamaraAcorazada3(Habitacion2):
	def __init__(self, PIN):
		self.__PIN = PIN

	def PIN1(self):
		return self._Habitacion2__PIN

	def PIN2(self):
		return self.__PIN


p3 = CamaraAcorazada3(2222)

print(p3.PIN1())
print(p3.PIN2())

