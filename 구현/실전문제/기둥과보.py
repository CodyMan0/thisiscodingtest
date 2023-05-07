# 이문제 핵심은 조건문을 활용한 조건을 정확히 구현하는게 핵심 포인트!


def possible(answer) : 
    for x,y, stuff in answer : 
        if stuff == 0 :
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer :
                continue
            return False
        elif stuff == 1 :
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer) :
                continue
            return False
    return True
    

def solution (n,build_frame) :
    answer =[]
    for frame in build_frame :
        x,y,stuff,operate = frame
        if operate == 0 : 
            print('banswer',answer)
            answer.remove([x,y,stuff])
            print('answer',answer)
            if not possible(answer) :
                answer.append([x,y,stuff])
        if operate == 1 :
            print('answer',answer)
            answer.append([x,y,stuff])
            if not possible(answer) :
                answer.remove([x,y,stuff])
    return sorted(answer)



    
n = 5
build= [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n,build))