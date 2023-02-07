"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


def romanToInt(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0

    for ind, val in enumerate(s):
        
        if ind != len(s) - 1:
            if romans[val] >= romans[s[ind + 1]]:
                total += romans[val]
            else:
                total -= romans[val]

    total += romans[s[len(s) - 1]]

    return total

print(romanToInt("MCMXCIV"))