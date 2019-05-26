import os 
import subprocess
from Topologia import *
br=[]
ovs=[]
veth=[]
ns=[1]
def buscar_bridge(lista, nombre)
    for i in lista:
        if i.nombre ==nombre
            return i
def sub (cadena):
    obj=subprocess.run([cadena],stdout=subprocess.PIPE, shell=True)
    return obj

def Exit():
    print("Bye Bye")
    return True
def CreacionSwitches():
    Topologia()
    return True 

def AgregarNs():
    opcion=input("Indique el nombre de switch a agregar el NS:")
    nbridge=int(opcion)
    if not ns
        #Crear el NS
        nsp=NameSpace("ns_1")
        extr_a="veth%s_%s" %(nsp.nombre,opcion); extr_b="veth%s_%s" %(opcion,nsp.nombre)
        Interface().crea_veth(extr_a,extr_b)
        br=buscar_bridge(opcion,bridge)
        br.add_interface(extr_b)
        ns.add_interface(extr_a)
    else:
        #se le suma 1 al ultimo valor y lo agrego al final de la lista
        ultimo=ns[len(ns)
        nsp=NameSpace("ns_%s" %(ultimo+1))
        extr_a="veth%s_%s" %(nsp.nombre,opcion); extr_b="veth%s_%s" %(opcion,nsp.nombre)
        Interface().crea_veth(extr_a,extr_b)
        br=buscar_bridge(opcion,bridge)
        br.add_interface(extr_b)
        ns.add_interface(extr_a)
        #Crear NS, crear enlace veth, añadir interfaz veth al bridge, interfaz veth al ns  
        """
        sub("sudo ip netns add ns_%s" %ultimo
        sub("sudo ip link add ns%s_%s type veth peer name br%s_%s" %(ultimo,nbridge,nbridge,ultimo))
        sub("sudo brctl addif br_%s br%s_%s" %(nbridge,nbridge,ultimo))
        sub("ip link set ns%s_%s netns ns_%s" %(ultimo,nbridge,ultimo))
        """


def NuevoSw():
    nuevo=input("Ingresar el switch a conectar")
    switch=input
    if

        
MENU = {1:CreacionSwitches,7:Exit}	

while 1:
    print("What would you like to do?\n [1] Hostname\n [2] Date and time\n [3] CPU usage\n [4] Available RAM\n [5] Number TX packets\n [6] Number RX packets\n [7] Exit")
    opt = input("Enter an option: ")
    #try:

    opt = int(opt)
    ex = MENU[opt]()
    if ex:
        break


