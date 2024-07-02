# 백준 2195 문자열 복사

s = input()
p = input()

temp = ""
answer = 1

for i in p:
    if s.find(temp + i) >= 0:
        temp += i
        continue
    temp = i
    answer += 1

print(answer)