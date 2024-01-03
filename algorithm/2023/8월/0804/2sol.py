# softeer 회의실 예약
# https://softeer.ai/practice/info.do?idx=1&eid=626&sw_prbl_sbms_sn=236355

from collections import defaultdict

n, m = map(int,input().split())
rooms = defaultdict(list)
for _ in range(n):
    room = input()
    rooms[room] = [0]*19

keys = sorted(rooms.keys())

for _ in range(m):
    room, s, e = input().split()
    s,e = int(s),int(e)
    for i in range(s,e):
        rooms[room][i] = 1

for i in range(len(keys)):
    key = keys[i]
    print(f'Room {key}:')
    available = list()
    idx = 9
    while idx < 18:
        if not rooms[key][idx]:
            start = idx

            while idx < 18 and not rooms[key][idx]:
                idx += 1
            end = idx
            start = str(start)
            end = str(end)
            if len(start) == 1:
                start = '0'+start
            if len(end) == 1:
                end = '0'+ end
            available.append([start,end])
        idx += 1
    if available:
        print(f'{len(available)} available:')
        for s, e in available:
            print(f'{s}-{e}')
    else:
        print("Not available")
    if i != len(keys)-1:
        print('-----')
