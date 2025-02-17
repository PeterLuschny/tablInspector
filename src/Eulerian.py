from functools import cache
from _tabltypes import Table

"""Eulerian triangle.

0:  1
1:  0 1
2:  0 1    1
3:  0 1    4     1
4:  0 1   11    11      1
5:  0 1   26    66     26       1
6:  0 1   57   302    302      57       1
7:  0 1  120  1191   2416    1191     120      1
8:  0 1  247  4293  15619   15619    4293    247     1

# Knuth's version is row reversed: ======================

[0]  1,
[1]  1,    0,
[2]  1,    1,     0,
[3]  1,    4,     1,      0,
[4]  1,   11,    11,      1,      0,
[5]  1,   26,    66,     26,      1,    0,
[6]  1,   57,   302,    302,     57,    1,   0,
[7]  1,  120,  1191,   2416,   1191,  120,   1,  0,
[8]  1,  247,  4293,  15619,  15619, 4293, 247,  1,  0
"""

@cache
def KnuthEulerian(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = KnuthEulerian(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n - k) * row[k - 1] + (k + 1) * row[k]
    return row


@cache
def eulerian(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = eulerian(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (n - k + 1) * row[k - 1] + k * row[k]
    return row


Eulerian = Table(
    eulerian,
    "Eulerian",
    ["A173018", "A123125", "A008292"],
    "A055325", # Inv of the A008292 version.
    r"\sum_{j=0}^{k} (-1)^{j} \binom{n+1}{j} (k+1-j)^{n}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Eulerian)




''' OEIS
    Eulerian_Tinv          -> 0 
    Eulerian_Trevinv       -> 0 
    Eulerian_Trevinv11     -> 0 
    Eulerian_Tantidiag     -> 0 
    Eulerian_Tacc          -> 0 
    Eulerian_TablGcd       -> 0 
    Eulerian_ColMiddle     -> 0 
    Eulerian_CentralO      -> 0 
    Eulerian_TransSqrs     -> 0 
    Eulerian_PolyRow3      -> 0 
    Eulerian_RevToff11     -> 0 
    Eulerian_RevTrev11     -> 0 
    Eulerian_RevTacc       -> 0 
    Eulerian_RevTder       -> 0 
    Eulerian_TablCol0      -> https://oeis.org/A7
    Eulerian_TablCol1      -> https://oeis.org/A12
    Eulerian_TablDiag0     -> https://oeis.org/A12
    Eulerian_RevPolyRow1   -> https://oeis.org/A12
    Eulerian_PolyRow1      -> https://oeis.org/A27
    Eulerian_RevPolyRow2   -> https://oeis.org/A27
    Eulerian_TablSum       -> https://oeis.org/A142
    Eulerian_AbsSum        -> https://oeis.org/A142
    Eulerian_TablCol2      -> https://oeis.org/A295
    Eulerian_TablDiag1     -> https://oeis.org/A295
    Eulerian_TablCol3      -> https://oeis.org/A460
    Eulerian_TablDiag2     -> https://oeis.org/A460
    Eulerian_TablDiag3     -> https://oeis.org/A498
    Eulerian_PolyCol2      -> https://oeis.org/A629
    Eulerian_RevPosHalf    -> https://oeis.org/A629
    Eulerian_PosHalf       -> https://oeis.org/A670
    Eulerian_AntiDSum      -> https://oeis.org/A800
    Eulerian_RevAntiDSum   -> https://oeis.org/A800
    Eulerian_RevTransNat0  -> https://oeis.org/A1286
    Eulerian_AccSum        -> https://oeis.org/A1710
    Eulerian_TransNat0     -> https://oeis.org/A1710
    Eulerian_RevAccRevSum  -> https://oeis.org/A1710
    Eulerian_RevTransNat1  -> https://oeis.org/A1710
    Eulerian_PolyRow2      -> https://oeis.org/A2378
    Eulerian_TablMax       -> https://oeis.org/A6551
    Eulerian_RevColMiddle  -> https://oeis.org/A6551
    Eulerian_Toff11        -> https://oeis.org/A8292
    Eulerian_Trev11        -> https://oeis.org/A8292
    Eulerian_AltSum        -> https://oeis.org/A9006
    Eulerian_BinConv       -> https://oeis.org/A11818
    Eulerian_RevCentralO   -> https://oeis.org/A25585
    Eulerian_RevPolyRow3   -> https://oeis.org/A28872
    Eulerian_AccRevSum     -> https://oeis.org/A38720
    Eulerian_TransNat1     -> https://oeis.org/A38720
    Eulerian_Tder          -> https://oeis.org/A65826
    Eulerian_PolyDiag      -> https://oeis.org/A122020
    Eulerian_RevPolyCol3   -> https://oeis.org/A122704
    Eulerian_RevPolyDiag   -> https://oeis.org/A122778
    Eulerian_PolyCol3      -> https://oeis.org/A123227
    Eulerian_OddSum        -> https://oeis.org/A128103
    Eulerian_RevEvenSum    -> https://oeis.org/A128103
    Eulerian_Tinv11        -> https://oeis.org/A162498
    Eulerian_Tinvrev11     -> https://oeis.org/A162498
    Eulerian_Triangle      -> https://oeis.org/A173018
    Eulerian_Trev          -> https://oeis.org/A173018
    Eulerian_Talt          -> https://oeis.org/A173018
    Eulerian_RevTalt       -> https://oeis.org/A173018
    Eulerian_RevNegHalf    -> https://oeis.org/A179929
    Eulerian_CentralE      -> https://oeis.org/A180056
    Eulerian_TablLcm       -> https://oeis.org/A180057
    Eulerian_NegHalf       -> https://oeis.org/A212846
    Eulerian_EvenSum       -> https://oeis.org/A262745
    Eulerian_RevOddSum     -> https://oeis.org/A262745
    Eulerian_InvBinConv    -> https://oeis.org/A344052
    Eulerian_RevTransSqrs  -> https://oeis.org/A344054
    Eulerian_RevTantidiag  -> https://oeis.org/A344393

    Eulerian: Distinct: 37, Hits: 56, Misses: 14
'''
