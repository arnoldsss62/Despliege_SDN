import subprocess

def sub (cadena):
    obj=subprocess.run([cadena],stdout=subprocess.PIPE, shell=True)
    return obj

