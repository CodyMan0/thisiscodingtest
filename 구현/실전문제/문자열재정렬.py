# n = input()

# a = []
# b = []

# for i in n : 
#     if ord(i) > 64 : 
#         a.append(i)
#     else : 
#         b.append(int(i))
# a.sort()
# b = str(sum(b))

# result = [*a , b]
# result1 = ''.join(result)

# print(result1)


# 책풀이 

# data = input()
# result = []
# value = 0

# for x in data :
#     if x.isalpha() :
#         result.append(x)
#     else :
#         value += int(x)

# result.sort()

# if value != 0 :
#     result.append(str(value))

# print(''.join(result))

## isalpha라는 매소드가 있네? 나는 아스키코드로 확인
## 굳이 정수일때 배열에 넣고 sum을 할 필요가 없네
## 그냥 더하면 됐네? 


# 책 풀이를 반영하여 수정한 코드 

n = input()

result = []
value = 0

for i in n : 
    if i.isalpha() : 
        result.append(i)
    else : 
        value += int(i)

result.sort()

if value != 0 :
    result.append(str(value))


print(''.join(result))