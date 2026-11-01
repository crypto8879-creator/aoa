def lcs(X, Y):

    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0] * (n + 1) for i in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find matching characters
    result = []
    i = m
    j = n

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    result.reverse()

    return dp[m][n], "".join(result)


# Main program
string1 = "ALONGWAY"
string2 = "longest"

string1 = string1.lower()
string2 = string2.lower()

length, sequence = lcs(string1, string2)

print("Length of LCS:", length)
print("Matching String:", sequence)
#matrix-chain multiplication

def matrix_chain(p):

    n = len(p) - 1

    # Create DP table
    dp = [[0] * (n + 1) for i in range(n + 1)]

    # Calculate minimum cost
    for L in range(2, n + 1):

        for i in range(1, n - L + 2):

            j = i + L - 1
            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = dp[i][k] + dp[k+1][j] + p[i-1] * p[k] * p[j]

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]


# Main program
p = [10, 20, 30, 40]

print("Minimum Multiplications:", matrix_chain(p))

def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    cuts = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if prices[j] + dp[i - j - 1] > dp[i]:
                dp[i] = prices[j] + dp[i - j - 1]
                cuts[i] = j + 1

    pieces = []
    while n > 0:
        pieces.append(cuts[n])
        n -= cuts[n]

    return dp[-1], pieces


# Test
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
max_rev, pieces = rod_cutting(prices, n)

print("Max Revenue:", max_rev)
print("Pieces:", pieces)
