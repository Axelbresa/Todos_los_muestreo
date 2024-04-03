import json
import random

poblacion=json.load(open("edades.json"))

# print("poblacion", poblacion)

edades=[]
muestra_aleatoria=[]

for individuo in poblacion:
    edades.append(individuo["age"])
# print("promedio de edades", sum(edades)/len(edades))

edades_auxiliar=edades.copy()

for _ in range(0, 21):
    indice_random=random.randint(0, len(edades_auxiliar)-1)
    valor=edades_auxiliar.pop(indice_random)
    muestra_aleatoria.append(valor)
print("promedio de la muestra aleatoria: ", sum(muestra_aleatoria)/len(muestra_aleatoria))
