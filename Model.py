from functions import sub 
class Bridge: 
	nombre=""
	tipo=""
	interfaces=[]
	def crea_bridge(self,tipo):
		if tipo=="lb":
			sub("sudo brctl addbr %s" %self.nombre).stdout
		elif tipo=="ovs":
			sub("sudo ovs-vsctl addbr %s" %self.nombre).stdout

	def __init__(self, nombre,tipo)
		self.nombre=nombre
		self.tipo=tipo
		self.crea_bridge(self.tipo)
	def __str__(self):
		return self.nombre

class Interface():
