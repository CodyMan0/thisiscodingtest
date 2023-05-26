# 문제
## 해당 값이 자신의 인덱스와 같을때 그것을 동일한 원소라고 한다.
## 모든 원소는 오름차순 정렬


# 입력
## N 1~ 1000000
## N 요소 

# 출력
## 고정점을 출력한다. 없으면 -1

#  아이디어
## target을 받는게 아니라 
## 함수 내부에서 mid와 target이 아닌 arr[mid]와 mid를 비교한다
## 그래서 arr[mid]가 크면 왼편으로 작으면 오른편으로 재귀적으로 호출한다. 


def binary_search (array,start,end):
    if start > end :
        return None
    mid = (start + end ) // 2
    if array[mid] == mid :
    ## 원래는 arr[mid] == target인데 이렇게 한줄 바꿨네
      return mid
    elif array[mid] > mid :
        return binary_search(array, start, mid - 1)
    else :
        return binary_search(array, mid + 1, end)


n = int(input())
array = list(map(int,input().split()))

index = binary_search(array, 0 , n-1)

if index == None :
    print(-1)
else :
    print(index)

