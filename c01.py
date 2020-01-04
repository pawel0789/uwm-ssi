import statistics

plik1 = open("hepatitis-filled.txt", "r")
plik2 = open("hepatitis-filled-type.txt", "r")
decyzja1 = {}
decyzja2 = {}
def unique(attribute, _list):
    _uniqueList = []
    for element in _list:
        if element not in _uniqueList:
            _uniqueList.append(element)

    print("Liczba unikalnych wartości atrybutu {}: {}".format(attribute, len(_uniqueList)))
    print("Unikalne wartości atrybutu {}".format(attribute))
    # for element in _uniqueList:
    print(_uniqueList)


for x in plik2:
    line = x
    line = line.strip()
    line = line.split(" ")
    decyzja2[line[0]] = line[1]

indexesOfNumbers = []
i = 0
for key in decyzja2:
    if decyzja2[key] == "n":
        indexesOfNumbers.append(i)
    i += 1

for x in plik1:
    line = x
    line = line.strip()
    line = line.split(" ")

    lineCopy = []
    n = 0
    for item in line:
        if n in indexesOfNumbers:
            lineCopy.append(float(item))
        else:
            lineCopy.append(item)
        n += 1
    line = lineCopy

    if line[-1] in decyzja1:
        decyzja1[line[-1]] = decyzja1.get(line[-1]) + [line]
    else:
        decyzja1[line[-1]] = [line]

print("---------")
print("Istniejące klasy decycyzyjne + liczba elementów w klasie: ")
print("---------")

for key in decyzja1:
    print("{}, liczba elementów: {}".format(key, len(decyzja1[key])))

print("---------")
print("Max i min:")
print("---------#")

for indexesOfNumber in indexesOfNumbers:
    listOfAttributes = []
    listOfAttributesByKey = {}

    for key in decyzja1:
        listByKeys = []
        for value in decyzja1[key]:
            listOfAttributes.append(value[indexesOfNumber])
            listByKeys.append(value[indexesOfNumber])
        listOfAttributesByKey[key] = listByKeys

    print("---------#")
    print("{} Max: {}; Min {}".format("a{}".format(str(indexesOfNumber + 1)), max(listOfAttributes),
                                      min(listOfAttributes)))
    unique("a{}".format(indexesOfNumber+1), listOfAttributes)
    print("Odchylenie standardowe atrybutu {}, wynosi: {}".format(indexesOfNumber+1, statistics.stdev(listOfAttributes)))
    print("---------")
    for key in listOfAttributesByKey:
        print("Odchylenie standardowe atrybutu {} w klasie decyzyjnej {}, wynosi: {}".format(indexesOfNumber+1, key, statistics.stdev(listOfAttributesByKey[key])))

print("---------")
