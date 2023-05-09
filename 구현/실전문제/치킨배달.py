# 내풀이
# n(도시 크기)은 2부터 50 m(치킨집 개수) 은 1부터 13개까지
# n개의 줄에는 도시의 정보 ()
# n , m = map(int, input().split())
# city = [list(map(int,input().split())) for _ in range(n)]
  
# city_list = []
# chicken_list = []

# for i in range(1, n + 1) : 
#     for j in range(1, n + 1) :
#         if city[i-1][j-1] == 1 :
#             city_list.append((i-1,j-1))
#         elif city[i-1][j-1] == 2:
#             chicken_list.append((i-1,j-1))

# def chicken_distance(cities,stores,m) :
#     each_chicken_distance = []
    
#     for i in cities : 
#         min_distance = []
#         for j in stores:
#           a = abs(i[0] - j[0]) + abs(i[1] - j[1])
#           print('ij',i,j)
#           print(a)
#           min_distance.append(a)
#         each_chicken_distance.append(min(min_distance))
#     each_chicken_distance.sort()
#     return each_chicken_distance

# print(chicken_distance(city_list,chicken_list,3))

# 최소 거리를 기준으로 m개의 치킨집을 고려해야하는데 그 m개의 치킨집을 고르고
# 동일한 로직을 반복해야하나? 
# 폐업 시키지 않을 치킨집을 어떻게 고르지?
# 내 시도는 각 완전 탐색으로 집과 치킨집을 찾고 서로 다른 배열에 append해준다
# 그리고 함수안에서 두 배열을 인자로 받고 완전 탐색으로 집을 i 치킨집을 j로
# 순회하며 치킨거리가 가장 낮은 거리를 min_distance에 append해줬고
# 오름차순 정렬을 활용했다. 여기까지


# 책 풀이
# 시간 초과 범위를 계산하여 조합을 사용할 수 있다고 판단.
# 치킨 집 (최대 13개) 중 m개를 고르는 조합을 파이썬 라이브러리 Combinations

from itertools import combinations
n,m = map(int,input().split())
chicken, house = [], []
# 내 풀이와 동일한 변수 선언

for r in range(n) :
    data = list(map(int,input().split()))
    for c in range(n) :
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

# 여기가 다르다
# 조합 복습 요망! 
candidates = list(combinations(chicken,m))


# 함수명 get으로 짓자!
def get_sum (candidate) :
    result =0
    for hx,hy in house :
        # 이런식으로 무한대로 변수를 지정하고 밑에서 min함수를 사용할 수 있구나 
        temp = 1e9
        for cx,cy in candidate :
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
        result +=temp
    return result

result = 1e9
for candidate in candidates :
    result = min(result,get_sum(candidate))
print(result)

## 코드 이해 완료, 내 코드로 정리해보기!