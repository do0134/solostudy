# 백준 6581 HTML

import sys

string = list()

for i in sys.stdin:
    string.append(i)

temp = ""
hr = "-"*80
for s in string:
    s_list = s.split()
    for i in s_list:
        if not i:
            continue
        if i == "<br>":
            print(temp)
            temp = ""
        elif i == "<hr>":
            if temp:
                print(temp)
                temp = ""
            print(hr)
        else:
            if not temp:
                temp = i
            else:
                prev_temp = temp
                temp += i
                temp += " "
                if len(temp) > 80:
                    print(prev_temp)
                    temp = i
if temp:
    print(temp)