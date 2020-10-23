def solution(A):
    n = len(A)+1

    sum1 = n*(n+1)//2

    return print(sum1-sum(A))

A=[1,2,3,5]

solution(A)