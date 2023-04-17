# 문제 : 카운터에는 거스름돈이 500원 100원 50원 10월짜리 동전이 무한히 존재한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구해라

n = 1260
count = 0

coin_types = [500, 100 , 50 , 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)