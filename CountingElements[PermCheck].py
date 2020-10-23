A= [1,3,2,4]

def solution(A):
    maxVal = len(A)
    lista = set(range(1,maxVal+1))
    ourList = set(A)

    compute = lista - ourList
    if compute:
        return 0
    else:
        return 1



solution(A)