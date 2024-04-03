import json
import random

poblacion=json.load(open("edades.json"))

edades=[]
muestra=[]

for individuo in poblacion:
    edades.append(individuo["age"])

edades_auxiliar=edades.copy()

acc=0
cant_muestra=20

k=round(len(edades)/ cant_muestra)
i=random.randint(1, k)

muestra_sistematica=[]
muestra_sistematica.append(edades[i])

for j in range(1, 21):
    acc=i+(j*k)

    if acc <= len(edades)-1:
        muestra_sistematica.append(edades[acc])
    else:
        muestra_sistematica.append(edades[acc - len(edades)])

print("muesta sistematica", muestra_sistematica)
print ("promedio de la muesta sistematica", sum(muestra_sistematica)/len(muestra_sistematica))

