# 특정 조건 
# 캐릭터의 점수 N이라고 할때 자릿수를 기준으로 점수 N을 반으로 나누어
# 왼쪽부분 자릿수 합 오른쪽 합을 더한 것이 동일한 상황을 의미 

# n = input()
# mid_length = len(n) // 2
# left = list(map(int, n[:mid_length]))
# right = left = list(map(int, n[mid_length:]))

# print("LUCKY" if left == right else "READY")

## 나는 왼쪽 오른쪽 짤라서 배열에 담은 후, 확인

# 책풀이
n = input()
length = len(n)
summary = 0

for i in range(length // 2) :
    summary += int(n[i])

for i in range(length // 2, length) :
    summary -= int(n[i])

if summary == 0 :
    print("LUCKY")
else :
    print("READY")