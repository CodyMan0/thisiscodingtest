n = int(input())
array = [input().split() for _ in range(n)]

new_array = sorted(array, key=lambda x:x[1])


for x in new_array : 
    print(x[0], end = " ")