n,m = map(int,input().split())

d = set()
for _ in range(n):
    name = input()
    d.add(name)
cnt = 0
l = set()
for _ in range(m):
    name = input()
    l.add(name)
answer = d&l
answer = sorted(list(answer))
print(len(answer))
for i in answer:
    print(i)
