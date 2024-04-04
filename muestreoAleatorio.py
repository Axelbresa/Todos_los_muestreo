import json
import random
from components.all_age import all_edades

poblacion=json.load(open("components/edades.json"))

edades=all_edades()

muestra_aleatoria=[]

for _ in range(0, 21):
    indice_random=random.randint(0, len(edades)-1)
    valor=edades.pop(indice_random)
    muestra_aleatoria.append(valor)

print("muesta aleatoria: ", muestra_aleatoria)
print("promedio de la muestra aleatoria: ", sum(muestra_aleatoria)/len(muestra_aleatoria))
