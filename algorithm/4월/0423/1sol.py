def solution(park, routes):
    start = [-1, -1]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start = [i, j]
                break
        if start != [-1, -1]:
            break
    for route in routes:
        direction, far = route.split(" ")
        far = int(far)
        d = [0, 0]
        if direction == "E":
            d = [0, far]
        elif direction == "S":
            d = [far, 0]
        elif direction == "W":
            d = [0, -far]
        elif direction == "N":
            d = [-far, 0]
        nr = d[0] + start[0]
        nc = d[1] + start[1]
        if 0 <= nr < len(park) and 0 <= nc < len(park[0]):
            flag = False
            for i in range(start[0], nr + 1):
                for j in range(start[1], nc + 1):
                    if park[i][j] == "X":
                        flag = True
                        break
                if flag:
                    break
            else:
                start = [nr, nc]

    return start