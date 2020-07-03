def InsertionSort(list):
    for i in range(1, len(list)):
        current_element = list[i]
        pos = i
        while current_element < list[pos-1] and pos>0:
            list[pos] = list[pos-1]
            pos = pos-1
        list[pos] = current_element

list = [50,30,10,80,60,20]
InsertionSort(list)
print(list)
