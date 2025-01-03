from functools import cache
from math import factorial
from _tabltypes import Table


"""Baxter polynomials.

[0] 1
[1] 0, 1
[2] 0, 1,   1
[3] 0, 1,   4,    1
[4] 0, 1,  10,   10,     1
[5] 0, 1,  20,   50,    20,     1
[6] 0, 1,  35,  175,   175,    35,     1
[7] 0, 1,  56,  490,   980,   490,    56,    1
[8] 0, 1,  84, 1176,  4116,  4116,  1176,   84,   1
[9] 0, 1, 120, 2520, 14112, 24696, 14112, 2520, 120, 1
"""


@cache
def F(n: int) -> int:
    return factorial(n) ** 3 * ((n + 1) * (n + 1) * (n + 2))


@cache
def baxter(n: int) -> list[int]:
    if n == 0:
        return [1]
    return [0] + [(2 * F(n - 1)) // (F(k - 1) * F(n - k)) for k in range(1, n + 1)]


Baxter = Table(
    baxter, 
    "Baxter", 
    ["A359363", "A056939"],
    "A000000",
    "x Hyper([-1 - n, -n, 1 - n], [2, 3], -x)"
 )


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Baxter)


''' OEIS
    Baxter_Tinv          -> 0 
    Baxter_Tinv11        -> 0 
    Baxter_Tinvrev11     -> 0 
    Baxter_Tantidiag     -> 0 
    Baxter_Tacc          -> 0 
    Baxter_Tder          -> 0 
    Baxter_TablLcm       -> 0 
    Baxter_TablGcd       -> 0 
    Baxter_TablMax       -> 0 
    Baxter_EvenSum       -> 0 
    Baxter_OddSum        -> 0 
    Baxter_AltSum        -> 0 
    Baxter_AccRevSum     -> 0 
    Baxter_AntiDSum      -> 0 
    Baxter_ColMiddle     -> 0 
    Baxter_CentralE      -> 0 
    Baxter_CentralO      -> 0 
    Baxter_TransNat1     -> 0 
    Baxter_TransSqrs     -> 0 
    Baxter_BinConv       -> 0 
    Baxter_InvBinConv    -> 0 
    Baxter_PolyRow3      -> 0 
    Baxter_PolyCol2      -> 0 
    Baxter_PolyCol3      -> 0 
    Baxter_PolyDiag      -> 0 
    Baxter_RevToff11     -> 0 
    Baxter_RevTrev11     -> 0 
    Baxter_RevTantidiag  -> 0 
    Baxter_RevTacc       -> 0 
    Baxter_RevTder       -> 0 
    Baxter_RevEvenSum    -> 0 
    Baxter_RevOddSum     -> 0 
    Baxter_RevAntiDSum   -> 0 
    Baxter_RevColMiddle  -> 0 
    Baxter_RevCentralO   -> 0 
    Baxter_RevNegHalf    -> 0 
    Baxter_RevTransNat0  -> 0 
    Baxter_RevTransSqrs  -> 0 
    Baxter_RevPolyDiag   -> 0 
    Baxter_TablCol0      -> https://oeis.org/A7
    Baxter_TablCol1      -> https://oeis.org/A12
    Baxter_TablDiag0     -> https://oeis.org/A12
    Baxter_RevPolyRow1   -> https://oeis.org/A12
    Baxter_PolyRow1      -> https://oeis.org/A27
    Baxter_RevPolyRow2   -> https://oeis.org/A27
    Baxter_TablCol2      -> https://oeis.org/A292
    Baxter_TablDiag1     -> https://oeis.org/A292
    Baxter_TablSum       -> https://oeis.org/A1181
    Baxter_AbsSum        -> https://oeis.org/A1181
    Baxter_PolyRow2      -> https://oeis.org/A2378
    Baxter_TablCol3      -> https://oeis.org/A6542
    Baxter_TablDiag2     -> https://oeis.org/A6542
    Baxter_RevPolyRow3   -> https://oeis.org/A28872
    Baxter_TablDiag3     -> https://oeis.org/A47819
    Baxter_Toff11        -> https://oeis.org/A56939
    Baxter_Trev11        -> https://oeis.org/A56939
    Baxter_AccSum        -> https://oeis.org/A350265
    Baxter_TransNat0     -> https://oeis.org/A350265
    Baxter_RevAccRevSum  -> https://oeis.org/A350265
    Baxter_RevTransNat1  -> https://oeis.org/A350265
    Baxter_Triangle      -> https://oeis.org/A359363
    Baxter_Trev          -> https://oeis.org/A359363
    Baxter_Talt          -> https://oeis.org/A359363
    Baxter_RevTalt       -> https://oeis.org/A359363
    Baxter_PosHalf       -> https://oeis.org/A368708
    Baxter_NegHalf       -> https://oeis.org/A368709
    Baxter_RevPolyCol3   -> https://oeis.org/A368733

    Baxter: Distinct: 16, Hits: 28, Misses: 39
'''
