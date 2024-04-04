import json
import random
from components.all_age import all_edades

poblacion=json.load(open("components/edades.json"))

edades=all_edades()

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

print("muesta sistematica: ", muestra_sistematica)
print ("promedio de la muesta sistematica", sum(muestra_sistematica)/len(muestra_sistematica))

