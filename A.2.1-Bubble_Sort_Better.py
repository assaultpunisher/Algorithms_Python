def bubbleSort(list):
    for a in range(len(list)-1,0,-1):
        for i in range(a):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [14,46,43,27,57,41,45,21,70]
bubbleSort(list)
print ("Sorted list is:")
print(list)