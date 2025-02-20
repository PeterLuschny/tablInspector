from functools import cache
from _tabltypes import Table

"""Ward set numbers.


[0] [1]
[1] [0, 1]
[2] [0, 1,   3]
[3] [0, 1,  10,    15]
[4] [0, 1,  25,   105,    105]
[5] [0, 1,  56,   490,   1260,     945]
[6] [0, 1, 119,  1918,   9450,   17325,   10395]
[7] [0, 1, 246,  6825,  56980,  190575,  270270,  135135]
[8] [0, 1, 501, 22935, 302995, 1636635, 4099095, 4729725, 2027025]
"""


@cache
def wardset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = wardset(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = k * row[k] + (n + k - 1) * row[k - 1]

    return row


WardSet = Table(
    wardset,
    "WardSet",
    ["A269939", "A134991"],
    "",
    r"\sum_{m=0}^{k} (-1)^{m + k} \binom{n+k}{n+m} { n + m \brace m}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(WardSet)






''' OEIS
    WardSet_Trev          -> 0 
    WardSet_Tinvrev11     -> 0 
    WardSet_Tacc          -> 0 
    WardSet_Tder          -> 0 
    WardSet_TablLcm       -> 0 
    WardSet_TablMax       -> 0 
    WardSet_EvenSum       -> 0 
    WardSet_OddSum        -> 0 
    WardSet_AccSum        -> 0 
    WardSet_AccRevSum     -> 0 
    WardSet_ColMiddle     -> 0 
    WardSet_CentralE      -> 0 
    WardSet_CentralO      -> 0 
    WardSet_PosHalf       -> 0 
    WardSet_TransNat0     -> 0 
    WardSet_TransNat1     -> 0 
    WardSet_TransSqrs     -> 0 
    WardSet_BinConv       -> 0 
    WardSet_InvBinConv    -> 0 
    WardSet_PolyRow3      -> 0 
    WardSet_PolyDiag      -> 0 
    WardSet_RevToff11     -> 0 
    WardSet_RevTrev11     -> 0 
    WardSet_RevTantidiag  -> 0 
    WardSet_RevTacc       -> 0 
    WardSet_RevTalt       -> 0 
    WardSet_RevTder       -> 0 
    WardSet_RevEvenSum    -> 0 
    WardSet_RevOddSum     -> 0 
    WardSet_RevAccRevSum  -> 0 
    WardSet_RevAntiDSum   -> 0 
    WardSet_RevColMiddle  -> 0 
    WardSet_RevCentralO   -> 0 
    WardSet_RevTransNat0  -> 0 
    WardSet_RevTransNat1  -> 0 
    WardSet_RevTransSqrs  -> 0 
    WardSet_RevPolyRow3   -> 0 
    WardSet_RevPolyCol3   -> 0 
    WardSet_RevPolyDiag   -> 0 
    WardSet_TablCol0      -> https://oeis.org/A7
    WardSet_TablCol1      -> https://oeis.org/A12
    WardSet_RevPolyRow1   -> https://oeis.org/A12
    WardSet_PolyRow1      -> https://oeis.org/A27
    WardSet_RevPolyRow2   -> https://oeis.org/A27
    WardSet_AltSum        -> https://oeis.org/A142
    WardSet_TablCol2      -> https://oeis.org/A247
    WardSet_AntiDSum      -> https://oeis.org/A296
    WardSet_TablSum       -> https://oeis.org/A311
    WardSet_AbsSum        -> https://oeis.org/A311
    WardSet_TablDiag1     -> https://oeis.org/A457
    WardSet_TablCol3      -> https://oeis.org/A478
    WardSet_TablDiag2     -> https://oeis.org/A497
    WardSet_TablDiag3     -> https://oeis.org/A504
    WardSet_TablDiag0     -> https://oeis.org/A1147
    WardSet_NegHalf       -> https://oeis.org/A1662
    WardSet_PolyRow2      -> https://oeis.org/A49451
    WardSet_TablGcd       -> https://oeis.org/A110560
    WardSet_RevNegHalf    -> https://oeis.org/A112487
    WardSet_Toff11        -> https://oeis.org/A134991
    WardSet_Tantidiag     -> https://oeis.org/A137375
    WardSet_Trev11        -> https://oeis.org/A181996
    WardSet_PolyCol2      -> https://oeis.org/A201465
    WardSet_RevPosHalf    -> https://oeis.org/A201465
    WardSet_PolyCol3      -> https://oeis.org/A201466
    WardSet_Triangle      -> https://oeis.org/A269939
    WardSet_Talt          -> https://oeis.org/A269939

    WardSet: Distinct: 23, Hits: 27, Misses: 39
'''
