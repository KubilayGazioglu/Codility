A=[1,2,3,1,4,5]

def solution(X,A):

    lista = set()

    for index,item in enumerate(A):
        if item <= X:
            lista.add(item)
        if len(lista) == X: return index

    return -1



solution(5,A)