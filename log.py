import subprocess, os

destino = "prueba@64.233.190.102:/tmp/"

archivo = open("session.log", "r")
lineas = archivo.readlines()

nuevo_archivo = open("session_last_100.log", "a")

for i in lineas[-100:]:
    nuevo_archivo.write(i)

subprocess.run(["scp", nuevo_archivo, destino])