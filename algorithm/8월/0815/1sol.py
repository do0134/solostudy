import sys

m,n = map(int,sys.stdin.readline().split())
length = 2*m-1
bugs = [1]*length

for _ in range(n):
    a,b,c = map(int,sys.stdin.readline().split())

    for i in range(a,a+b):
        bugs[i] += 1

    for i in range(a+b, length):
        bugs[i] += 2

for i in range(0,m,1) :
    for j in range(0,m,1) :
        if not j :
            print(bugs[m-1-i], end=" ")
        else :
            print(bugs[m+j-1], end=" ")
    print()