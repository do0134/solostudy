s = input()
flag = False
max_v = 0
answer = ''
for i in range(0,26):
    temp = s.count(chr(65+i))+s.count(chr(97+i))
    if max_v == temp:
        flag = True
    elif max_v < temp:
        flag = False
        max_v = temp
        answer = chr(65+i)
if flag :
    print('?')
else:
    print(answer)


