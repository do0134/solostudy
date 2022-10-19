n = int(input())
hour = []
for _ in range(n):
    hour.append(list(map(int,input().split())))

hour.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = hour[0][1]
for i in range(1, n):
    if hour[i][0] >= end :
        cnt += 1
        end = hour[i][1]

print(cnt)

