# 큰수 부터 작은 수로 정렬 

# 입력
# 첫 줄에 수열에 속해있는 수 (1 이상 N 500이하)
# 둘째 줄 수 1이상 10만 이하 자연수 

# 출력 
# 내림 차순, 정렬된 결과를 공백으로 구분하여 출력 

n = int(input())
data = [int(input()) for i in range(n)]

array = sorted(data,reverse=True)

for i in array:
    print(i, end=" ")