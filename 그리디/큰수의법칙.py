n,m,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort(reverse=True)
first = array[0]
second = array[1]


result = 0

while True:
    for i in range(k) :
        print(m)
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)