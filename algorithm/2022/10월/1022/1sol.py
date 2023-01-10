n = int(input())
temp = n // 5
while temp >= 0 :
    check = n - temp*5
    if check % 3 == 0:
        print(temp + check // 3)
        break
    else:
        temp -= 1
else:
    print(-1)