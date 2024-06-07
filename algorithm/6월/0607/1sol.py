# 백준 20004 베스킨라빈스 31

A = int(input())

for i in range(1,A+1):
    if not 30%(i+1):
        print(i) 