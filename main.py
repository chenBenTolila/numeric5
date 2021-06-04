def neville(pointsList, m, n, X):
    if m is n:
        return pointsList[m][1]
    else:
        res = (X - pointsList[m][0]) * neville(pointsList, m+1, n, X) - (X - pointsList[n][0]) * neville(pointsList, m, n-1, X)
        res /= (pointsList[n][0] - pointsList[m][0])
        return res

points = [[]]

