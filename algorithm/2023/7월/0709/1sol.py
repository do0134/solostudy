n = int(input())
arr = list(map(int,input().split()))

youngsik = 0
minsik = 0

for i in range(n):
    youngsik += (arr[i]//30+1)*10
    minsik += (arr[i]//60+1)*15

if youngsik > minsik:
    answer = ["M", minsik]
elif youngsik < minsik:
    answer = ["Y", youngsik]
else:
    answer = ["Y","M",minsik]

print(*answer)