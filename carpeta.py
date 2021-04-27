import shutil, os, time, datetime



rango = datetime.datetime.now() - datetime.timedelta(30)
rangoE = rango.timestamp()

carpeta = "grupo"
carpetaDestino = "grupo2"
if not os.path.exists(carpetaDestino):
    os.mkdir(os.path.join(os.path.abspath(os.getcwd()), carpetaDestino))

for filename in os.listdir(carpeta):
    f = os.path.join(carpeta, filename)
    if os.path.isfile(f):
        x = os.path.getctime(f)
        if x > rangoE:
            shutil.copy(f, carpetaDestino)