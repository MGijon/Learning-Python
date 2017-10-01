# Clases en Python: Lo estas haciendo mal - Victor Terrón (en youtube)

class Perro1:
	# NO HEREDA DE OBJECT
	def __init__(self, nombre, raza, edad):
		self.nombre = nombre
		self.raza = raza
		self.edad = edad

sargento1 = Perro1("Stubby", "Bull-terrier", 9)

print ("Tipo: ", type(sargento1))				# Tipo:  <class '__main__.Perro1'>

# para que nuestra clase sea new-style debemos hacer que herede de Object

class Perro2(object):
	# HEREDA DE OBJECT
	def __init__(self, nombre, raza, edad):
		self.nombre = nombre
		self.raza = raza
		self.edad = edad

sargento2 = Perro2("Stubby", "Bull-terrier", 9)

print("Tipo: ", type(sargento2))


# heredar de object desde python 3 no es necesrio explícitamente, pero es conveniente, ya que todos los abojetos son new-style
