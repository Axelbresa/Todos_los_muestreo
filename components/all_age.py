import json

def all_edades():
    poblacion=json.load(open("components/edades.json"))
    edades=[]


    for individuo in poblacion:
        edades.append(individuo["age"])
    # print("edades: ", edades)
    # print("promedio de edades", sum(edades)/len(edades))s
    # print("cantidad: ", len(edades))
    return edades.copy()

# all_edades()

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
    # print("software: ", software)
    # print("edades: ", edades)
    # print("promedio de edades", sum(edades)/len(edades))s
    # print("cantidad: ", len(edades))
    return edades.copy()

# all_edades_carrera()