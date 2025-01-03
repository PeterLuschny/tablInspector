from functools import cache
from _tabltypes import Table

"""Schroeder triangle.

[0] [1]
[1] [0,     1]
[2] [0,     2,     1]
[3] [0,     6,     4,     1]
[4] [0,    22,    16,     6,    1]
[5] [0,    90,    68,    30,    8,    1]
[6] [0,   394,   304,   146,   48,   10,   1]
[7] [0,  1806,  1412,   714,  264,   70,  12,   1]
[8] [0,  8558,  6752,  3534, 1408,  430,  96,  14,  1]
[9] [0, 41586, 33028, 17718, 7432, 2490, 652, 126, 16, 1]
"""


@cache
def schroeder(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = schroeder(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + row[k + 1]

    return row


Schroeder = Table(
    schroeder,
    "Schroeder",
    ["A122538", "A033877", "A080245", "A080247", "A106579"],
    "A000000",
    r"is(k = 0)\ ? \ 0^{n} : T(n-1,k-1)+T(n-1,k)+T(n,k+1)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Schroeder)


''' OEIS
    Schroeder_Tantidiag     -> 0 
    Schroeder_Tacc          -> 0 
    Schroeder_Tder          -> 0 
    Schroeder_TablDiag3     -> 0 
    Schroeder_TablLcm       -> 0 
    Schroeder_AccSum        -> 0 
    Schroeder_ColMiddle     -> 0 
    Schroeder_CentralO      -> 0 
    Schroeder_PolyRow3      -> 0 
    Schroeder_PolyCol3      -> 0 
    Schroeder_PolyDiag      -> 0 
    Schroeder_RevToff11     -> 0 
    Schroeder_RevTrev11     -> 0 
    Schroeder_RevTantidiag  -> 0 
    Schroeder_RevTder       -> 0 
    Schroeder_RevOddSum     -> 0 
    Schroeder_RevAccRevSum  -> 0 
    Schroeder_RevColMiddle  -> 0 
    Schroeder_RevNegHalf    -> 0 
    Schroeder_RevTransNat0  -> 0 
    Schroeder_RevTransNat1  -> 0 
    Schroeder_RevTransSqrs  -> 0 
    Schroeder_RevPolyCol3   -> 0 
    Schroeder_RevPolyDiag   -> 0 
    Schroeder_TablCol0      -> https://oeis.org/A7
    Schroeder_TablDiag0     -> https://oeis.org/A12
    Schroeder_RevPolyRow1   -> https://oeis.org/A12
    Schroeder_PolyRow1      -> https://oeis.org/A27
    Schroeder_InvBinConv    -> https://oeis.org/A225
    Schroeder_TablSum       -> https://oeis.org/A1003
    Schroeder_AltSum        -> https://oeis.org/A1003
    Schroeder_AbsSum        -> https://oeis.org/A1003
    Schroeder_RevPolyRow2   -> https://oeis.org/A5408
    Schroeder_PolyRow2      -> https://oeis.org/A5563
    Schroeder_TablDiag1     -> https://oeis.org/A5843
    Schroeder_TablCol1      -> https://oeis.org/A6318
    Schroeder_TablMax       -> https://oeis.org/A6318
    Schroeder_TablCol2      -> https://oeis.org/A6319
    Schroeder_TablCol3      -> https://oeis.org/A6320
    Schroeder_AntiDSum      -> https://oeis.org/A6603
    Schroeder_OddSum        -> https://oeis.org/A10683
    Schroeder_AccRevSum     -> https://oeis.org/A10683
    Schroeder_TransNat1     -> https://oeis.org/A10683
    Schroeder_RevAntiDSum   -> https://oeis.org/A26003
    Schroeder_Trev11        -> https://oeis.org/A33877
    Schroeder_TablDiag2     -> https://oeis.org/A54000
    Schroeder_TablGcd       -> https://oeis.org/A55642
    Schroeder_TransSqrs     -> https://oeis.org/A65096
    Schroeder_Toff11        -> https://oeis.org/A80247
    Schroeder_RevPolyRow3   -> https://oeis.org/A80859
    Schroeder_CentralE      -> https://oeis.org/A103885
    Schroeder_Trev          -> https://oeis.org/A106579
    Schroeder_RevTalt       -> https://oeis.org/A106579
    Schroeder_PolyCol2      -> https://oeis.org/A109980
    Schroeder_Tinv11        -> https://oeis.org/A113413
    Schroeder_Triangle      -> https://oeis.org/A122538
    Schroeder_Talt          -> https://oeis.org/A122538
    Schroeder_Tinv          -> https://oeis.org/A122542
    Schroeder_RevTacc       -> https://oeis.org/A144944
    Schroeder_BinConv       -> https://oeis.org/A178792
    Schroeder_RevEvenSum    -> https://oeis.org/A227506
    Schroeder_EvenSum       -> https://oeis.org/A239204
    Schroeder_TransNat0     -> https://oeis.org/A239204
    Schroeder_RevCentralO   -> https://oeis.org/A330801
    Schroeder_PosHalf       -> https://oeis.org/A330802
    Schroeder_NegHalf       -> https://oeis.org/A330803

    Schroeder: Distinct: 34, Hits: 42, Misses: 24
'''
