# Crear un script bash que guarde en un archivo llamado
# "test2.txt" las líneas del archivo "test1.txt" que contengan
# alguna de las siguientes palabras: "GATO", "PERRO", "LORO"

archivo1 = open("prueba.txt", "r")
archivo2 = open("test.txt", "a")
for linea in archivo1:
    for palabra in linea.split():
        if palabra.lower() == "prueba" or palabra.lower() == "funciona":
            archivo2.write(linea)
    
        #if palabra.lower() == "perro" or palabra.lower() == "gato" or palabra.lower() == "loro":


