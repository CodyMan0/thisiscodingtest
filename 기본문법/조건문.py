# 간단한 조건문
score = 95

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점: C")
else:
    print("학점: f")

# 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

a = [1,2,3,4,5,5,5]

remove_set = {3,5}

# result = []
# for i in a :
#     if i not in remove_set:
#         result.append(i)
# print(result)

result = [i for i in a if i not in remove_set]
print(result)



