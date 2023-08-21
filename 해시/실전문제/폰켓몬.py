# # 홍박사님이 N/2개는 연구실에서 제공
# # 폰켓몬 종류에 따라 번호. 같은 종류 == 같은 번호
# # 예시 [3,1,2,3] 경우의 수 고려하여 2개 선택해야한다
# # 동일한 번호 선택하면 종류는 1개로 체크 

# # N개 폰켓몬 주어질때 절반을 픽할때 가장 많은 종류의 폰켓몬 선택하는 방법

# def mySolution(nums):
#     set_num = set(nums)
#     kind_num = len(set_num)
#     pick_num = len(nums) // 2

#     if kind_num >= pick_num :
#         return pick_num 
#     else : 
#         return kind_num


# def otherSolution(ls):
#     return min(len(ls)/2, len(set(ls)))


# 홍박사님이 N/2개는 연구실에서 제공
# 폰켓몬 종류에 따라 번호. 같은 종류 == 같은 번호
# 예시 [3,1,2,3] 경우의 수 고려하여 2개 선택해야한다
# 동일한 번호 선택하면 종류는 1개로 체크 

# N개 폰켓몬 주어질때 절반을 픽할때 가장 많은 종류의 폰켓몬 선택하는 방법

def mySolution(nums):
    set_num = set(nums)
    kind_num = len(set_num)
    pick_num = len(nums) // 2

    if kind_num >= pick_num :
        return pick_num 
    else : 
        return kind_num


def otherSolution(ls):
    return min(len(ls)/2, len(set(ls)))