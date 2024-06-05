# 백준 20170 Commemorative Dice

a = list(map(int,input().split()))
b = list(map(int,input().split()))

args = [36,18,12,9,4,3,2]

temp = 0
temp1 = 36

for i in range(6):
    for j in range(6):
        if a[i] > b[j]:
            temp += 1

flag = True

while flag:
    flag = False

    for arg in args:
        if temp >= arg and temp % arg == 0 and temp1 %arg == 0:
            flag = True
            temp //= arg
            temp1 //= arg
            break

if temp == temp1:
    print(1)
else:
    print(f"{temp}/{temp1}")