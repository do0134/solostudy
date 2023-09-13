# 백준 9017 크로스 컨트리

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt1 = dict()
    cnt2 = dict()
    max_idx = 0

    for i in arr:
        if i not in cnt1.keys():
            cnt1[i] = 1
            cnt2[i] = 1
        else:
            cnt1[i] += 1
            cnt2[i] += 1
        max_idx = max(i, max_idx)

    total_score = [0]*(max_idx+1)
    score = 1
    five = list()
    for i in range(n):
        if cnt1[arr[i]] < 6:
            total_score[arr[i]] = int(1e9)
            continue
        elif cnt2[arr[i]] == 1:
            score += 1
            continue
        elif cnt2[arr[i]] == 2:
            five.append(arr[i])
            cnt2[arr[i]] -= 1
            score += 1
        else:
            total_score[arr[i]] += score
            score += 1
            cnt2[arr[i]] -= 1

    total_score[0] = int(1e9)
    min_score = min(total_score)
    can_answer = list()

    for i in cnt1.keys():
        if total_score[i] == min_score:
            can_answer.append(i)

    if len(can_answer) == 1:
        print(can_answer[0])
    else:
        for i in five:
            if i in can_answer:
                print(i)
                break
