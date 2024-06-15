# 백준 4358 생태학

import sys
from collections import defaultdict

input = sys.stdin.readline
cnt = 0
str_dict = defaultdict(int)

while True:
    try:
        temp = input().rstrip()
        if not temp:
            break
        str_dict[temp] += 1
        cnt += 1
    except:
        break

for i in sorted(str_dict.keys()):
    print("%s %.4f" %(i, (str_dict[i]/cnt*100)))