# 점화실 ai = ai-1 + a-2 * 2

n = int(input())
dt = [0]*(n+1)

dt[1] = 1
dt[2] = 3
for i in range(3,n+1):
    dt[i] = (dt[i-1] + 2*dt[i-2]) % 796796

print(dt)
print(dt[n])