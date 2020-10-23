def solution(X, Y, D):
    #X start point
    #Y Destination point
    #D step size

    totalDistance = Y-X

    if totalDistance % D == 0:
        return totalDistance//D
    else:
        return totalDistance//D + 1







solution(1,1,3)
