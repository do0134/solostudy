# 백준 10431 줄세우기

p = int(input())

for _ in range(p):
    case = list(map(int,input().split(" ")))
    tc = case.pop(0)
    line = list()
    answer = 0

    for i in case:
        if not line:
            line.append(i)
        else:
            for j in range(len(line)):
                if line[j] > i:
                    answer += len(line)-j
                    line.insert(j,i)
                    break
            else:
                line.append(i)
    print(tc, answer)