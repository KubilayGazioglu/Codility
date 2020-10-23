A = [1,2,3,4,5]
K = 3
def solution(A, K):
    firstArray = A
    newArray = [0] * len(A)

    if firstArray:
        if K > 0:
            for i in range(K):
                newArray[0] = firstArray[-1]
                newArray[1:] = firstArray[:-1]
                firstArray = newArray[:]
        else:
            newArray = A
    return newArray