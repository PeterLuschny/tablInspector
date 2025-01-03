from functools import cache
from _tabltypes import Table

"""Fibonacci-Pascal triangle.

[0] [ 1]
[1] [ 0,  1]
[2] [ 1,  1,  1]
[3] [ 1,  2,  2,  1]
[4] [ 2,  3,  4,  3,  1]
[5] [ 3,  5,  7,  7,  4,  1]
[6] [ 5,  8, 12, 14, 11,  5,  1]
[7] [ 8, 13, 20, 26, 25, 16,  6,  1]
[8] [13, 21, 33, 46, 51, 41, 22,  7, 1]
[9] [21, 34, 54, 79, 97, 92, 63, 29, 8, 1]
"""


@cache
def fibonacci(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = fibonacci(n - 1) + [1]
    s = row[1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1]
    row[0] = s
    return row


Fibonacci = Table(
    fibonacci, 
    "Fibonacci", 
    ["A354267", "A105809", "A228074"], 
    "A000000", 
    r"T(n-1, k-1) + T(n-1, k)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Fibonacci)


''' OEIS
    Fibonacci_Tinv          -> 0 
    Fibonacci_Trev          -> 0 
    Fibonacci_Trev11        -> 0 
    Fibonacci_Tantidiag     -> 0 
    Fibonacci_Tacc          -> 0 
    Fibonacci_Tder          -> 0 
    Fibonacci_TablLcm       -> 0 
    Fibonacci_EvenSum       -> 0 
    Fibonacci_AccSum        -> 0 
    Fibonacci_AccRevSum     -> 0 
    Fibonacci_CentralO      -> 0 
    Fibonacci_PosHalf       -> 0 
    Fibonacci_NegHalf       -> 0 
    Fibonacci_TransNat1     -> 0 
    Fibonacci_TransSqrs     -> 0 
    Fibonacci_InvBinConv    -> 0 
    Fibonacci_PolyCol2      -> 0 
    Fibonacci_PolyCol3      -> 0 
    Fibonacci_PolyDiag      -> 0 
    Fibonacci_RevToff11     -> 0 
    Fibonacci_RevTantidiag  -> 0 
    Fibonacci_RevTacc       -> 0 
    Fibonacci_RevTalt       -> 0 
    Fibonacci_RevTder       -> 0 
    Fibonacci_RevEvenSum    -> 0 
    Fibonacci_RevOddSum     -> 0 
    Fibonacci_RevAccRevSum  -> 0 
    Fibonacci_RevAntiDSum   -> 0 
    Fibonacci_RevColMiddle  -> 0 
    Fibonacci_RevTransNat0  -> 0 
    Fibonacci_RevTransNat1  -> 0 
    Fibonacci_RevTransSqrs  -> 0 
    Fibonacci_RevPolyCol3   -> 0 
    Fibonacci_RevPolyDiag   -> 0 
    Fibonacci_TablDiag0     -> https://oeis.org/A12
    Fibonacci_RevPolyRow1   -> https://oeis.org/A12
    Fibonacci_TablDiag1     -> https://oeis.org/A27
    Fibonacci_PolyRow1      -> https://oeis.org/A27
    Fibonacci_TablCol0      -> https://oeis.org/A45
    Fibonacci_TablCol1      -> https://oeis.org/A45
    Fibonacci_AltSum        -> https://oeis.org/A45
    Fibonacci_TablCol2      -> https://oeis.org/A71
    Fibonacci_TablDiag2     -> https://oeis.org/A124
    Fibonacci_TablCol3      -> https://oeis.org/A1924
    Fibonacci_PolyRow2      -> https://oeis.org/A2061
    Fibonacci_RevPolyRow2   -> https://oeis.org/A2061
    Fibonacci_TablDiag3     -> https://oeis.org/A4006
    Fibonacci_AntiDSum      -> https://oeis.org/A6367
    Fibonacci_TablMax       -> https://oeis.org/A27988
    Fibonacci_ColMiddle     -> https://oeis.org/A27988
    Fibonacci_PolyRow3      -> https://oeis.org/A69778
    Fibonacci_RevPolyRow3   -> https://oeis.org/A69778
    Fibonacci_TransNat0     -> https://oeis.org/A79282
    Fibonacci_TablSum       -> https://oeis.org/A99036
    Fibonacci_OddSum        -> https://oeis.org/A99036
    Fibonacci_AbsSum        -> https://oeis.org/A99036
    Fibonacci_Toff11        -> https://oeis.org/A105809
    Fibonacci_Tinv11        -> https://oeis.org/A105810
    Fibonacci_RevCentralO   -> https://oeis.org/A108081
    Fibonacci_RevNegHalf    -> https://oeis.org/A113312
    Fibonacci_TablGcd       -> https://oeis.org/A174965
    Fibonacci_RevTrev11     -> https://oeis.org/A228074
    Fibonacci_Triangle      -> https://oeis.org/A354267
    Fibonacci_Talt          -> https://oeis.org/A354267
    Fibonacci_CentralE      -> https://oeis.org/A371870
    Fibonacci_BinConv       -> https://oeis.org/A371870

    Fibonacci: Distinct: 22, Hits: 32, Misses: 34
'''
