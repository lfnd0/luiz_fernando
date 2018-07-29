num = int(input())
array_final = []

array = input()
array = array.split(' ')
array = list(map(int, array))

for i in range(len(array)-1, -1, -1):
    array_final.append(array[i])

array_final = str(array_final).strip('[]').replace(',', '')
print(array_final)

troca_final = len(array)
array.insert(troca_final, array[0])
del(array[0])
array_final = str(array).strip('[]').replace(',', '')
print(array_final)

array.sort(reverse=True)
array_final = str(array).strip('[]').replace(',', '')
print(array_final)
