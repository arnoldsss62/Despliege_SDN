import os 
import subprocess
from Topologia import *
br=[]
ovs=[]
veth=[]
ns=[1]
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
    if(ns[len(ns)-1]==1):
        sub("sudo ip netns add ns_%s" %ns[0])
        sub("sudo ip link add ns%s_%s type veth peer name br%s_%s" %(ns[0],nbridge,nbridge,ns[0]))
        sub("sudo brctl addif br_%s br%s_%s" %(nbridge,nbridge,1))
        sub("ip link set ns1_%s netns ns_1" %(nbridge))
    else:
        #se le suma 1 al ultimo valor y lo agrego al final de la lista
        ns.append(ns[len(ns)ns[len(ns)-1]+1)
        ultimo=ns[len(ns)
        #Crear NS, crear enlace veth, añadir interfaz veth al bridge, interfaz veth al ns  
        sub("sudo ip netns add ns_%s" %ultimo
        sub("sudo ip link add ns%s_%s type veth peer name br%s_%s" %(ultimo,nbridge,nbridge,ultimo))
        sub("sudo brctl addif br_%s br%s_%s" %(nbridge,nbridge,ultimo))
        sub("ip link set ns%s_%s netns ns_%s" %(ultimo,nbridge,ultimo))

def NuevoSw():
    opcion=input("Ingresar el switch a cnectar")
    tipo=input("El switch a agregar es LB(L) o OVS(O)")
    if opcion in br and tipo==L:
        sub("sudo brctl addbr br_%s")
        sub("sudo ip link add  type veth peer name %s" %(opcion)).stdout
        

MENU = {1:CreacionSwitches,7:Exit}	

while 1:
    print("What would you like to do?\n [1] Hostname\n [2] Date and time\n [3] CPU usage\n [4] Available RAM\n [5] Number TX packets\n [6] Number RX packets\n [7] Exit")
    opt = input("Enter an option: ")
    #try:

    opt = int(opt)
    ex = MENU[opt]()
    if ex:
        break
        
    #except KeyError:
    #    print("Invalid option!\n")
    #except ValueError:
    #    print("Option must be an integer!\n")
    #except:
    #    print("An error occurred!\n")



