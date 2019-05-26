from Model import *
from funtions import *
def Topologia():
    topologia=input("Ingrese el tipo de topologia,lineal(L) anillo(A) :")
    num_switches=input("Ingrese el numero de switches(3-8)")
    opcionlb_ovs=input("Desea utilizar linux bridge(lb) o ovs(ovs)?")
    #Ejecutar funcion en Bash
    #Cambio a entero para poder realizar operaciones con este 
    nswitches=int(num_switches)
    # Configuracion si los switche es linux bridges
    if(opcion=="lb"):
        #Creacion de enlaces veth
        for i in range(1,nswitches):
            ext_a="veth%s_%s" %(i,i+1);ext_b="veth%s_%s" %(i+1,i)
            interface().crea_veth(ext_a,ext_b)
        #Creacion de switches
        for i in range(1,nswitches+1):
            br=Bridge("br_%s" %i,"lb")
            br.append(br)
            #Asignar interfaz a l linux bridges 
    	    if(i==1):
                br.add_interface("veth1_%s" %(i+1))
            elif(i==nswitches):
                br.add_interface("veth%s_%s" %(nswitches,nswitches-1))
            else:
                br.add_interface("veth%s_%s" %(i.i-1))
                br.add_interface("veth%s_%s" %(i.i+1))
        #Si es topologia en anillo se crea un enlace veth y se adigna las interfaces al primer y ultimo sbridge
        if(topologia=="A"):
            sub("sudo ip link add -veth1_%s type veth peer name veth%s_1" %(nswitches,nswitches)).stdout
            sub("sudo brctl addif br_1 veth1_%s" %(nswitches)).stdout
            sub("sudo brctl addif br_%s veth%s_1" %(nswitches,nswitches)).stdout

    elif(opcion=="ovs"):
        for i in range(1,nswitches+1):
            ovs=Bridge("ovs_%s" %i,"ovs")
            if(i==1):
                ovs.add_interface("patch1_2","patch2_1")
                if topologia=="A"
                    ovs.add_interface("patch1_%s" %nswitches,"patch%s_1" %nswitches)
            elif(i=nswitches):
                ovs.add_interface("patch%s_%s" %(nswitches,nswitches-1), "patch%s_%s" %(nswitches-1,nswitches))
                if topologia=="A"
                    ovs.add_interface("patch%s_1" %nswitches,"patch1_%s" %nswitches)
            else:
                ovs.add_interface("patch%s_%s" %(i,i-1),"patch%s_%s" %(i-1,i))
                ovs.add_interface("patch%s_%s" %(i,i+1),"patch%s_%s" %(i+1,i))
            
    return False