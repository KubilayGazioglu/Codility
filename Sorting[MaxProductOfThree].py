def solution(A):

    A.sort()

    return max((A[0] * A[1] * A[-1]), (A[-1] * A[-2] * A[-3]))

A = [4, 5, 1, 0]
B = [10, 10, 10]
solution(A)
solution(B)