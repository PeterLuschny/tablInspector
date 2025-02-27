from functools import cache
from _tabltypes import Table

"""Schroeder bilateral paths.

[0]     1;
[1]     2,     1;
[2]     6,     6,     1;
[3]    20,    30,    12,     1;
[4]    70,   140,    90,    20,     1;
[5]   252,   630,   560,   210,    30,    1;
[6]   924,  2772,  3150,  1680,   420,   42,    1;
[7]  3432, 12012, 16632, 11550,  4200,  756,   56,  1;
[8] 12870, 51480, 84084, 72072, 34650, 9240, 1260, 72, 1;
"""


@cache
def schroederp(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = schroederp(n - 1) + [1]

    for k in range(n, 0, -1):
        row[k] = (row[k - 1] * (2 * n - k)) // k
    row[0] = (row[0] * (4 * n - 2)) // n

    return row


SchroederP = Table(
    schroederp,
    "SchroederP",
    ["A104684", "A063007"],
    "A000000",
    r"\binom{n}{k} \binom{2n - k}{n}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(SchroederP)






''' OEIS
    SchroederP_Tinv          -> 0 
    SchroederP_Trevinv       -> 0 
    SchroederP_Toff11        -> 0 
    SchroederP_Trev11        -> 0 
    SchroederP_Tinv11        -> 0 
    SchroederP_Trevinv11     -> 0 
    SchroederP_Tantidiag     -> 0 
    SchroederP_Tacc          -> 0 
    SchroederP_Tder          -> 0 
    SchroederP_TablLcm       -> 0 
    SchroederP_TablGcd       -> 0 
    SchroederP_TablMax       -> 0 
    SchroederP_AccSum        -> 0 
    SchroederP_AccRevSum     -> 0 
    SchroederP_ColMiddle     -> 0 
    SchroederP_TransNat1     -> 0 
    SchroederP_TransSqrs     -> 0 
    SchroederP_InvBinConv    -> 0 
    SchroederP_PolyRow3      -> 0 
    SchroederP_RevToff11     -> 0 
    SchroederP_RevTrev11     -> 0 
    SchroederP_RevTantidiag  -> 0 
    SchroederP_RevTacc       -> 0 
    SchroederP_RevTder       -> 0 
    SchroederP_RevEvenSum    -> 0 
    SchroederP_RevOddSum     -> 0 
    SchroederP_RevAccRevSum  -> 0 
    SchroederP_RevColMiddle  -> 0 
    SchroederP_RevCentralO   -> 0 
    SchroederP_RevTransNat0  -> 0 
    SchroederP_RevTransNat1  -> 0 
    SchroederP_RevTransSqrs  -> 0 
    SchroederP_TablDiag0     -> https://oeis.org/A12
    SchroederP_AltSum        -> https://oeis.org/A12
    SchroederP_PolyRow1      -> https://oeis.org/A27
    SchroederP_TablCol0      -> https://oeis.org/A984
    SchroederP_TablSum       -> https://oeis.org/A1850
    SchroederP_AbsSum        -> https://oeis.org/A1850
    SchroederP_NegHalf       -> https://oeis.org/A1850
    SchroederP_TablDiag1     -> https://oeis.org/A2378
    SchroederP_RevAntiDSum   -> https://oeis.org/A2426
    SchroederP_TablCol1      -> https://oeis.org/A2457
    SchroederP_TablCol2      -> https://oeis.org/A2544
    SchroederP_RevPolyRow2   -> https://oeis.org/A3154
    SchroederP_BinConv       -> https://oeis.org/A5258
    SchroederP_RevPolyRow1   -> https://oeis.org/A5408
    SchroederP_PosHalf       -> https://oeis.org/A6442
    SchroederP_CentralE      -> https://oeis.org/A6480
    SchroederP_TablCol3      -> https://oeis.org/A7744
    SchroederP_PolyRow2      -> https://oeis.org/A28872
    SchroederP_TablDiag2     -> https://oeis.org/A33487
    SchroederP_OddSum        -> https://oeis.org/A47665
    SchroederP_Trev          -> https://oeis.org/A63007
    SchroederP_RevTalt       -> https://oeis.org/A63007
    SchroederP_PolyCol2      -> https://oeis.org/A69835
    SchroederP_RevPosHalf    -> https://oeis.org/A69835
    SchroederP_RevPolyCol3   -> https://oeis.org/A84768
    SchroederP_PolyCol3      -> https://oeis.org/A84771
    SchroederP_Triangle      -> https://oeis.org/A104684
    SchroederP_Talt          -> https://oeis.org/A104684
    SchroederP_TablDiag3     -> https://oeis.org/A105939
    SchroederP_TransNat0     -> https://oeis.org/A108666
    SchroederP_RevNegHalf    -> https://oeis.org/A126869
    SchroederP_RevPolyRow3   -> https://oeis.org/A160674
    SchroederP_CentralO      -> https://oeis.org/A208881
    SchroederP_EvenSum       -> https://oeis.org/A226994
    SchroederP_RevPolyDiag   -> https://oeis.org/A331656
    SchroederP_PolyDiag      -> https://oeis.org/A335309
    SchroederP_AntiDSum      -> https://oeis.org/A349713

    SchroederP: Distinct: 32, Hits: 37, Misses: 32
'''
