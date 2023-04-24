# 절단기 높이 H 기준으로 주어진 떡 짜르기 

# 문제가 이해가 안간다... 

# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램 작성해야한다. 

# 입력 
# 첫번째 떡의 개수 N , 요청한 떡의 길이 M, N은 백만까지 , M은 20억 
# 두번째 떡의 개별 높이 떡 높이의 총합은 항상 M 높이는 10억 

# 출력 
# 적어도 M 만큼의 떡을 가져갈 H의 최댓값 

# 아이디어 
# 적절한 높이를 찾을때까지 절단기의 높이 H를 반복해서 조정 

# 책 풀이 
n , m = list(map(int,input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end) :
    total =0 
    mid = (start + end) // 2
    for x in array : 
        if x > mid :
            total += x - mid
    print('total',total)
    if total < m :
        end = mid - 1
    else :
        result = mid
        start = mid + 1
    print('res',result)

print(result)


# 파라메트릭 서치 유형은 최적화 문제를 결정문제로 바꾸는 방법이라는 것을 이해하고 우선 넘어가자
