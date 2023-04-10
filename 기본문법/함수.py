def add(a,b):
    return a + b

print(add(1,4))


# 글로벌 키워드 
a = 0 

def func():
    global a
    a += 1

for i in range(10):
    func()

print('global',a)