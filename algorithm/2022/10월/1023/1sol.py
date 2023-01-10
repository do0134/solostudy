# 코딩 도장 숫쟈야구
import random
# 정답 뽑기!

answer= ""

while len(answer) < 3:
    temp = str(random.randint(0,9))
    if temp not in answer:
        answer += temp
idx = 0
while True:
    idx += 1
    print(f"{idx}번째 도전!")
    user_submit = input("세자리 숫자를 입력해주세요 : ")
    if user_submit == answer:
        print("정답입니다!")
        break
    if len(user_submit) != 3:
        print("세 자리를 입력해주세요!")
    elif not user_submit.isdigit():
        print("숫자를 입력해주세요!")
    elif len(set(user_submit)) != 3:
        print("중복된 값은 입력할 수 없습니다.")
    else:
        s,b= 0,0
        for i in range(3):
            if user_submit[i] == answer[i]:
                s += 1
            elif user_submit[i] in answer:
                b += 1
        print(f"{s}S{b}B")



