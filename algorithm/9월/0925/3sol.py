# 틀림 + 시간초과

from itertools import permutations

n = int(input())
arr = list()
for i in range(n):
    arr.append(input())
k = int(input())

total = 0
answer = 0


for i in range(1,n+1):
    for j in permutations(arr,i):
        total += 1
        temp = ''
        for p in j:
            temp+= p
        if int(temp) % k == 0:
            answer += 1
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

g = gcd(answer,total)
if answer == 0:
    print('0/1')
elif answer == total:
    print('1/1')
else:
    print(f'{answer//g}/{total//g}')
# def perm(per,idx,target):
#     global total, answer
#     if idx == target:
#         total += 1
#         if int(per)%k == 0:
#             answer += 1
#         return
#     else:
#         for i in range(n):


