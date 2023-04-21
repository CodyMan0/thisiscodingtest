# 입력
# 첫번쨰 줄 학생의 수 n
# 두번째 학생의 이름의 문자열 A와 점수를 나타내는 정수 B 공백으로 구분


# 출력
# 모든 학생의 이름을 성적이 앉은 순서대로 출력 
n = int(input())
data = []
for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

# key를 이용해서 점수를 기준으로 정렬
array = sorted(data , key=lambda x: x[1])

for student in array :
    print(student[0], end=" ")
