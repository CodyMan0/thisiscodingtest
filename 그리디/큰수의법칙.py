# 배열의 크기 N , 숫자가 더해지는 횟수 M, K가 주어질때 동빈이의 큰 수 법칙에 따른 결과 출력

n , m , k = map(int, input().split())
arr  = list(map(int,  input().split()))
arr.sort(reverse=True)
first = arr[0]
second = arr[1]

result =0 

while True : 
    for i in range(k) : 
        if m == 0 : 
            break
        result += first
        m -= 1 

    if m == 0 : 
        break
    result += second
    m -= 1

print(result)





# 나의 생각
# 4.17 약 5일간 독감으로 앓다가 정신을 차라기 위해 풀어본 그리디 알고리즘... 유난히 지치고 하기 싫은 날이다.
# 7.18 혼자 하다 2/3 지점에서 문제풀이를 그만 두어 스터디를 통해 다시 시작했다. 파이팅 해보자
