import json
import math
import random

# Todas las edades del ipf

def all_edades():
    poblacion=json.load(open("components/edades.json"))
    edades=[]


    for individuo in poblacion:
        edades.append(individuo["age"])
    return edades.copy()

# all_edades()

# Todas las edades de la carrera de software
def all_edades_carrera():
    poblacion=json.load(open("components/edades.json"))
    edades=[]
    software=[]


    for individuo in poblacion:
        carreras=individuo["careers"]
        # print("carreras: ", carreras)
        if "SOFTWARE" in carreras:
            edad=individuo["age"]
            software.append(carreras)  
            edades.append(edad)
    return edades.copy()

# all_edades_carrera()

#Agregar los valores al muestreo strintificado 

def addMuestraStrintificado(edades, cant_muestra, adultez_etapa):
    muestra_strintificado=[]
    muestra_temprana = int(len(adultez_etapa) / len(edades) * 100)
    muestra_temprana=math.ceil((muestra_temprana/100)*cant_muestra)
    print("cantidad de la muestra temprana: ", muestra_temprana)

    for i in range(muestra_temprana):
        ramdom=random.randint(0, len(adultez_etapa)-1)
        valor_muestra = adultez_etapa[ramdom]
        muestra_strintificado.append(valor_muestra)
    return muestra_strintificado        

# addMuestraStrintificado(edades, cant_muestra, adultez_etapa)