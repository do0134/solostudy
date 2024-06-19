# 백준 21867 Java Bitecode

n = input()
s = input()
answer = ""

for i in s:
    if i == "J" or i == "A" or i == "V":
        continue
    answer += i

if not answer:
    print("nojava")
else:
    print(answer)