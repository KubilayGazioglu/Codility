A=[9,3,9,3,9,7,9]

def solution(A):
    dicta = {}

    for i in A:
        if i not in dicta:
            dicta[i] = 1
        else:
            dicta[i] = dicta[i] + 1

    for j in dicta:
        if dicta[j] % 2 == 1:
            return j




solution(A)