def countMax(upRight):
    # Write your code here

    min_r = int(1e9)
    min_c = int(1e9)

    for s in upRight:
        r, c = s.split(" ")
        r = int(r)
        c = int(c)
        min_r = min(r, min_r)
        min_c = min(c, min_c)

    answer = min_r * min_c

    return answer

