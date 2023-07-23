# 백준 28352 10!

n = int(input())
value = 1

for i in range(1,n+1):
    value *= i

value //= (7*24*60*60)
print(value)