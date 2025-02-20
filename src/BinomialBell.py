from functools import cache
from _tabltypes import Table

"""
T(n, k) = if k == 0 then 0^n else binomial(n-1, k-1) * Bell(n - k)

[0]     1
[1]     1,    1
[2]     2,    2,    1
[3]     5,    6,    3,    1
[4]    15,   20,   12,    4,    1
[5]    52,   75,   50,   20,    5,   1
[6]   203,  312,  225,  100,   30,   6,  1
[7]   877, 1421, 1092,  525,  175,  42,  7, 1
[8]  4140, 7016, 5684, 2912, 1050, 280, 56, 8, 1
"""


@cache
def binomialbell(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    a = binomialbell(n - 1) + [1]
    s = sum(a) - 1

    for j in range(n - 1, 0, -1):
        a[j] = (a[j - 1] * n) // j
    a[0] = s

    return a


BinomialBell = Table(
    binomialbell,
    "BinomialBell",
    ["A056857", "A056860"],
    "",  # not invertible
    r"\binom{n}{k} \text{Bell}(n-k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(BinomialBell)






''' OEIS
    BinomialBell_Trev11        -> 0 
    BinomialBell_Tinv11        -> 0 
    BinomialBell_Trevinv11     -> 0 
    BinomialBell_Tantidiag     -> 0 
    BinomialBell_Tacc          -> 0 
    BinomialBell_Tder          -> 0 
    BinomialBell_TablLcm       -> 0 
    BinomialBell_TablGcd       -> 0 
    BinomialBell_TablMax       -> 0 
    BinomialBell_AccSum        -> 0 
    BinomialBell_AntiDSum      -> 0 
    BinomialBell_ColMiddle     -> 0 
    BinomialBell_BinConv       -> 0 
    BinomialBell_InvBinConv    -> 0 
    BinomialBell_RevToff11     -> 0 
    BinomialBell_RevTrev11     -> 0 
    BinomialBell_RevTantidiag  -> 0 
    BinomialBell_RevTacc       -> 0 
    BinomialBell_RevTder       -> 0 
    BinomialBell_RevEvenSum    -> 0 
    BinomialBell_RevOddSum     -> 0 
    BinomialBell_RevAccRevSum  -> 0 
    BinomialBell_RevColMiddle  -> 0 
    BinomialBell_RevCentralO   -> 0 
    BinomialBell_RevTransNat1  -> 0 
    BinomialBell_RevTransSqrs  -> 0 
    BinomialBell_RevPolyRow3   -> 0 
    BinomialBell_TablDiag0     -> https://oeis.org/A12
    BinomialBell_TablDiag1     -> https://oeis.org/A27
    BinomialBell_PolyRow1      -> https://oeis.org/A27
    BinomialBell_RevPolyRow1   -> https://oeis.org/A27
    BinomialBell_TablCol0      -> https://oeis.org/A110
    BinomialBell_TablSum       -> https://oeis.org/A110
    BinomialBell_AbsSum        -> https://oeis.org/A110
    BinomialBell_AltSum        -> https://oeis.org/A296
    BinomialBell_RevPolyRow2   -> https://oeis.org/A1844
    BinomialBell_TablDiag2     -> https://oeis.org/A2378
    BinomialBell_PolyRow2      -> https://oeis.org/A2522
    BinomialBell_PolyRow3      -> https://oeis.org/A5491
    BinomialBell_PolyCol2      -> https://oeis.org/A5493
    BinomialBell_RevPosHalf    -> https://oeis.org/A5493
    BinomialBell_PolyCol3      -> https://oeis.org/A5494
    BinomialBell_TablCol1      -> https://oeis.org/A52889
    BinomialBell_Triangle      -> https://oeis.org/A56857
    BinomialBell_Talt          -> https://oeis.org/A56857
    BinomialBell_Trev          -> https://oeis.org/A56860
    BinomialBell_RevTalt       -> https://oeis.org/A56860
    BinomialBell_TransNat0     -> https://oeis.org/A70071
    BinomialBell_OddSum        -> https://oeis.org/A102286
    BinomialBell_TablCol2      -> https://oeis.org/A105479
    BinomialBell_TablCol3      -> https://oeis.org/A105480
    BinomialBell_CentralE      -> https://oeis.org/A124102
    BinomialBell_NegHalf       -> https://oeis.org/A124311
    BinomialBell_AccRevSum     -> https://oeis.org/A124427
    BinomialBell_TransNat1     -> https://oeis.org/A124427
    BinomialBell_PosHalf       -> https://oeis.org/A126390
    BinomialBell_RevNegHalf    -> https://oeis.org/A126617
    BinomialBell_RevTransNat0  -> https://oeis.org/A127741
    BinomialBell_TablDiag3     -> https://oeis.org/A134481
    BinomialBell_PolyDiag      -> https://oeis.org/A134980
    BinomialBell_TransSqrs     -> https://oeis.org/A175716
    BinomialBell_Toff11        -> https://oeis.org/A175757
    BinomialBell_RevAntiDSum   -> https://oeis.org/A211694
    BinomialBell_EvenSum       -> https://oeis.org/A224271
    BinomialBell_RevPolyCol3   -> https://oeis.org/A284859
    BinomialBell_CentralO      -> https://oeis.org/A297926
    BinomialBell_RevPolyDiag   -> https://oeis.org/A307066

    BinomialBell: Distinct: 33, Hits: 40, Misses: 27
'''
