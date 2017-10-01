class T1000(object):
	JEFE = "Skynet" 		# Variable de clase, compartida por todos los objetos de la clase

	def saluda_uno(self):
		print(self.JEFE, 'se envía a eliminarte')

	def saluda_dos(selg):
		print(T1000.JEFE, 'se envía a eliminarte')  
	
robot = T1000()
robot.saluda_uno()
robot.saluda_dos()

''' Ambos funcionan, sin embargo es más comun utilizar 'SELF' '''	
