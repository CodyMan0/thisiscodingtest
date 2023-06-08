# 문제 그룹 단어를 찾아라

## 1. 그룹 단어가 아니려면 해당 이중 포문을 예로 들면
## i와 j가 동일한 값인데 인덱스가 2이상 차이나면 안됨? 




# 아이디어 
##

# 입력

# n = int(input())
# cnt = n

# for _ in range(n):
#     word = input()
#     for i in range(0, len(word)-1) :
#         if word[i] == word[i+1] :
#             pass
#         elif word[i] in word[i+1 :] :
#             cnt -= 1
#             break


# print(cnt)

a = 0
for i in range(int(input())):
    s = input()
    a+= list(s) == sorted(s, key=s.find)
    print(sorted(s, key=s.find))
print(a)




        
