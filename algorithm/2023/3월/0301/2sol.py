n = int(input())
lopes = list()

for _ in range(n) :
    lopes.append(int(input()))

lopes.sort(reverse=True)
answer = 0
while lopes :
    lope = lopes.pop()
    if lope*n > answer :
        answer = lope*n
    n -= 1

print(answer)