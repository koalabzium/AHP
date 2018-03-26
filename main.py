import json


#ZCZYTYWANIE

dict = {}
alternatives = []
goal = input("Jaki masz cel?")
alternatives_count = int(input("Ile masz alternatyw? "))

for i in range(alternatives_count):
    tmp = input("Podaj alternatywe nr " + str(i + 1))
    alternatives.append(tmp)

criterium_count = int(input("Ile masz kryteriow? "))
dict_crit = {}
if criterium_count:
    alternatives_matrix = [float(x) for x in input('Podaj macierz porównań alternatyw wg tych kryteriów: ').split()]
else:
    alternatives_matrix = [float(x) for x in input('Podaj macierz porównań alternatyw: ').split()]
    #alternatives_matrix = input('Podaj: ')




for i in range(criterium_count):
    name = input("Podaj kryterium nr " + str(i + 1))
    sub_count = int(input("Podaj ilość subkryteriów: "))
    if sub_count:
        cr_matrix = [float(x) for x in input('Podaj macierz porównań podkryteriów kryterium "' + name + '": ').split()]
        dict_sub = {}
        dict_sub["matrix"] = cr_matrix
        for i in range(sub_count):
            sub_name = input("Podaj nazwę podkryterium " + str(i + 1) + ": ")
            sub_matrix = [float(x) for x in input('Podaj macierz porównań wg podkryterium "' + sub_name + '": ').split()]
            dict_sub[sub_name] = sub_matrix
        dict_crit[name] = dict_sub

    else:
        cr_matrix = [float(x) for x in input('Podaj macierz porównań alternatyw na podstawie kryterium "' + name + '": ').split()]
        dict_crit['matrix'] = alternatives_matrix
        dict_crit[name] = cr_matrix
    subs = []



dict['Alternatives'] = alternatives
if criterium_count:
    dict[goal] = dict_crit
else:
    dict[goal] = alternatives_matrix



#do jsona


with open('result.json', 'w') as fp:
    json.dump(dict, fp, indent=4)
