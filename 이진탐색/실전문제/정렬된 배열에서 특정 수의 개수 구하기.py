## 책풀이 이진 트리로 구현

# Q. 왜 첫번째 인덱스와 마지막 인덱스의 차이로 게산을 하는거지? 
# 그냥 한개의 이진 탐색 함수로 target을 구하면 되는거아닌가? 


n , x = map(int,input().split())
array = list(map(int,input().split()))

def count_by_value (array,x):
    n = len(array)
    a = first(array,x,0,n -1)
    if a == None :
        return 0
    b = last(array,x,0,n-1)
    print('ab',a,b)
    return b - a + 1

def first(array,target,start,end):
    if start > end :
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid -1]) and array[mid] == target :
        return mid
    elif array[mid] >= target:
        return first(array,target,start,mid -1)
    else :
        return first(array,target,mid + 1, end)
    

def last(array, target, start, end):
    if start > end :
        return None
    mid = (start + end )// 2
    #해당 값중 가장 오른쪽에서만 
    if (mid == n - 1 or target < array[mid + 1] and array[mid] == target) :
        return mid
    elif array[mid] > target:
        return last(array,target,start,mid -1)
    else :
        return last(array,target,mid + 1, end)
    

count = count_by_value(array, x)

if count == 0 :
    print(-1)
else :
    print(count)

## bisect 활용하여 문제 해결 
# from bisect import bisect_left, bisect_right

# def count_by_range(array, left_value, right_value) :
#     right_index = bisect_right(array,right_value)
#     left_index = bisect_left(array,left_value)
#     return right_index - left_index

# n,x = map(int,input().split())
# array = list(map(int,input().split()))

# count = count_by_range(array,x, x)

# if count == 0 :
#     print(-1)
# else:
#     print(count)