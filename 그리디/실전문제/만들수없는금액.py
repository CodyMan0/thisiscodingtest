#1회
## 동전의 개수 정수 N이 주어진다 (1이상 1000이하)

n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1
print('data',data)
for x in data :
    ## 화폐로 만들지 못하는 금액을 의미 
    if target < x : 
        break
    target += x
    print('target',target)

print(target)



## 아이디어 
# 1. 정렬은 체크 

# 현재 확인하는 동전의 단위가 target 이하인지가 핵심. 

# 화폐 단위가 작은 동전부터 하나씩 확인하면서 target 변수를 업데이트하는
# 방법으로 최적의 해를 계산할 수 있다. 