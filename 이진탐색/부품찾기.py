# 동빈이네 전자 매장에는 부품이 Nro 
# 손님이 M개 종류의 부품을 대량 구매 원함
# 가게 안에 부품이 모두 있는지 확인 프로그램 

# 입력 
# 첫째 줄에 정수 1부터 100만
# 둘째 공백으로 정수 N 모두 백만 
# 셋째 정수 1부터 10만
# 넷째 공백 M의 정수 모두 백만 

# 출력 공북 구분하여 yes or no

# 1초에 연산 2000만번 충분히 가능 
# 대량의 데이터 검색이라 이진 탐색 


# 내 풀이

import sys
N = int(input())
n_list = list(map(int,sys.stdin.readline().rstrip().split()))
n_list.sort()
print(n_list)
M = int(input())
m_list = list(map(int,sys.stdin.readline().rstrip().split()))



def binary_search (array,target,start,end):
    if start > end :
        return None
    mid = (start + end) // 2
    if array[mid] == target :
        return target
    elif array[mid] > target :
        return binary_search(array,target,start,mid -1)
    else :
        return binary_search(array,target,mid+1 , end) 

for target in m_list :
    arr = binary_search(n_list, target,0, N-1)

    if arr == None :
        print("no", end=' ')
    else :
        print('yes', end=' ')

# 놓친 부분 
# 정렬을 하지 않고 이진 탐색을 진행했는데 잘못된것. 


# 책풀이 
# 이진 탐색 이외에도 계수 정렬 개념을 활용해서 풀 수도 있다. 

# n = int(input())
# array = [0] * 1000001

# for i in input().split() :
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x : 
#     if array[i] == 1 :
#         print("yes", end=' ')
#     else :
#         print('no', end=' ')

# print(array)







