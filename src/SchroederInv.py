from functools import cache
from _tabltypes import Table

"""SchroederInv triangle.

 [0] [1],
 [1] [0,  1],
 [2] [0,  2,   1],
 [3] [0,  2,   4,    1],
 [4] [0,  2,   8,    6,   1],
 [5] [0,  2,  12,   18,   8,    1],
 [6] [0,  2,  16,   38,  32,   10,   1],
 [7] [0,  2,  20,   66,  88,   50,  12,   1],
 [8] [0,  2,  24,  102, 192,  170,  72,  14, 1]
"""


@cache
def schroederinv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    arow = schroederinv(n - 2) + [1]
    row = schroederinv(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += row[k - 1] + arow[k - 1]

    return row


SchroederInv = Table(
    schroederinv,
    "SchroederInv",
    ["A122542", "A035607", "A113413", "A119800", "A266213"],
    "",
    r"",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(SchroederInv)

''' OEIS

SchroederInv_Tantidiag     -> 0
    SchroederInv_Tacc          -> 0
    SchroederInv_Tder          -> 0
    SchroederInv_TablLcm       -> 0
    SchroederInv_OddSum        -> 0
    SchroederInv_AccSum        -> 0
    SchroederInv_ColMiddle     -> 0
    SchroederInv_CentralO      -> 0
    SchroederInv_TransSqrs     -> 0
    SchroederInv_InvBinConv    -> 0
    SchroederInv_PolyRow3      -> 0
    SchroederInv_PolyDiag      -> 0
    SchroederInv_RevToff11     -> 0
    SchroederInv_RevTrev11     -> 0
    SchroederInv_RevTantidiag  -> 0
    SchroederInv_RevTacc       -> 0
    SchroederInv_RevTder       -> 0
    SchroederInv_RevEvenSum    -> 0
    SchroederInv_RevOddSum     -> 0
    SchroederInv_RevAccRevSum  -> 0
    SchroederInv_RevTransNat0  -> 0
    SchroederInv_RevTransNat1  -> 0
    SchroederInv_RevTransSqrs  -> 0
    SchroederInv_RevPolyDiag   -> 0
    SchroederInv_AltSum        -> 4
    SchroederInv_TablCol0      -> 7
    SchroederInv_TablDiag0     -> 12
    SchroederInv_RevPolyRow1   -> 12
    SchroederInv_PolyRow1      -> 27
    SchroederInv_RevAntiDSum   -> 213
    SchroederInv_TablDiag2     -> 1105
    SchroederInv_TablSum       -> 1333
    SchroederInv_AbsSum        -> 1333
    SchroederInv_AntiDSum      -> 1590
    SchroederInv_CentralE      -> 2003
    SchroederInv_RevPolyRow2   -> 5408
    SchroederInv_PolyRow2      -> 5563
    SchroederInv_TablDiag1     -> 5843
    SchroederInv_TablCol3      -> 5899
    SchroederInv_PosHalf       -> 7483
    SchroederInv_TablCol2      -> 8586
    SchroederInv_Trevinv11     -> 33877
    SchroederInv_TablDiag3     -> 35597
    SchroederInv_Trev11        -> 35607
    SchroederInv_RevCentralO   -> 50146
    SchroederInv_TablCol1      -> 55642
    SchroederInv_TablGcd       -> 55642
    SchroederInv_RevPolyRow3   -> 56220
    SchroederInv_NegHalf       -> 77020
    SchroederInv_RevNegHalf    -> 78050
    SchroederInv_Tinv11        -> 80247
    SchroederInv_RevPolyCol3   -> 86901
    SchroederInv_PolyCol2      -> 104934
    SchroederInv_RevPosHalf    -> 104934
    SchroederInv_TablMax       -> 110110
    SchroederInv_RevColMiddle  -> 110110
    SchroederInv_EvenSum       -> 111587
    SchroederInv_Toff11        -> 113413
    SchroederInv_TransNat0     -> 119915
    SchroederInv_Triangle      -> 122542
    SchroederInv_Talt          -> 122542
    SchroederInv_PolyCol3      -> 122558
    SchroederInv_BinConv       -> 240688
    SchroederInv_Trev          -> 266213
    SchroederInv_RevTalt       -> 266213
    SchroederInv_AccRevSum     -> 292400
    SchroederInv_TransNat1     -> 292400
'''
