# Egg dropping refers to a class of problems in which it is important to find the correct response without exceeding a (low) number of certain failure states.
#In a toy example, there is a tower of nnn floors, and an egg dropper with mmm ideal eggs. The physical properties of the ideal egg is such that it will shatter
#if it is dropped from floor n∗n^*n∗ or above, and will have no damage whatsoever if it is dropped from floor n∗−1n^*-1n∗−1 or below.

# DP solution
def solvepuzzle(N,k):
    for i in range (1, N):
        numdrops[i][1] = 1
        numdrops[i][0] = 0

    for i in range(1, k):
        numdrops[1][i] = i

    for i in range(2, N):
        for j in range(2, k): 

            numdrops[i][j] = INF
            minimum = INF

            for x in range(1, j)
                minimum = min(minimum, 1 + max(numdrops[i-1][x-1],numdrops[i][j-x]))

            numdrops[i][j] = minimum


    return numdrops[N][k]
