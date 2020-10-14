# Egg dropping refers to a class of problems in which it is important to find the correct response without exceeding a (low) number of certain failure states.
In a toy example, there is a tower of nnn floors, and an egg dropper with mmm ideal eggs. The physical properties of the ideal egg is such that it will shatter
if it is dropped from floor n∗n^*n∗ or above, and will have no damage whatsoever if it is dropped from floor n∗−1n^*-1n∗−1 or below.

# DP solution
def solvepuzzle(N,k):
    for i = 1 to N
        numdrops(i,1) = 1
        numdrops(i,0) = 0
    end for

    for i=1 to k
        numdrops(1, i) = i
    end for

    for i = 2 to N
        for j = 2 to k 

            numdrops[i][j] = ∞
            minimum = ∞

            for x = 1 to j
                minimum = min(minimum, 
                1 + max(numdrops(i-1,x-1),numdrops(i,j-x))
                )
            end for

            numdrops[i][j] = minimum

        end for
    end for

    return numdrops(N,k)
