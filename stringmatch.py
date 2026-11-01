#KMP
def kmp(text, pattern):

    n = len(text)
    m = len(pattern)

    # Create LPS array
    lps = [0] * m

    j = 0
    for i in range(1, m):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
        else:
            j = 0

    # Search pattern in text
    i = 0
    j = 0

    while i < n:

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print("Pattern found at index:", i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


# Main program
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"


kmp(text, pattern)
#boyre moore
def boyer_moore(text, pattern):

    n = len(text)
    m = len(pattern)

    # Create bad character table
    bad = {}

    for i in range(m):
        bad[pattern[i]] = i

    # Search pattern in text
    s = 0

    while s <= n - m:

        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print("Pattern found at index:", s)
            s += 1
        else:
            s += max(1, j - bad.get(text[s + j], -1))


# Main program
text = "ABAAABCD"
pattern = "ABC"

boyer_moore(text, pattern)
#rabin karp
def rabin_karp(text, pattern):

    n = len(text)
    m = len(pattern)

    d = 256
    q = 101

    p = 0
    t = 0
    h = 1

    # Calculate h value
    for i in range(m - 1):
        h = (h * d) % q

    # Calculate hash values
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Search pattern
    for i in range(n - m + 1):

        if p == t:
            if text[i:i+m] == pattern:
                print("Pattern found at index:", i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q


# Main program
text = "ABCCDDAEFG"
pattern = "CDD"

rabin_karp(text, pattern)
