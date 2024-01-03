# 백준 2304 창고 다각형

n = int(input())
square = list()

max_h = 0
max_h_list = list()

for _ in range(n):
    x,y = map(int,input().split())
    square.append((x,y))
    if y == max_h:
        max_h_list.append((x,y))
    elif y > max_h:
        max_h_list = list()
        max_h_list.append((x,y))
        max_h = y

square.sort()
max_h_list.sort()
l,r = max_h_list[0][0], max_h_list[-1][0]
answer = 0
max_x, max_y = square[0]

for i in range(n):
    cx, cy = square[i]
    if cy == max_h:
        answer += ((cx-max_x)*max_y)
        break
    if cy > max_y:
        answer += ((cx-max_x)*max_y)
        max_y = cy
        max_x = cx

max_x, max_y = square[-1]

for i in range(n-1,-1,-1):
    cx, cy = square[i]
    if cy == max_h:
        answer += ((max_x-cx)*max_y)
        break
    if cy > max_y:
        answer += ((max_x-cx)*max_y)
        max_y = cy
        max_x = cx

answer += ((r-l+1)*max_h)

print(answer)