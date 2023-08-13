# 1회
# 전부 같도록 하고 싶다. 
# 다솜이의 행동 연속된 하나 이상의 순자를 잡고 모두 뒤집는 것. 

# split() 사용하면 될 것 가탇. 

n = input()
result = 0


one = n.split('0')
zero = n.split('1')

print(one)

for i in one :
    if i != '' :
        result += 1

print('one',result)


# data = input()
# count0 = 0
# count1 = 0

# if data[0] == '1' :
#     count0 += 1
# else :
#     count1 += 1

# for i in range(len(data)-1):
#     if data[i] != data[i+1] :
#         if data[i+1] =='1':
#             count0 += 1
#         else :
#             count1 +=1

# print(min(count0,count1))