# 문제
# 두개의 배열 A,B N개의 원소로 구성
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것 

# N,K 그리고 배열 A,B의 정보가 주어졌을때 , 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 
# 배열 A의 모든 원소의 합의 최대값을 출력하는 프로그램 만들기


# 입력
# 첫번째 N ,K 공백으로 구분된다 (n은 1이상 10만 이하 , k는 0이상 n 이하)
# 두번째 A 공백으로 구분 배열
# 세번째 B 공백으로 구분 배열

# 출력
# 최대 K번 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 최댓값

# 아이디어 
# 배열 A를 K번 순회하면서 이중포문으로 배열 B를 순회하여 가장 큰값을 A의 i와 변경하면 될 것 같다. 
# A는 오름 차순으로 
# B는 내림 차순으로 하면 더 쉬울 것 같다 

n , k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k) :
    if a[i] < b[i] :
        a[i] , b[i] = b[i], a[i]
    else :
        break
print(sum(a))

