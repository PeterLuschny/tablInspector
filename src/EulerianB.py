from functools import cache
from _tabltypes import Table

"""EulerianB triangle.


[0] [1]
[1] [1,    1]
[2] [1,    6,     1]
[3] [1,   23,    23,      1]
[4] [1,   76,   230,     76,      1]
[5] [1,  237,  1682,   1682,    237,     1]
[6] [1,  722, 10543,  23548,  10543,   722,    1]
[7] [1, 2179, 60657, 259723, 259723, 60657, 2179,  1]
"""


@cache
def eulerianb(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = eulerianb(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = (2 * (n - k) + 1) * row[k - 1] + (2 * k + 1) * row[k]
    return row


EulerianB = Table(
    eulerianb, 
    "EulerianB", 
    ["A060187", "A138076"], 
    "A000000", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(EulerianB)






''' OEIS
    EulerianB_Trevinv       -> 0 
    EulerianB_Toff11        -> 0 
    EulerianB_Trev11        -> 0 
    EulerianB_Tinv11        -> 0 
    EulerianB_Trevinv11     -> 0 
    EulerianB_Tantidiag     -> 0 
    EulerianB_Tacc          -> 0 
    EulerianB_TablLcm       -> 0 
    EulerianB_TablGcd       -> 0 
    EulerianB_EvenSum       -> 0 
    EulerianB_OddSum        -> 0 
    EulerianB_CentralO      -> 0 
    EulerianB_NegHalf       -> 0 
    EulerianB_TransSqrs     -> 0 
    EulerianB_BinConv       -> 0 
    EulerianB_InvBinConv    -> 0 
    EulerianB_PolyRow3      -> 0 
    EulerianB_PolyCol3      -> 0 
    EulerianB_PolyDiag      -> 0 
    EulerianB_RevToff11     -> 0 
    EulerianB_RevTrev11     -> 0 
    EulerianB_RevTinv11     -> 0 
    EulerianB_RevTantidiag  -> 0 
    EulerianB_RevTacc       -> 0 
    EulerianB_RevEvenSum    -> 0 
    EulerianB_RevOddSum     -> 0 
    EulerianB_RevCentralO   -> 0 
    EulerianB_RevNegHalf    -> 0 
    EulerianB_RevTransSqrs  -> 0 
    EulerianB_RevPolyRow3   -> 0 
    EulerianB_RevPolyCol3   -> 0 
    EulerianB_RevPolyDiag   -> 0 
    EulerianB_TablCol0      -> https://oeis.org/A12
    EulerianB_TablDiag0     -> https://oeis.org/A12
    EulerianB_PolyRow1      -> https://oeis.org/A27
    EulerianB_RevPolyRow1   -> https://oeis.org/A27
    EulerianB_TablSum       -> https://oeis.org/A165
    EulerianB_AbsSum        -> https://oeis.org/A165
    EulerianB_AltSum        -> https://oeis.org/A2436
    EulerianB_TransNat0     -> https://oeis.org/A14479
    EulerianB_RevTransNat0  -> https://oeis.org/A14479
    EulerianB_PolyRow2      -> https://oeis.org/A28884
    EulerianB_RevPolyRow2   -> https://oeis.org/A28884
    EulerianB_Triangle      -> https://oeis.org/A60187
    EulerianB_Trev          -> https://oeis.org/A60187
    EulerianB_Talt          -> https://oeis.org/A60187
    EulerianB_RevTalt       -> https://oeis.org/A60187
    EulerianB_TablCol1      -> https://oeis.org/A60188
    EulerianB_TablDiag1     -> https://oeis.org/A60188
    EulerianB_TablCol2      -> https://oeis.org/A60189
    EulerianB_TablDiag2     -> https://oeis.org/A60189
    EulerianB_TablCol3      -> https://oeis.org/A60190
    EulerianB_TablDiag3     -> https://oeis.org/A60190
    EulerianB_PosHalf       -> https://oeis.org/A80253
    EulerianB_PolyCol2      -> https://oeis.org/A80253
    EulerianB_RevPosHalf    -> https://oeis.org/A80253
    EulerianB_Tder          -> https://oeis.org/A142707
    EulerianB_RevTder       -> https://oeis.org/A142707
    EulerianB_TablMax       -> https://oeis.org/A154420
    EulerianB_ColMiddle     -> https://oeis.org/A154420
    EulerianB_RevColMiddle  -> https://oeis.org/A154420
    EulerianB_Tinv          -> https://oeis.org/A171273
    EulerianB_Tinvrev       -> https://oeis.org/A171273
    EulerianB_CentralE      -> https://oeis.org/A177043
    EulerianB_AntiDSum      -> https://oeis.org/A178118
    EulerianB_RevAntiDSum   -> https://oeis.org/A178118
    EulerianB_AccSum        -> https://oeis.org/A187735
    EulerianB_AccRevSum     -> https://oeis.org/A187735
    EulerianB_TransNat1     -> https://oeis.org/A187735
    EulerianB_RevAccRevSum  -> https://oeis.org/A187735
    EulerianB_RevTransNat1  -> https://oeis.org/A187735

    EulerianB: Distinct: 18, Hits: 39, Misses: 32
'''
