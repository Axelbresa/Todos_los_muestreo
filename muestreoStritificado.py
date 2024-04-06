import json
from components.all_age import all_edades, addMuestraStrintificado

poblacion=json.load(open("components/edades.json"))

edades=all_edades()


muestra_strintificado=[]
#subgrupos
adultez_temprana=[]
# La adultez temprana (18-40 años de edad)
adultez_media=[]
# La adultez media (40-60 años de edad)
adultez_tardia=[]
# La adultez tardía (desde los 60 años en adelante)

print(len(edades))

cant_muestra=20

for i in edades:
    if i>18 and i<40:
        adultez_temprana.append(i)
    if i>=40 and i<60:
        adultez_media.append(i)
    if i>=60:
        adultez_tardia.append(i)

muestra_strintificado.extend(addMuestraStrintificado(edades, cant_muestra, adultez_temprana))
muestra_strintificado.extend(addMuestraStrintificado(edades, cant_muestra, adultez_media))
muestra_strintificado.extend(addMuestraStrintificado(edades, cant_muestra, adultez_tardia))

print("adultez temprana: ",adultez_temprana)
print("adultez media: ",adultez_media)
print("adultez tardia: ",adultez_tardia)
print("muestra strintificado: ", muestra_strintificado)
print("promedio de edades de la muestra strintificado: ", int(sum(muestra_strintificado)/cant_muestra))
