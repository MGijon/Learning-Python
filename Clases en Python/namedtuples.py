import collections

Punto = collections.namedtuple('Punto', 'x y z')

p = Punto(3, 1, 5)

print('x: ' + str(p.x))
print('y: ' + str(p.y))
print('z; ' + str(p.z))

p2 = Punto(3, 1, 5)

print(p2)				# Punto(x=3, y=1, z=5)

print(p == p2)			# True


'''
	Lo que namedtuple(), una FACTORY FUNCION, nos devuelve,
	es una nueva clasa que hereda de typle pero que también 
	nos permite el acceso a los atributos por nombre.

	Nada más y nada menos, pero al ser una subclase significa que 
	todos los métodos mágicos que necesitamos ya están 
	implementados.
'''

# Otro ejemplo...

Punto2 = collections.namedtuple('Punto2', 'x y z')

P = Punto2(5, 4, 4)

print('x: ' + str(P.x))
print('y: ' + str(P[1]))
print('z; ' + str(P[-1]))

print('Tamaño: ' + str(len(P)))		# Tamaño: 3


'''
	Namedtuple(): recibe dos argumentos:
		- Nombre de la clase
		- Atributos de la misma
			- Secuencia de cadenas de texto
			- Única cadena de texto con los atributos separados por comas o espacios
			ej: son equivalentes
			Punto = namedtuple('Punto', ['x', 'y', 'z'])
			Punto = namedtuple('Punto', 'x y z')
			Punto = namedtuple('Punto', 'x, y, z')

			Si usamos palabras reservadas de Python como nombre de los atributos levantaremos un 'ValueError
'''