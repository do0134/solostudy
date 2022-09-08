n,m,a,k = map(int,input().split())
a -= k
if a  > n :
    answer = n
else:
    answer = a +1
if a %m == 0:
    print(answer, a // m+1)
else:
    print(answer, a// m + 2)