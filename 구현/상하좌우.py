# 여행가 A는 N*N 크기의 정사각형 공간 위에 서있다. 이 공간은 1 * 1 정사각형으로 나누어져있다.
# 가장 왼쪽을 (1,1) 오른쪽 아래를 (N,N)이라고 한다. 여행가 A는 상 하 좌 우로
# 이동 가능하며 시작은 항상 (1,1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다. 
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 L,R,U,D 중 하나의 문자가 반복적으로 적혀있다. 
# value = int(input())
# list = list(map(str,input().split()))
# x , y = (1,1)

# for way in list :
    
#     if way == 'R' :
#         nx = x
#         ny = y + 1
#     elif way == 'L' :
#         nx = x
#         ny = y -1
#     elif way == "U" :
#         nx = x -1
#         ny = y
#     else : 
#         nx = x + 1
#         ny = y


#     # 0 일때는 상위 스코프에 있는 x , y를 가지고 올 수 있도록 함. 
#     if 0<nx<=value and 0<ny<=value:
#         x = nx
#         y = ny
# print(x,y)
        

# x가 1일때는 U 무시
# y가 1일때는 L 무시
# x가 n일때는 D 무시
# y가 n일때는 R 무시


# 두번 쨰 

value = int(input())
list = list(map(str,input().split()))
x , y = (1,1)

for way in list :
    
    if way == 'R' :
        nx = x
        ny = y + 1
    elif way == 'L' :
        nx = x
        ny = y -1
    elif way == "U" :
        nx = x -1
        ny = y
    else : 
        nx = x + 1
        ny = y


    # 0 일때는 상위 스코프에 있는 x , y를 가지고 올 수 있도록 함. 
    if 0<nx<=value and 0<ny<=value:
        x = nx
        y = ny
print(x,y)
        
