import json
import math

data = json.load(open('agusi.json'))
print(type(data["alternatives"]))
def decode_alternatives():
    alternatives=[]
    for i in data["alternatives"]:
        alternatives.append(i)
    return alternatives

alternatives=decode_alternatives()

def decode_reszte(data) :
    matrix = []
    lista=[]
    for i in data:
        #print(type(i))
        if type(data[i]) == dict:
            decode_reszte(data[i])
        lista.append(data[i])
    data.clear()

    print(lista)






    return 0

decode_reszte(data["obiad"])

