from Model import *
def Topologia():
    topologia=input("Ingrese el tipo de topologia,lineal(L) anillo(A) :")
    num_switches=input("Ingrese el numero de switches(3-8)")
    opcionlb_ovs=input("Desea utilizar linux bridge(lb) o ovs(ovs)?")
    #Ejecutar funcion en Bash
    #Cambio a entero para poder realizar operaciones con este 
    nswitches=int(num_switches)
    # Configuracion si los switche es linux bridges
    if(opcion=="lb"):
        #Creacion de switches
    	for i in range(1,nswitches+1):
        	br.append(Bridge("br_%s" %i,"lb"))
        #Creacion de enlaces veth
    	for i in range(1,nswitches):
            ext_a="veth%s_%s" %(i,i+1);ext_b="veth%s_%s" %(i+1,i)
            interface().crea_veth(ext_a,ext_b)
        #Asignar interfaz a l linux bridges 
    	for i in range(1,nswitches+1):
            #Añade interefaz con vecino de la izquiera(cadena1) derecha(cadena2)
            cadena1="sudo brctl addif br_%s veth%s_%s" %(i,i,i-1)
            cadena2="sudo brctl addif br_%s veth%s_%s" %(i,i,i+1)
            #Validacion del primero, ultimo e intermedios 
            if(i==1):
            	sub(cadena2).stdout
            elif(i==nswitches):
            	sub(cadena1).stdout
            else:
            	sub(cadena1).stdout
                sub(cadena2).stdout
        #Si es topologia en anillo se crea un enlace veth y se adigna las interfaces al primer y ultimo sbridge
        if(topologia=="A"):
            sub("sudo ip link add veth1_%s type veth peer name veth%s_1" %(nswitches,nswitches)).stdout
            sub("sudo brctl addif br_1 veth1_%s" %(nswitches))
            sub("sudo brctl addif br_%s veth%s_1" %(nswitches,nswitches))

    elif(opcion=="ovs"):
        for i in range(1,nswitches+1):
            cadena="sudo ovs-vsctl add-br ovs_%s" %i
            if(i==1):
                cadena_port="sudo ovs-vsctl add-port ovs_%s patch%s_%s" $(i,i,i+1)
                cadena_patch="ovs-vsctl set interface patch%s_%s type=patch" %(i,i+1)
                cadena_peer="ovs-vsctl set interface patch%s_%s options:peer=patch%s_%s" %(i,i+1,i+1,i)

                sub(cadena).stdout
                ovs.append("ovs_%s" %i)
            elif(i=nswitches):
                cadena_port="sudo ovs-vsctl add-port ovs_%s patch%s_%s" $(i,i,i-1)
                cadena_patch="ovs-vsctl set interface patch%s_%s type=patch" %(i,i-1)
                cadena_peer="ovs-vsctl set interface patch%s_%s options:peer=patch%s_%s" %(i,i-1,i-1,i)
                ovs.append("ovs_%s" %i)

            else:
                cadena_port_r="sudo ovs-vsctl add-port ovs_%s patch%s_%s" $(i,i,i+1)
                cadena_patch_r="ovs-vsctl set interface patch%s_%s type=patch" %(i,i+1)
                cadena_peer_r="ovs-vsctl set interface patch%s_%s options:peer=patch%s_%s" %(i,i+1,i+1,i)

                cadena_port_l="sudo ovs-vsctl add-port ovs_%s patch%s_%s" $(i,i,i-1)
                cadena_patch_l="ovs-vsctl set interface patch%s_%s type=patch" %(i,i-1)
                cadena_peer_l="ovs-vsctl set interface patch%s_%s options:peer=patch%s_%s" %(i,i-1,i-1,i)

                sub(cadena_port_r).stdout
                sub(cadena_patch_r).stdout
                sub(cadena_peer_r).stdout
                sub(cadena_port_l).stdout
                sub(cadena_patch_l).stdout
                sub(cadena_peer_l).stdout

                sub(cadena).stdout
                ovs.append("ovs_%s" %i)
        if(topologia=="A"):
            sub("sudo ovs-vsctl ")
            
    return False