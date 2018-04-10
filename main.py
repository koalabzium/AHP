import json
from pprint import pprint

data = json.load(open('agusi.json'))

for i in data["alternatives"]:
    print(i)


#ZCZYTYWANIE

dict = {}

def get_alternatives():
    alternatives = []
    goal = input("Jaki masz cel?")
    alternatives_count = int(input("Ile masz alternatyw? "))

    for i in range(alternatives_count):
        tmp = input("Podaj alternatywe nr " + str(i + 1))
        alternatives.append(tmp)
    return alternatives

alternatives = get_alternatives()

cryt_count = int(input("Ile jest kryteriów?"))

def get_cryterium(slownik, cryt_count):
    cryt=[]
    for j in range(cryt_count):
        cryt.append(input("Podaj nazwę kryterium nr" + str(j + 1)))
    if cryt_count>1:
        slownik["matrix"] = make_matrix(cryt)

    for i in range(cryt_count):
        cryt_name = cryt[i]
        flaga = int(input("Ile kryterium " + cryt[i] + " ma podkryteriów?"))
        if flaga:
            slownik[cryt_name] = {}
            nowy_slownik = slownik[cryt_name]
            get_cryterium(nowy_slownik, flaga)
        else:
            slownik[cryt_name] = make_matrix2(alternatives, cryt_name)
    return 0

def make_matrix2(alternatives, cryt_name):
    matrix = []
    for i in range(len(alternatives)):
        for j in range(len(alternatives)):
            if i==j:
                matrix.append(1)
            elif i<j:
                matrix.append(float(input("Ile razy wg kryterium " + cryt_name + " alternatywa " + alternatives[i] + " jest lepsza od alternatywy " + alternatives[j])))
            else:
                matrix.append(1/matrix[((i+1)*(j+1))-1])


    return [float(x) for x in matrix]

def make_matrix(cryt):
    matrix = []
    for i in range(len(cryt)):
        for j in range(len(cryt)):
            if i==j:
                matrix.append(1)
            elif i<j:
                matrix.append(float(input("Ile razy kryterium " + cryt[i] + " jest wazniejsze od kryterium " + cryt[j])))
            else:
                matrix.append(1/matrix[((i+1)*(j+1))-1])
    return [float(x) for x in matrix]


dict['Alternatives'] = alternatives
dict['goal'] = {}
get_cryterium(dict['goal'], cryt_count)

with open('result.json', 'w') as fp:
    json.dump(dict, fp, indent=4)
