# 순열
from itertools import permutations
data = ['a', 'b', 'c']
result = list(permutations(data,3))


#조합
from itertools import combinations
data1 = ['A', 'B','C']
result = list(combinations(data1,2))



# 힙정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))

       
    return result

answer = heapsort([1,3,5,7,8,2,10,0])



# 이진 탐색 bisect
from bisect import bisect_left, bisect_right

# a = [1,2,4,4,8]
# x = 2

# print(bisect_left(a,x)) 
# print(bisect_right(a,x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a , left_value)
    return right_index - left_index
a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4))


# counter
from collections import Counter

counter = Counter(['red', 'blue', 'red','green','blue'])

print(counter['blue'])
print(dict(counter))


#factorial

import math
print(math.factorial(5))