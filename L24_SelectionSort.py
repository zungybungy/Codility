#Selection sort:
def selectionSort(list):
    for slot in range(len(list)-1,0,-1):
        pmax=0
        for poz in range(1,slot+1):
            if list[poz] > list[pmax]:
                pmax = poz
        temp = list[slot]
        list[slot] = list[pmax]
        list[pmax] = temp
    return list

alist = [54,26,93,17,77,31,44,55,20]
print(selectionSort(alist))