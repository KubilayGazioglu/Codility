"""def solution(A):
    B= set()
    for i in range(1,len(A)):
        calc = abs(sum(A[:i])-sum(A[i:]))
        B.add(calc)
    return min(B)"""
#O(N*N) çıkıyor. For zaten O(N) içinde, sum() fonksiyonu var O(N) //
#Totalde O(N*N) ediyor.Sum bir şekilde dışarı alınmalı.

def solution(A):
    total = sum(A)
    rest = 0
    B= set()
    #İki kere saydığımız için ilk rest kendini çıkarmak için.//
    # İkincisi toplamdan çıkarmak
    for i in A[:-1]:
        rest += i
        a = abs(total - rest - rest)
        B.add(a)
    return min(B)











    

A = [3,1,2,4,3]

solution(A)