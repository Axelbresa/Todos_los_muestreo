import json
import random
from components.all_age import all_edades_carrera

poblacion=json.load(open("components/edades.json"))

edades=all_edades_carrera()

cant_muestra=11
muestreo_conglomerados=[]

edades_copia = edades.copy()

muestreo_conglomerados = [] 

while len(muestreo_conglomerados) < cant_muestra:
    indice_random = random.randint(0, len(edades_copia) - 1)
    valor_random = edades_copia[indice_random]
    muestreo_conglomerados.append(valor_random)
    # Eliminar el valor de la lista copiada para evitar repeticiones
    edades_copia.pop(indice_random)

print("Muestra de conglomerados :", muestreo_conglomerados)
print("Promedio de edades de la muestra de conglomerados :", int(sum(muestreo_conglomerados) / cant_muestra))
