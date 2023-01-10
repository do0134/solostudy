# 어차피 13개 중에서 m개 뽑아내는 조합 몇 개 없으니까...
# 치킨 집이 없을 수 있는 조합을 뽑아서 집에서 가장 거리가 가까운 값을 비교하면 되지 않을까


from itertools import combinations
import copy
def back(rem):
    global min_v
    total = 0
    temp = copy.deepcopy(chic)
    for i in rem:
        temp[chicken[i][0]][chicken[i][1]] = 0
    live = []
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 2:
                live.append([i,j])

    for a,b in house:
        min_d = int(1e9)
        for c,d in live:
            min_d = min(abs(a-c)+abs(b-d),min_d)
        total += min_d
    min_v = min(min_v, total)

n,m = map(int,input().split())
chic = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if chic[i][j] == 1:
            house.append([i,j])
        elif chic[i][j] == 2:
            chicken.append([i,j])

idx = [i for i in range(len(chicken))]
remove = []
min_v = int(1e9)
if m == len(chicken):
    total = 0
    for a, b in house:
        min_d = int(1e9)
        for c, d in chicken:
            min_d = min(abs(a - c) + abs(b - d), min_d)
        total += min_d
    print(total)
else:
    for i in combinations(idx,len(chicken)-m):
        back(i)

    print(min_v)




