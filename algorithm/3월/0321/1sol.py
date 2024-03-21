# 백준 2730 오늘은 OS 숙제 제출일

import sys
from enum import Enum
from datetime import datetime


class Result(Enum):
    PRIOR = "PRIOR"
    AFTER = "AFTER"
    SAME = "SAME DAY"
    OUT = "OUT OF RANGE"


def calc_date(origin, submit):
    o_date = datetime.strptime(origin, "%m/%d/%Y")
    s_date = datetime.strptime(submit, "%m/%d/%Y")
    delta = o_date - s_date

    if not delta.days:
        return Result.SAME.value
    elif abs(delta.days) > 7:
        return Result.OUT.value

    if abs(delta.days) == 1:
        day = "DAY"
    else:
        day = "DAYS"

    base_result = submit + f" IS {abs(delta.days)} {day} "

    if delta.days < 0:
        return base_result + Result.AFTER.value
    else:
        return base_result + Result.PRIOR.value


def check_month(origin, submit):
    o = origin.split("/")
    s = submit.split("/")
    year = int(o[2])
    if o[0] == "12" and s[0] == "1":
        year += 1
    elif o[0] == "1" and s[0] == "12":
        year -= 1

    submit += f"/{year}"
    return submit


input = sys.stdin.readline

t = int(input())

for _ in range(t):
    origin_date, submit_date = input().split()
    submit_date = check_month(origin_date, submit_date)
    print(calc_date(origin_date, submit_date))


