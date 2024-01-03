# softeer 플레이페어 암호
# https://softeer.ai/practice/info.do?idx=1&eid=804&sw_prbl_sbms_sn=235674

from collections import defaultdict

s1 = input()
s2 = input()
v = set()
arr = [[] for _ in range(5)]
idx = 0

for i in s2:
    if i == "J":
        continue
    if i not in v:
        v.add(i)
        arr[idx].append(i)
    if idx >= 5:
        break
    if idx < 5 and len(arr[idx]) == 5:
        idx += 1


def make_start(idx):
    if idx >= 5:
        return
    if len(arr[idx]) == 5:
        idx += 1

    for i in range(26):
        if chr(65+i) == "J":
            continue
        if chr(65+i) not in v:
            arr[idx].append(chr(65+i))
            v.add(chr(65+i))
        if len(arr[idx]) == 5:
            idx += 1
        if idx >= 5:
            return


make_start(idx)

arr2 = list()
idx = 0
while idx < len(s1):
    if idx != len(s1)-1:
        first, second = s1[idx], s1[idx+1]
        if first == second:
            if first != "X":
                first = first + "X"
            elif first == "X":
                first = first + "Q"

            if idx+2 < len(s1):
                if s1[idx+2] == second and second != "X":
                    second = second+"X"
                    idx += 2
                elif s1[idx+2] == second and second == "X":
                    second = second + "Q"
                    idx += 2
                elif s1[idx+2] != second:
                    second = second+s1[idx+2]
                    idx += 3
            else:
                second = second+"X"
                idx += 2
            arr2.append(first)
            arr2.append(second)
        else:
            arr2.append(first+second)
            idx += 2
    else:
        arr2.append(s1[idx]+"X")
        idx += 1


def check_idx(s):
    idx1 = [0,0]
    idx2 = [0,0]
    for i in range(5):
        for j in range(5):
            if arr[i][j] == s[0]:
                idx1 = [i,j]
            if arr[i][j] == s[1]:
                idx2 = [i,j]
    return idx1, idx2


crypto = defaultdict(str)

for s in arr2:
    idx1, idx2 = check_idx(s)
    if idx1[0] == idx2[0]:
        idx1[1] += 1
        idx2[1] += 1
        if idx1[1] == 5:
            idx1[1] = 0
        if idx2[1] == 5:
            idx2[1] = 0
    elif idx1[1] == idx2[1]:
        idx1[0] += 1
        idx2[0] += 1
        if idx1[0] == 5:
            idx1[0] = 0
        if idx2[0] == 5:
            idx2[0] = 0
    else:
        temp = idx1[1]
        idx1[1] = idx2[1]
        idx2[1] = temp

    crypto[s] = arr[idx1[0]][idx1[1]] + arr[idx2[0]][idx2[1]]

answer = ""
for i in arr2:
    answer += crypto[i]

print(answer)


