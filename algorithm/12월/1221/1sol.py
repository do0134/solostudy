# 벡준 1439 뒤집기

s = input()
zero = False
one = False
zero_cnt = 0
one_cnt = 0

for i in s:
    if i == "0" and not zero:
        zero = True
        one = False
        zero_cnt += 1
    elif i == "1" and not one:
        one = True
        zero = False
        one_cnt += 1


print(min(one_cnt, zero_cnt))