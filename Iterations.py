def solution(N):
    rep = str(bin(N)[2:])
    max = 0
    count = 0
    control = False
    for idx in rep:
        if idx == "1":
            if max < count:
                max = count
            control = True
            count = 0
        elif control:
            count = count+1
    return max



