# 백준 2831 댄스파티

n = int(input())
m = list(map(int,input().split()))
w = list(map(int,input().split()))
m_pos = list()
w_pos = list()
m_neg = list()
w_neg = list()

for i in range(n):
    if m[i] > 0:
        m_pos.append(m[i])
    else:
        m_neg.append(abs(m[i]))
    if w[i] > 0:
        w_pos.append(w[i])
    else:
        w_neg.append(abs(w[i]))

answer = 0
m_pos.sort()
m_neg.sort()
w_pos.sort()
w_neg.sort()

l = 0
r = 0

while l < len(m_pos) and r < len(w_neg):
    if m_pos[l] < w_neg[r]:
        answer += 1
        l += 1
        r += 1
    else:
        r += 1

l = 0
r = 0
while l < len(w_pos) and r < len(m_neg):
    if w_pos[l] < m_neg[r]:
        answer += 1
        l += 1
        r += 1
    else:
        r += 1

print(answer)

