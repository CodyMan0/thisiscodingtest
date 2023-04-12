# 문자 포맷팅
## 숫자 바로 대입
print("I eat %d apples" % 3)

## 문자열 바로 대입
print("I eat %s apples" %"five")

## 2개 이상 대입
number =10
day = "three"
print ("I ate %d apples. so i was sick for %s days" %(number , day))


## format 함수로 포매팅
print("I eat {0} apples".format("three"))
print("I eat {0} apples during {1}days".format("three", 3))


## 공백 채우기
print("{0:=^10}".format("hi"))

## f 사용 
print(f"I eat {3} apples")




# 문자열 내장 함수



# 리스트 합치지 
x = [1,2,8,4]
y = ["hello", "world"]
z = x+y
z[1] = 10
print(z)
print(x)
# 원시형 타입에서는 깊은 복사가 이루어지네! 


# 내장함수
k = sorted(x)
z = sum(x)

print("======================")
# 튜플

x =(1,2,3)
y =('a','b','c')
z = (1, 'hello', 'there')


print(x + y)
print('a' in y )
print(z.index(1))
#list와 동일하다. 대부분
# 튜플이 안되는건 할당!! 

print("======================")

x = {
    'name' : 'ju',
    'age': '28'
}
y = {} 

# 사용할 수 있는 메소드
print(x.keys())

for key in x:
    print(key)
    print(x[key])


fruit = ['사과', '사과','바나나','바나나','딸기','키워','복숭아','복숭아','복숭아']

d ={}

for f in fruit:
    if f in d :
        d[f] += 1
    else:
        d[f] = 1
print(d) 




