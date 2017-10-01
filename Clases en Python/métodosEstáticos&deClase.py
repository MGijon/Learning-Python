''' MÉTODO ESTÁTICO: aquellos que no necesitan acceso a ningún atributo
    ----------------

    - En estos casos el elemento 'self' se vuelve innecesario.
    - Usamos el decorador @staticmethod para evitar que lo reciba.
    - La pertenencia de los métodos a estas clases es cuestión de lógica, no de necesidad.

'''

class Calculadora(object):

	def __init__ (self, nombre):
		self.nombre = nombre

	def nombre(self):
		return self.nombre

	'''
	def suma(self, x, y):      		# Es un método estático, no necisita acceder a ningún atributo de la clase, RECORDEMOS:	
		return x + y				# OTROS MÉTODOS TAMBIÉN SERÍAN ATRIBUTOS DE LA CLASE
	'''

	@staticmethod
	def suma(x, y):
		return x + y


cal = Calculadora('Suma')
print(cal.nombre)				
print(cal.suma(3, 5))

''' MÉTODO DE CLASE: se puede pensar en ellos como en una variante de los métodos ordinarios. Sí reciben un primer argumento, pero la
	----------------- 		diferencia no es el objeto al que llaman ('self'), sino a la clase de dicho objeto (por  convención 'cls').

	- Si necesitamos devolver otro objeto de la misma clase, necesitaremos una referencia a dicha clase.
	- Si quisiésemos RENOMBRAR la clase tendríamos un porblema: tener que renombrarla en todos los puntos donde la hemos llamado.
	- Utilizaremos el decorador @classmethod y 'cls' para arreglarlo.
		OBS: si necesitamos un acceso a un atributo del objeto ya no podremos usarlo, necesitaremos 'self' indefectiblemente.

'''

class Ameba(object):

	def __init__(self, nombre):
		self.nombre = nombre

	'''
	def fision(self):

		h1 = Ameba('Primogénito')	# ¿y si renombraramos la clase?... aquí tendríamos porblemas...
		h2 = Ameba('Benjamín')
		return h1, h2
	'''

	@classmethod
	def fision(cls):
		h1 = cls('Primogénito')
		h2 = cls('Benjamín')
		return h1, h2




ameba = Ameba('Papuchi')
hijo1, hijo2 = ameba.fision()

print(hijo1.nombre)
print(hijo2.nombre)

print(type(ameba))

class Ameba2(object):

	def __init__(self, nombre):
		self.nombre = nombre

	def fision(self):
		cls = type(self)		# Así obtenemos la clase si @classmethod
		ascendencia = 'Hijo de ' + self.nombre
		h1 = cls('Primogénito ' + ascendencia)
		h2 = cls('Benjamín ' + ascendencia)
		return h1, h2


ameba2 = Ameba2('Papuchi')

print(type(ameba2))
hijo3, hijo4 = ameba2.fision()

print(hijo3.nombre)
print(hijo4.nombre)



















