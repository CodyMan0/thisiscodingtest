array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 가장 큰수 max 함수로 확인 
count = [0] * (max(array) + 1)
print(count)

# array를 순회하면서 동일한 넘버에 1씩 더한다 
for i in range(len(array)) :
    count[array[i]] += 1

# count의 길이 만큼 순회하고 이중포문을 돌면서 카운트된 갯수만큼 순회하면서 정렬시킨다.
for i in range(len(count)) :
    for j in range(count[i]) :
        print(i,end =" ")
