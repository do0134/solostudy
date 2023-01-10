def fishing(gate,people,index):
    distance = 0
    distance2 = False
    dist = 0
    direction = -1
    while people :
        x = gate + (dist * direction)
        if 0 <= x < n and not fish[x]:
            fish[x] += index
            distance += dist + 1
            people -= 1
        direction *= -1
        if direction == 1 and people:
            dist += 1
        if direction == -1 and not people:
            x2 = gate + (dist * direction)
            if 0<= x2 < n and not fish[x2]:
                distance2 = [x,x2]
    return distance,distance2


def solve(idx,dist):
    global answer
    if idx == 3 :
        answer = min(answer,dist)
        return
    else:
        for i in range(3):
            if visit[i]:
                continue
            visit[i] = 1
            distance, distance2 = fishing(arr[i][0],arr[i][1],i+1)
            solve(idx + 1, dist + distance)
            if distance2 :
                fish[distance2[0]] = 0
                fish[distance2[1]] = i + 1
                solve(idx +1, dist + distance)
                fish[distance2[0]] = i + 1
                fish[distance2[1]] = 0
            for j in range(n):
                if fish[j] == i + 1:
                    fish[j] = 0
            visit[i] = 0

        pass


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    answer = int(1e9)
    arr = [list(map(int,input().split())) for _ in range(3)]
    visit = [0]*3
    fish = [0] *n
    for i in arr :
        i[0] -= 1
    solve(0,0)
    print(f'#{tc} {answer}')