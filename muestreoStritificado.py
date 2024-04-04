import json
import math
import random
from components.all_age import all_edades

poblacion=json.load(open("components/edades.json"))

edades=all_edades()

# La adultez temprana (18-40 años de edad)
# La adultez media (40-60 años de edad)
# La adultez tardía (desde los 60 años en adelante)

muestra_strintificado=[]
adultez_temprana=[]
adultez_media=[]
adultez_tardia=[]

print(len(edades))

cant_muestra=20

for i in edades:
    if i>18 and i<40:
        adultez_temprana.append(i)
    if i>=40 and i<60:
        adultez_media.append(i)
    if i>=60:
        adultez_tardia.append(i)
    
muestra_temprana = int(len(adultez_temprana) / len(edades) * 100)
muestra_temprana=math.ceil((muestra_temprana/100)*cant_muestra)
print("cantidad de la muestra temprana: ", muestra_temprana)

for i in range(muestra_temprana):
    ramdom=random.randint(0, len(adultez_temprana)-1)
    valor_muestra = adultez_temprana[ramdom]
    muestra_strintificado.append(valor_muestra)

muestra_media = int(len(adultez_media) / len(edades) * 100)
# el metodo math.ceil lo use para redondear el numero(ejemplo 7.80 lo pasa a 8)
muestra_media=math.ceil((muestra_media/100)*cant_muestra)
print("cantidad de la muestra media: ", muestra_media)

for i in range(muestra_media):
    ramdom=random.randint(0, len(adultez_media)-1)
    valor_muestra = adultez_media[ramdom]
    muestra_strintificado.append(valor_muestra)

muestra_tardia = int(len(adultez_tardia) / len(edades) * 100)
muestra_tardia=math.ceil(muestra_tardia/100*cant_muestra)
print("cantidad de la muestra tardia: ", muestra_tardia)

for i in range(muestra_tardia):
    ramdom=random.randint(0, len(adultez_tardia)-1)
    valor_muestra = adultez_tardia[ramdom]
    muestra_strintificado.append(valor_muestra)

print("adultez temprana: ",adultez_temprana)
print("adultez media: ",adultez_media)
print("adultez tardia: ",adultez_tardia)
print("muestra strintificado: ", muestra_strintificado)
print("promedio de la muestra strintificado: ", int(sum(muestra_strintificado)/cant_muestra))
