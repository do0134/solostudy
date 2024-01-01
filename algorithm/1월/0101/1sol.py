# 백준 1541 잃어버린 괄호

s = input()
arr = list()

value = ""

for i in s:
    if i in "+-":
        arr.append(int(value))
        value = ""
        arr.append(i)
    else:
        value += i

if value:
    arr.append(int(value))

# todo: - 이후에 나오는 값을 최대한으로 만들어야 함. - 앞 숫자에 괄호 열고 다음 -에 괄호를 닫는다.

temp = 0
answer = 0
while arr:
    now = arr.pop()
    if now == "+":
        temp += arr.pop()
    elif now == "-":
        answer -= temp
        temp = 0
    else:
        temp = now

if temp:
    answer += temp

print(answer)
