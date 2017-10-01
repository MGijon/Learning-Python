''' Usaremos RENAME = TRUE para que los identificadores vñalidos se renombres automáticamente (también eliminará los repetidos), 
	sustituyéndolos por identificadores posicionales.

	Muy útil para generar namedtuple's a partir de BASES DE DATOS -> MACHINE LEARNING for instance.
'''

from collections import namedtuple

Hucha = namedtuple('Hucha', '__PIN color for 1', rename = True)		# por culpa de 'for' sin rename tendríamos un ValueError

print(Hucha._fields) 							# _fields como atributo protegido de la clase TUPLE !!!!
												# ('_0', 'color', '_2', '_3')
