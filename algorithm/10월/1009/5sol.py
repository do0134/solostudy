s = input()
v = list()
max_v = 0
idx = 0
flag = True
answer = ''
while idx < len(s):
    if s[idx].upper() not in v or s[idx] not in v:
        v.append(s[idx].upper())
        v.append(s[idx])
        if not s[idx].isupper():
            if max_v == s.count(s[idx])+s.count(s[idx].upper()):
                flag = True
            elif max_v < s.count(s[idx])+s.count(s[idx].upper()):
                flag = False
                max_v = s.count(s[idx])+s.count(s[idx].upper())
                answer = s[idx].upper()
        else:
            if max_v == s.count(s[idx]):
                flag = True
            elif max_v < s.count(s[idx]):
                flag = False
                max_v = s.count(s[idx])
                answer = s[idx]

    idx += 1

if flag :
    print('?')
else :
    print(answer)