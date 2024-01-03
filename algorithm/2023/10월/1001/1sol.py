# 백준 1522 문자열 교환

s = list(input())
a_cnt = s.count('a')
s += s
answer = int(1e9)

for i in range(len(s)-a_cnt+1):
    answer = min(answer, s[i:i+a_cnt].count('b'))

print(answer)