# 백준 16968 차량 번호판 1

s = input()
prev = ""
answer = 1
for i in s:
    if i == "c":
        if prev == "c":
            answer *= 25
        else:
            answer *= 26
            prev = "c"
    else:
        if prev == "d":
            answer *= 9
        else:
            answer *= 10
            prev = "d"

print(answer)