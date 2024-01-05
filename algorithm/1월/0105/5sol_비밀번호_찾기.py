# 백준 17219 비밀번호 찾기
# https://www.acmicpc.net/problem/17219

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

site_dict = defaultdict(str)
for _ in range(n):
    key, value = input().split()
    site_dict[key] = value

for _ in range(m):
    site = input().rstrip()
    print(site_dict[site])
