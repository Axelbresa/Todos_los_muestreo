import json

def all_edades():
    poblacion=json.load(open("components/edades.json"))
    edades=[]


    for individuo in poblacion:
        edades.append(individuo["age"])
    # print("promedio de edades", sum(edades)/len(edades))
    return edades.copy()

# all_edades()
