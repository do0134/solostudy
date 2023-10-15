# 백준 20056 마법사 상어와 파이어볼

from collections import defaultdict

n,m,k = map(int,input().split())

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

fire = defaultdict(list)

for _ in range(m):
    r,c,ma,s,d = map(int,input().split())
    fire[(r-1,c-1)].append((ma,s,d))

for _ in range(k):
    result = defaultdict(list)

    # 이동
    for key in fire.keys():
        cr, cc = key
        for cm, cs, cd in fire[key]:
            nr,nc = cr+(dr[cd]*cs), cc+(dc[cd]*cs)
            nr %= n
            nc %= n
            result[(nr,nc)].append((cm,cs,cd))

    # 병합
    fire = defaultdict(list)
    for key in result.keys():
        flag = True
        if len(result[key]) == 1:
            fire[key] = result[key]
            continue

        mass = 0
        speed = 0
        for cm, cs, cd in result[key]:
            mass += cm
            speed += cs
            if cd%2 != result[key][0][2]%2:
                flag = False

        if flag:
            d_idx = 0
        else:
            d_idx = 1

        nm = mass//5
        ns = speed//len(result[key])

        if not nm:
            continue

        for nd in range(d_idx,8,2):
            fire[key].append((nm,ns,nd))

    if not fire:
        break

answer = 0

for key in fire.keys():
    for cm, cs, cd in fire[key]:
        answer += cm

print(answer)