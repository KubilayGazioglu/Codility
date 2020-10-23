def solution(A):

    if len(A)<3:
        return 0
    A.sort()
    for i in range(len(A)-2):
        if (A[i] + A[i+1] > A[i+2] and A[i+1] + A[i+2] > A[i] and A[i+2] + A[i] > A[i+1]):
            return 1
    return 0


A = [10,50,5,1]
solution(A)

"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].

"""