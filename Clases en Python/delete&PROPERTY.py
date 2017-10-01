class CajaFuerte(object):
	def __init__(self, PIN):
		# guardaremos un historial de los PIN's que usemos
		self._PINs = []
		self.PIN = PIN

	@property
	def PIN(self):
		try:
			return self._PINs[-1]		# escogemos el ÚLTIMO ELEMENTO DE LA LISTA
		except IndexError:				# atrapamos el error y lo gestionamos apropiadamente
			return None

	@PIN.setter
	def PIN(self, PIN):
		if len(str(PIN)) != 4:
			raise ValueError('El PIN debe tener exáctamente 4 números')
		self._PINs.append(PIN)			# añadimos a lista el último de los PINs

	@PIN.deleter
	def PIN(self):
		del self._PINs[:]				# borramos todos los elementos de la lista, la dejamos vacía

''' 
	Lo que está ocurriendo es con el decorador @property es que la función SE ESTÁ CONVIERTIENDO EN UN GETTER para un atributo
	de lectura de ese mismo nombre.
	
	Este objeto property nos ofrece a su vez los métodos getter, setter y deleter que podemos usar como decoradores para copiar
	la propiedad y ajustar su correspondiente función de acceso.

	Obs: el docstring (la documentación, para que nos entendamos) de la @property será aquel que especifiquemos para la setter.

'''
import math

class Circulo(object):
	def __init__(self, radio):
		self.radio = radio

	@property
	def area(self):
		''' Devuelve el área del círculo '''
		return math.pi * 2 * self.radio


c = Circulo(3.4)
print('Este círculo tiene un radio de: ')
print(c.radio)
print('y un área de:')
print(c.area)
print('Docstrind de la property, se imprime con Circulo.area.__doc__: (Circulo es la clase!!) ' +  Circulo.area.__doc__)

''' 
	Al usar decoradores tenemos que asegurarnos que todas las funciones tienen el mismo nombre que aquella que hemos decorado como
	Setter, ie. aquella que hemos decorado con el property
'''

# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------

'''
	La idea es siempre adherirnos en lo posible al:

						UNIFORM ACCESS PRINCIPLE:
						-------------------------

	El acceso a todos los atributos lo hacemos a través de una notación uniforme, al margen deque estén implementados 
	como simple almacenamiento (un atribiuto) o una llamada a un método (propiedades).

'''
