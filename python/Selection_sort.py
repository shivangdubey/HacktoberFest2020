def selection_Sort(array, a):
   
    for i in range(a):
        x = i

        for j in range(i + 1, a):

            if array[j] < array[x]:
                x = j
         
        (array[i], array[x]) = (array[x], array[i])


data = [-3, 5, 0, 13, -4,-1,23]
a = len(data)
selection_Sort(data, a)
print('Sorted Array in Ascending Order:')
print(data)