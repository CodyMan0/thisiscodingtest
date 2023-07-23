n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

print(array)

for i in range(1,len(array)):
    for j in range(i, 0, -1) :
        print('df',array[i],array[j],i,j)
        if array[j] < array[j - 1] :
            array[j] , array[j -1] = array[j-1] , array[j]
        else :
            break
print(array)