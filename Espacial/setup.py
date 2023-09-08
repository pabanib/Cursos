#setup
#Instala las dependencias


import subprocess

# Lista de bibliotecas a instalar
libraries_to_install = [
    "folium",
    "mapclassify",
    "geodatasets",
    "pysal",
]

# Itera a través de la lista e instala cada biblioteca
for library in libraries_to_install:
    try:
        subprocess.check_call(["pip", "install", library])
        print(f"La biblioteca {library} se ha instalado correctamente.")
    except subprocess.CalledProcessError:
        print(f"Error al instalar la biblioteca {library}.")

print("Todas las bibliotecas se han instalado o se han intentado instalar.")
