import os 
import subprocess
from Topologia import Topologia,AgregarNs
from Model import *
br=[]
ovs=[]
veth=[]
ns=[]
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
def hola():
    return True

def Agregar_IP():
    modo=input("Modo manual(m) o automatico(a)")
    delta=10
    if modo=="a":
        for i in ns:
        ip_final=sub("python generateipv4.py 10.0.0.0 %s" ).stdout
        i.asignar_ip(ip_final)
        delta+=1
    elif modo=="m":
        for i in ns:
            ip_final=input("Ingrese la ip para el la namespace %s" %i.nombre)
            i.asignar_ip(ip_final)
    return True 

def Mostrar_IP():
    for i in ns:
        print("La ip del ns: %s es %s/24" %(i.nombre,i.mostrar_ip())
    return True 

def NuevoSw():

    nuevo=input("Ingresar el switch a nuevo")
    switch=input("Ingresar el nombre del switch a conectar ")
    br=buscar_bridge(br,switch)
    ovs=buscar_bridge(ovs,switch)
    if br:
        br_nuevo=Bridge(nuevo,"lb")
        extr_a="veth%s_%s" %(nuevo,switch); extr_b="veth%s_%s" %(switch,nuevo)
        br_nuevo.add_interface(extr_a)
        br.add_interface(extr_b)
    elif ovs:
        ovs_nuevo=Bridge(nuevo,"ovs")
        extr_a="patch%s_%s" %(nuevo,switch); extr_b="patch%s_%s" %(switch,nuevo)
        ovs_nuevo.add_interface(extr_a,extr_b)
        ovs.add_interface(extr_b,extr_a)
    return True 
        
MENU = {1:CreacionSwitches,2:AgregarNs,3:NuevoSw,4:Agregar_IP,5:Mostrar_IP,6:Conectividad,7:Exit}	

while 1:
    print("What would you like to do?\n [1]Creacion de Topologia\n [2] Agregar NameSpace\n [3] Agregar nuevo SW a topologia\n [4] Asignar Ips a host (NS)\n [5] Mostrar ips de host\n [6] Prueba de Conectividad \n [7] Exit")
    opt = input("Enter an option: ")
    #try:

    opt = int(opt)
    ex = MENU[opt]()
    if ex:
        break


