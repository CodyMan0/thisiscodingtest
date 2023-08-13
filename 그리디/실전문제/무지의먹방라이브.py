# # 가장 낮은 음식을 먼저 나오고 나머지는 빠진만큼 감소시킨다.
# # 가장 낮은 걸 먼저 나가고 크기만큼 time에 추가
# # k값을 k//len(q)*len만큼 감소시켜

# import heapq

# food_times=[3, 1, 2]
# k=5

# def solution(food_times, k):
#     if sum(food_times)<k:
#       return -1
    
#     q=[]
#     for i in range(len(food_times)):
#       heapq.heappush(q,(food_times[i],i+1))
#     print('q',q)
    
#     length=len(food_times)
#     previous=0
#     sum_value=0

#     while sum_value+((q[0][0]-previous)*length)<=k:
#       now=heapq.heappop(q)[0]
#       sum_value+=(now-previous)*length
#       length-=1
#       previous=now
    
#     result=sorted(q,key=lambda x:x[1])
#     print('result',result)
#     return result[(k-sum_value)%length][1]

# print(solution(food_times,k))


num_strings = int(input("문자열 개수를 입력하세요: "))  # 입력받을 문자열 개수

# 리스트 컴프리헨션을 사용하여 문자열 입력받기
string_array = [input(f"{i+1}. 문자열 입력: ") for i in range(num_strings)]

# 결과 출력
print("입력한 문자열들:", string_array)

