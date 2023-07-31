# 백준 1935 후위 표기식2
# https://www.acmicpc.net/problem/1935

from collections import defaultdict

n = int(input())
arr = list(input())
my_dict = defaultdict(int)

for i in range(n):
    temp = int(input())
    my_dict[chr(65+i)] = temp

stack = list()

for i in arr:
    if i in "+-/*":
        b = stack.pop()
        a = stack.pop()
        if i == "+":
            stack.append(a+b)
        elif i == "-":
            stack.append(a-b)
        elif i == "/":
            stack.append(a/b)
        elif i == "*":
            stack.append(a*b)
    else:
        stack.append(my_dict[i])

print("%.2f" %stack.pop())