alternatives = []
goal = input("Jaki masz cel?")
alternatives_count = int(input("Ile masz alternatyw? "))

for i in range(alternatives_count):
    tmp = input("Podaj alternatywe nr " + str(i + 1))
    alternatives.append(tmp)
alternatives_matrix = [float(x) for x in input('Podaj macierz porównań alternatyw: ').split()]

criteriums = []
criterium_count = int(input("Ile masz kryteriow? "))

for i in range(criterium_count):
    name = input("Podaj kryterium nr " + str(i + 1))
    criteriums.append(name)
    sub_count = int(input("Podaj liczbę subkryteriów: "))
    if sub_count:

    for j in range(sub_count):



if criterium_count:
    criterium_matrix = [float(x) for x in input('Podaj macierz porównań alternatyw wg kryteriów: ').split()]



