A = [1, 3, 6, 4, 1, 2]
B=[-1,-2]
C=[4,5,6,2]

def solution(A):
    neg = all(i < 0 for i in A)
    if neg:
        return 1
    if len(A) == 1:
        return max(A)-1
    else:
        a = set(range(min(A), max(A)))
        b = set(A)
        calc = a - b
        if not calc:
            return max(b)+1
        return int(*calc)
#Max counter dönmeli  //
#
solution(C)