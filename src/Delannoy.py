from functools import cache
from _tabltypes import Table

"""Delannoy triangle.

[0] [1]
[1] [1,  1]
[2] [1,  3,   1]
[3] [1,  5,   5,   1]
[4] [1,  7,  13,   7,   1]
[5] [1,  9,  25,  25,   9,   1]
[6] [1, 11,  41,  63,  41,  11,   1]
[7] [1, 13,  61, 129, 129,  61,  13,   1]
[8] [1, 15,  85, 231, 321, 231,  85,  15,  1]
[9] [1, 17, 113, 377, 681, 681, 377, 113, 17, 1]
"""


@cache
def delannoy(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    rov = delannoy(n - 2)
    row = delannoy(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + rov[k - 1]
    return row


Delannoy = Table(
    delannoy,
    "Delannoy",
    ["A008288"],
    "A132372",
    r"\text{Hyper}([-k, k - n], [1], 2)",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Delannoy)


''' OEIS
    Delannoy_Toff11        -> 0 
    Delannoy_Trev11        -> 0 
    Delannoy_Tinv11        -> 0 
    Delannoy_Trevinv11     -> 0 
    Delannoy_Tantidiag     -> 0 
    Delannoy_Tacc          -> 0 
    Delannoy_Tder          -> 0 
    Delannoy_TablLcm       -> 0 
    Delannoy_OddSum        -> 0 
    Delannoy_TransSqrs     -> 0 
    Delannoy_PolyRow3      -> 0 
    Delannoy_RevToff11     -> 0 
    Delannoy_RevTrev11     -> 0 
    Delannoy_RevTinv11     -> 0 
    Delannoy_RevTantidiag  -> 0 
    Delannoy_RevTacc       -> 0 
    Delannoy_RevTder       -> 0 
    Delannoy_RevOddSum     -> 0 
    Delannoy_RevTransSqrs  -> 0 
    Delannoy_RevPolyRow3   -> 0 
    Delannoy_TablCol0      -> https://oeis.org/A12
    Delannoy_TablDiag0     -> https://oeis.org/A12
    Delannoy_PolyRow1      -> https://oeis.org/A27
    Delannoy_RevPolyRow1   -> https://oeis.org/A27
    Delannoy_AntiDSum      -> https://oeis.org/A73
    Delannoy_RevAntiDSum   -> https://oeis.org/A73
    Delannoy_TablSum       -> https://oeis.org/A129
    Delannoy_AbsSum        -> https://oeis.org/A129
    Delannoy_TablCol2      -> https://oeis.org/A1844
    Delannoy_TablDiag2     -> https://oeis.org/A1844
    Delannoy_TablCol3      -> https://oeis.org/A1845
    Delannoy_TablDiag3     -> https://oeis.org/A1845
    Delannoy_CentralE      -> https://oeis.org/A1850
    Delannoy_CentralO      -> https://oeis.org/A2002
    Delannoy_RevCentralO   -> https://oeis.org/A2002
    Delannoy_TablCol1      -> https://oeis.org/A5408
    Delannoy_TablDiag1     -> https://oeis.org/A5408
    Delannoy_BinConv       -> https://oeis.org/A6139
    Delannoy_PosHalf       -> https://oeis.org/A7482
    Delannoy_PolyCol2      -> https://oeis.org/A7482
    Delannoy_RevPosHalf    -> https://oeis.org/A7482
    Delannoy_Triangle      -> https://oeis.org/A8288
    Delannoy_Trev          -> https://oeis.org/A8288
    Delannoy_Talt          -> https://oeis.org/A8288
    Delannoy_RevTalt       -> https://oeis.org/A8288
    Delannoy_PolyCol3      -> https://oeis.org/A15530
    Delannoy_RevPolyCol3   -> https://oeis.org/A15530
    Delannoy_TablMax       -> https://oeis.org/A26003
    Delannoy_ColMiddle     -> https://oeis.org/A26003
    Delannoy_RevColMiddle  -> https://oeis.org/A26003
    Delannoy_AccSum        -> https://oeis.org/A26937
    Delannoy_AccRevSum     -> https://oeis.org/A26937
    Delannoy_TransNat1     -> https://oeis.org/A26937
    Delannoy_RevAccRevSum  -> https://oeis.org/A26937
    Delannoy_RevTransNat1  -> https://oeis.org/A26937
    Delannoy_PolyRow2      -> https://oeis.org/A28387
    Delannoy_RevPolyRow2   -> https://oeis.org/A28387
    Delannoy_Trevinv       -> https://oeis.org/A33878
    Delannoy_AltSum        -> https://oeis.org/A56594
    Delannoy_InvBinConv    -> https://oeis.org/A59304
    Delannoy_NegHalf       -> https://oeis.org/A77020
    Delannoy_RevNegHalf    -> https://oeis.org/A77020
    Delannoy_EvenSum       -> https://oeis.org/A116404
    Delannoy_RevEvenSum    -> https://oeis.org/A116404
    Delannoy_Tinv          -> https://oeis.org/A132372
    Delannoy_Tinvrev       -> https://oeis.org/A132372
    Delannoy_TransNat0     -> https://oeis.org/A364553
    Delannoy_RevTransNat0  -> https://oeis.org/A364553
    Delannoy_TablGcd       -> https://oeis.org/A372443
    Delannoy_PolyDiag      -> https://oeis.org/A376871
    Delannoy_RevPolyDiag   -> https://oeis.org/A376871

    Delannoy: Distinct: 26, Hits: 51, Misses: 20
'''
