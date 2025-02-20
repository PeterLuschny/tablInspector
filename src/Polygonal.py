from functools import cache
from _tabltypes import Table

"""Polygonal numbers.

[0 ] Nonnegatives . A001477: 0,  1,  2,  3,  4,   5,   6,   7, ...
[1 ] Triangulars .. A000217: 0,  1,  3,  6, 10,  15,  21,  28, ...
[2 ] Squares ...... A000290: 0,  1,  4,  9, 16,  25,  36,  49, ...
[3 ] Pentagonals .. A000326: 0,  1,  5, 12, 22,  35,  51,  70, ...
[4 ] Hexagonals ... A000384: 0,  1,  6, 15, 28,  45,  66,  91, ...
[5 ] Heptagonals .. A000566: 0,  1,  7, 18, 34,  55,  81, 112, ...
[6 ] Octagonals ... A000567: 0,  1,  8, 21, 40,  65,  96, 133, ...
[7 ] 9-gonals ..... A001106: 0,  1,  9, 24, 46,  75, 111, 154, ...
[8 ] 10-gonals .... A001107: 0,  1, 10, 27, 52,  85, 126, 175, ...
[9 ] 11-gonals .... A051682: 0,  1, 11, 30, 58,  95, 141, 196, ...
[10] 12-gonals .... A051624: 0,  1, 12, 33, 64, 105, 156, 217, ...


Triangle view:
[0] [0]
[1] [0, 1]
[2] [0, 1, 2]
[3] [0, 1, 3,  3]
[4] [0, 1, 4,  6,  4]
[5] [0, 1, 5,  9, 10,  5]
[6] [0, 1, 6, 12, 16, 15,  6]
[7] [0, 1, 7, 15, 22, 25, 21, 7]
"""


@cache
def polygonal(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]

    rov = polygonal(n - 2)
    row = polygonal(n - 1) + [n]
    row[n - 1] += row[n - 2]
    for k in range(2, n - 1):
        row[k] += row[k] - rov[k]
    return row


Polygonal = Table(
    polygonal,
    "Polygonal",
    ["A139600", "A057145", "A134394", "A139601"],
    "",
    r"k + \frac{1}{2}\, n\, k\, (k-1)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Polygonal)






''' OEIS
    Polygonal_Trev          -> 0 
    Polygonal_Tinvrev11     -> 0 
    Polygonal_Tantidiag     -> 0 
    Polygonal_Tacc          -> 0 
    Polygonal_Tder          -> 0 
    Polygonal_TablLcm       -> 0 
    Polygonal_TablMax       -> 0 
    Polygonal_EvenSum       -> 0 
    Polygonal_OddSum        -> 0 
    Polygonal_AltSum        -> 0 
    Polygonal_AccSum        -> 0 
    Polygonal_AccRevSum     -> 0 
    Polygonal_AntiDSum      -> 0 
    Polygonal_ColMiddle     -> 0 
    Polygonal_TransNat0     -> 0 
    Polygonal_TransNat1     -> 0 
    Polygonal_TransSqrs     -> 0 
    Polygonal_BinConv       -> 0 
    Polygonal_PolyCol2      -> 0 
    Polygonal_PolyCol3      -> 0 
    Polygonal_PolyDiag      -> 0 
    Polygonal_RevToff11     -> 0 
    Polygonal_RevTantidiag  -> 0 
    Polygonal_RevTacc       -> 0 
    Polygonal_RevTalt       -> 0 
    Polygonal_RevTder       -> 0 
    Polygonal_RevEvenSum    -> 0 
    Polygonal_RevOddSum     -> 0 
    Polygonal_RevAccRevSum  -> 0 
    Polygonal_RevAntiDSum   -> 0 
    Polygonal_RevColMiddle  -> 0 
    Polygonal_RevPosHalf    -> 0 
    Polygonal_RevNegHalf    -> 0 
    Polygonal_RevTransNat0  -> 0 
    Polygonal_RevTransNat1  -> 0 
    Polygonal_RevTransSqrs  -> 0 
    Polygonal_RevPolyCol3   -> 0 
    Polygonal_RevPolyDiag   -> 0 
    Polygonal_TablCol0      -> https://oeis.org/A4
    Polygonal_TablCol1      -> https://oeis.org/A12
    Polygonal_RevPolyRow1   -> https://oeis.org/A12
    Polygonal_TablCol2      -> https://oeis.org/A27
    Polygonal_TablDiag0     -> https://oeis.org/A27
    Polygonal_PolyRow1      -> https://oeis.org/A27
    Polygonal_RevPolyRow2   -> https://oeis.org/A27
    Polygonal_TablDiag1     -> https://oeis.org/A217
    Polygonal_TablDiag2     -> https://oeis.org/A290
    Polygonal_TablDiag3     -> https://oeis.org/A326
    Polygonal_RevPolyRow3   -> https://oeis.org/A2061
    Polygonal_CentralE      -> https://oeis.org/A6000
    Polygonal_CentralO      -> https://oeis.org/A6003
    Polygonal_TablCol3      -> https://oeis.org/A8585
    Polygonal_PolyRow2      -> https://oeis.org/A14105
    Polygonal_TablSum       -> https://oeis.org/A55795
    Polygonal_AbsSum        -> https://oeis.org/A55795
    Polygonal_Toff11        -> https://oeis.org/A57145
    Polygonal_RevCentralO   -> https://oeis.org/A64808
    Polygonal_InvBinConv    -> https://oeis.org/A80300
    Polygonal_TablGcd       -> https://oeis.org/A114890
    Polygonal_Trev11        -> https://oeis.org/A134394
    Polygonal_Triangle      -> https://oeis.org/A139600
    Polygonal_Talt          -> https://oeis.org/A139600
    Polygonal_RevTrev11     -> https://oeis.org/A139601
    Polygonal_PolyRow3      -> https://oeis.org/A249354
    Polygonal_NegHalf       -> https://oeis.org/A360605
    Polygonal_PosHalf       -> https://oeis.org/A360606

    Polygonal: Distinct: 23, Hits: 28, Misses: 38
'''
