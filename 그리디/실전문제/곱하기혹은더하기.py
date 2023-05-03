#1회

## 내풀이

# n = input()

# result = 0
# for i in n :      
#     el = int(i)
#     if result == 0 :
#       result += el
#     else : 
#       result *= el

# print(result)


## 책 풀이 

data = input()

result = int(data[0])

for i in range(1, len(data)) :
    num = int(data[i])

    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num

## 여기서 핵심은 나는 0일 경우에만 더했는데 문제 정답은 1일 경우에도 더했다. 
## 
