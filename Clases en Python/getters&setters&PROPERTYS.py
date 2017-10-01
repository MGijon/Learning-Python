import math

class Circulo(object):

	def __init__(self, radio):
		self.radio = radio
		self.area = math.pi * 2 * radio

circulo_1 = Circulo(1)
print("Círculo de radio: " + str(circulo_1.radio))
print("tiene área " + str(circulo_1.area))

# si ahora cambiamos el radio el área no variará !!!!

circulo_1.radio = 2
print("Círculo de radio: " + str(circulo_1.radio))
print("tiene área " + str(circulo_1.area))

''' SOLUCIONES:

	- Podríamos convertir el área en una funcion 'area()' que lea el atributo 'radio'.
	  PROBLEMA: hemos pasado de leer un atributo a hacerlo con un método.
	
	OBS: y si le asignaramos un radio negativo?

	- Podemos construir un 'set_radio' que nos lance un error si intentamos asignarle un valor negativo.

'''

class Circulo_2(object):
	def __init__(self, radio):
		self._radio = radio 		# lo definino como variable privada para "obligarme" a llamar al siguiente método...

	def set_radio(self, radio):
		if radio < 0:
			raise ValueError('el radio debe ser un número no negativo')
		else:
			self._radio = radio 

circulo_2 = Circulo_2(2)
print("Círculo de radio: " + str(circulo_1.radio))
print("tiene área " + str(circulo_1.area))

#circulo_2.set_radio(-3)				# lanza el error como se espera

'''

	Estos métodos son conocidos como SETTERS y GETTERS (o también MUTADORES): métodos usados para controlar el acceso y los
	cambios en una variable.

	EN PYTHON PODEMOS IMPLEMENTAR ESTA FUNCIONALIDAD EXPONIENDO ESTOS MÉTODOS COMO ATRIBUTOS!!
	------------------------------------------------------------------------------------------
	(las funciones que controlan el acceso se ejecutarán entre vastidores)

'''

class CajaFuerte(object):

	def __init__(self, PIN):
		self.PIN = PIN

	@property													# @property convierte PIN en un getter para el atributo de solo lectura con ese mismo nombre !!!!
	def PIN(self):						
		print('Enviando copia a la NSA')
		return self._PIN

	@PIN.setter 
	def PIN(self, PIN):
		if len(str(PIN)) != 4:
			raise ValueError('PIN has to have 4 digits')
		self._PIN = PIN

hucha = CajaFuerte(7814)
print(hucha.PIN)
#hucha.PIN = 342							# raises and error as expected



class Circulo_3(object):
	def __init__(self, radio):
		self.radio = radio

	@property
	def radio(self):
		return self._radio 

	@radio.setter
	def radio(self, radio):
		if radio < 0:
			raise ValueError('Radio must be grater or equal to 0')
		else:
			self._radio = radio

c = Circulo_3(10)
print(c.radio)

#c.radio = -112								# raise the erro, as expected
