animales = [
    {
        "nombre": "Salmon",
        "tipo": "pez"
    },
    {
        "nombre": "Aguti",
        "tipo": "mamifero"
    },
    {
        "nombre": "Tiburon",
        "tipo": "pez"
    },
   {
        "nombre": "Caiman",
        "tipo": "reptil"
    },
    {
        "nombre": "Salmon",
        "tipo": "pez"
    },
   {
        "nombre": "Serpiente",
        "tipo": "reptil"
    },
    {
        "nombre": "Panda",
        "tipo": "mamifero"
    },
   {
        "nombre": "Tortuga",
        "tipo": "reptil"
    },
    {
        "nombre": "Sardina",
        "tipo": "pez"
    },
    {
        "nombre": "Gorila",
        "tipo": "mamifero"
    },
]

mamiferos = []
for i in animales:
    if i.get("tipo") == "mamifero":
        mamiferos.append(i.get("nombre"))

print(mamiferos)