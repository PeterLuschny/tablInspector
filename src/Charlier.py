from functools import cache
from _tabltypes import Table

"""Coefficients of Charlier polynomials.

[0] [1]
[1] [1, -1]
[2] [1, -3, 1]
[3] [1, -6, 8, -1]
[4] [1, -10, 29, -24, 1]
[5] [1, -15, 75, -145, 89, -1]
[6] [1, -21, 160, -545, 814, -415, 1]
[7] [1, -28, 301, -1575, 4179, -5243, 2372, -1]
[8] [1, -36, 518, -3836, 15659, -34860, 38618, -16072, 1]
"""


@cache
def charlier(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, -1]

    a = charlier(n - 1)
    b = [0] + charlier(n - 2)
    c = charlier(n - 1) + [(-1) ** n]

    for k in range(1, n):
        c[k] = a[k] - n * a[k - 1] - (n - 1) * b[k - 1]

    return c


Charlier = Table(
    charlier,
    "Charlier",
    ["A046716", "A094816"],
    "A000000",
    r"\sum_{j=0}^{k} (-1)^k \, \binom{n}{k-j}\,{j+n-k \brack n-k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Charlier)


''' OEIS
    Charlier_Tinv          -> 0 
    Charlier_Toff11        -> 0 
    Charlier_Trev11        -> 0 
    Charlier_Tinv11        -> 0 
    Charlier_Tantidiag     -> 0 
    Charlier_Tacc          -> 0 
    Charlier_Tder          -> 0 
    Charlier_TablDiag2     -> 0 
    Charlier_TablDiag3     -> 0 
    Charlier_TablLcm       -> 0 
    Charlier_TablMax       -> 0 
    Charlier_EvenSum       -> 0 
    Charlier_OddSum        -> 0 
    Charlier_AccSum        -> 0 
    Charlier_AccRevSum     -> 0 
    Charlier_AntiDSum      -> 0 
    Charlier_ColMiddle     -> 0 
    Charlier_CentralE      -> 0 
    Charlier_CentralO      -> 0 
    Charlier_TransNat0     -> 0 
    Charlier_TransNat1     -> 0 
    Charlier_TransSqrs     -> 0 
    Charlier_BinConv       -> 0 
    Charlier_InvBinConv    -> 0 
    Charlier_PolyRow3      -> 0 
    Charlier_PolyCol2      -> 0 
    Charlier_PolyCol3      -> 0 
    Charlier_PolyDiag      -> 0 
    Charlier_RevToff11     -> 0 
    Charlier_RevTrev11     -> 0 
    Charlier_RevTinv11     -> 0 
    Charlier_RevTantidiag  -> 0 
    Charlier_RevTacc       -> 0 
    Charlier_RevTder       -> 0 
    Charlier_RevAccRevSum  -> 0 
    Charlier_RevAntiDSum   -> 0 
    Charlier_RevColMiddle  -> 0 
    Charlier_RevCentralO   -> 0 
    Charlier_RevTransNat0  -> 0 
    Charlier_RevTransNat1  -> 0 
    Charlier_RevTransSqrs  -> 0 
    Charlier_RevPolyRow3   -> 0 
    Charlier_RevPolyCol3   -> 0 
    Charlier_TablCol0      -> https://oeis.org/A12
    Charlier_TablDiag0     -> https://oeis.org/A12
    Charlier_TablSum       -> https://oeis.org/A27
    Charlier_PolyRow1      -> https://oeis.org/A27
    Charlier_RevPolyRow1   -> https://oeis.org/A27
    Charlier_TablCol1      -> https://oeis.org/A217
    Charlier_AltSum        -> https://oeis.org/A522
    Charlier_AbsSum        -> https://oeis.org/A522
    Charlier_NegHalf       -> https://oeis.org/A1339
    Charlier_TablDiag1     -> https://oeis.org/A2104
    Charlier_RevEvenSum    -> https://oeis.org/A9132
    Charlier_RevOddSum     -> https://oeis.org/A9578
    Charlier_RevPolyDiag   -> https://oeis.org/A9940
    Charlier_PosHalf       -> https://oeis.org/A28387
    Charlier_PolyRow2      -> https://oeis.org/A28387
    Charlier_RevPolyRow2   -> https://oeis.org/A28387
    Charlier_Triangle      -> https://oeis.org/A46716
    Charlier_Talt          -> https://oeis.org/A46716
    Charlier_Tinvrev       -> https://oeis.org/A49020
    Charlier_RevNegHalf    -> https://oeis.org/A81367
    Charlier_Trev          -> https://oeis.org/A94816
    Charlier_RevTalt       -> https://oeis.org/A94816
    Charlier_TablGcd       -> https://oeis.org/A174965
    Charlier_TablCol2      -> https://oeis.org/A290312
    Charlier_TablCol3      -> https://oeis.org/A290313

    Charlier: Distinct: 18, Hits: 25, Misses: 43
'''
