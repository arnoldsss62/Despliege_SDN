from functions import sub 

class Bridge: 
	nombre=""
	tipo=""
	interfaces=[]
	def crea_bridge(self,tipo):
		if tipo=="lb":
			sub("sudo brctl addbr %s" %self.nombre).stdout
		elif tipo=="ovs":
			sub("sudo ovs-vsctl add-br %s" %self.nombre).stdout
	def add_interface(self,n_interface,n_interface2=""):
		if tipo=="lb":
			sub("sudo brctl addif %s %s" %(self.nombre,n_interface).stdout
			self.interfaces.append(n_interface)
		elif tipo=="ovs":
			sub("sudo ovs-vsctl add-port %s %s" %(self.name,n_interface)).stdout
			sub("ovs-vsctl set interface %s type=patch", %n_interface).stdout
			sub("ovs-vsctl set interface %s options:peer=%s" %(n_interface,n_interface2)).stdout
			self.interfaces.append(n_interface)

	def __init__(self, nombre,tipo):
		self.nombre=nombre
		self.tipo=tipo
		self.crea_bridge(self.tipo)
	def __str__(self):
		return self.nombre
class Interface:
	nombre=""
	tipo=""
	ip=""
	@staticmethod
	def crea_veth(ext_a,ext_b):
		sub("sudo ip link add %s type veth peer name %s" %(ext_a,ext_b)).stdout

	def __init__(self, nombre,tipo):
		self.nombre=nombre
		self.tipo=tipo
	def __str__(self):
		return self.nombre
class NameSpace:
	nombre:
	interfaces=[]
	def crea_ns(self):
		sub("sudo ip netns add %s" %self.nombre)
	def add_interface(self,n_interface)
		sub("ip link set %s netns %s" %(n_interface,self.nombre)).stdout
		self.interfaces.append(n_interface)
	def asignar_ip(self,ip):
		for i in interfaces:
			sub("ip netns %s exec ip addr add %s dev %s" %(self.name, ip, i.nombre)
			i.ip=ip
	def mostrar_ip(self):
		for i in interfaces
			return i.ip

	def __init__(self,nombre)
		self.nombre=nombre
	def __str__(self):
		return self.nombre






