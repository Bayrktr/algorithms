def collect_all_the_names(parameter1):
    listcopy1 = parameter1.copy()
    string_list = []
    a = 0
    flag = 0
    while flag < len(listcopy1):
        firstname = listcopy1[a]
        if firstname not in string_list:
            string_list.append(firstname)
            a += 1
        else:
            a += 1
            flag -= 1
        flag += 1
        if a == len(string_list):
            break
    return string_list


def collect_all_the_index(parameter1):
    string_list = collect_all_the_names(parameter1)
    listcopy1 = parameter1.copy()
    index_list = []
    for x in string_list:
        listcopy = listcopy1.copy()
        listem = []
        b = 0
        foodName = x
        number = listcopy.count(foodName)
        for x in range(number):
            index = listcopy.index(foodName)
            listem.append(index + b)
            listcopy.pop(index)
            b += 1
        index_list.append(listem)
    return index_list


def collect_all_numbers(parameter1, parameter2):
    def collect_for_list():
        all_numbers = []
        for x in collect_all_the_index(parameter1):
            liste = []
            for y in x:
                liste.append(parameter2[y])
            all_numbers.append(liste)
        return all_numbers

    def collection():
        a = 0
        liste = []
        for x in collect_for_list():
            a = 0
            for y in x:
                a = a + int(y)
            liste.append(a)
        return liste

    return collection()


def list_arrangement(parameter1, parameter2):
    names = collect_all_the_names(parameter1)
    numbers = collect_all_numbers(parameter1, parameter2)
    numbersTwo = numbers.copy()
    newNames = []
    newNumbers = []
    for x in range(len(names)):
        bigNumber = max(numbers)
        index = numbersTwo.index(bigNumber)
        newNames.append(names[index])
        newNumbers.append(bigNumber)
        numbers.remove(bigNumber)
    return newNames, newNumbers
