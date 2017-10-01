# la función super nos devuelve un objeto proxy qye delega llamadas a una superclase

class ListaLogger(list):
	def append(self, x):
		print("Intentando añadir x")
		# self.append() # no funciona, entramos en un bucle
		# super(ListaLogger, self).append(x)  # esta era la sintaxis en python 2, en python 3 es más sencilla
		super().append(x)

numeros = ListaLogger()
numeros.append('?')
print(numeros)

def separador():
	print("===========================================")

separador()

class Punto(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circulo(Punto):
	"""heredera de Punto"""
	def __init__(self, x, y, r):
		#super(Circulo, self).__init__(x, y)   # esta era la sintaxis en python 2, en python 3 es más sencilla
		super().__init__(x, y)
		self.r = r
		
c = Circulo(3, 4, 5.5)
print("x: ", c.x)
print("y: ", c.y)
print("radio: ", c.r)

separador()

print("herencia múltiple".upper())

separador()

class Humano(object):
	def ataca(self):
		print('Puñetazo')
class Cyborg(Humano):
	def ataca(self):
		print('Láser')
class Ninja(Humano):
	def ataca(self):
		print('Suriken')

# Ahora la clase con hererncia múltiple:

class Terminator(Cyborg, Ninja):
	def ataca(self, h):
		for h in range(h):
			super().ataca()

robot = Terminator()
robot.ataca(10)# Ataca con láser!!

print('nos lanza lo que nos lanzaría la su clase tía, no va hasta la abuela,\n esto es porque el concepto de superclase no tiene sentido al hablar\n de herencia múltiple.')

print('PODEMOS USAR A VOLUNTAD ESTO, se hereda dependiendo de el orden en el que situemos la herencia\n entre los hermanos de la generación anterior')

print('EN CONCLUSIÓN: usamos super para llamar a métodos definios en alguna de las clases de las que heredamos !!!!')

