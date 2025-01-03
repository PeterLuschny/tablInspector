from functools import cache
from _tabltypes import Table

"""Inverse of the DyckPaths triangle. Unsigned version.

 [1] 
 [1, 1] 
 [1, 3, 1] 
 [1, 6, 5, 1] 
 [1, 10, 15, 7, 1] 
 [1, 15, 35, 28, 9, 1] 
 [1, 21, 70, 84, 45, 11, 1]
"""


@cache
def dyckpathsinv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    q = dyckpathsinv(n - 2) + [0]
    p = dyckpathsinv(n - 1) + [0]
    row = p.copy()
    row[n] = 1

    for k in range(n - 1, 0, -1):
        row[k] = p[k - 1] + 2 * p[k] - q[k]

    return row


DyckPathsInv = Table(
    dyckpathsinv,
    "DyckPathsInv",
    ["A085478", "A129818", "A123970"],
    "A039599",
    r"\binom{n+k}{2k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(DyckPathsInv)



''' OEIS
    DyckPathsInv_Tacc          -> 0 
    DyckPathsInv_Tder          -> 0 
    DyckPathsInv_TablLcm       -> 0 
    DyckPathsInv_TablMax       -> 0 
    DyckPathsInv_OddSum        -> 0 
    DyckPathsInv_ColMiddle     -> 0 
    DyckPathsInv_CentralO      -> 0 
    DyckPathsInv_TransSqrs     -> 0 
    DyckPathsInv_InvBinConv    -> 0 
    DyckPathsInv_RevTinv11     -> 0 
    DyckPathsInv_RevTantidiag  -> 0 
    DyckPathsInv_RevTder       -> 0 
    DyckPathsInv_RevColMiddle  -> 0 
    DyckPathsInv_RevTransSqrs  -> 0 
    DyckPathsInv_RevPolyCol3   -> 0 
    DyckPathsInv_RevPolyDiag   -> 0 
    DyckPathsInv_TablCol0      -> https://oeis.org/A12
    DyckPathsInv_TablDiag0     -> https://oeis.org/A12
    DyckPathsInv_TablGcd       -> https://oeis.org/A12
    DyckPathsInv_RevNegHalf    -> https://oeis.org/A12
    DyckPathsInv_PolyRow1      -> https://oeis.org/A27
    DyckPathsInv_RevPolyRow1   -> https://oeis.org/A27
    DyckPathsInv_AntiDSum      -> https://oeis.org/A79
    DyckPathsInv_TablCol1      -> https://oeis.org/A217
    DyckPathsInv_TablCol2      -> https://oeis.org/A332
    DyckPathsInv_TablDiag2     -> https://oeis.org/A384
    DyckPathsInv_TablDiag3     -> https://oeis.org/A447
    DyckPathsInv_TablCol3      -> https://oeis.org/A579
    DyckPathsInv_TablSum       -> https://oeis.org/A1519
    DyckPathsInv_AbsSum        -> https://oeis.org/A1519
    DyckPathsInv_PolyCol2      -> https://oeis.org/A1835
    DyckPathsInv_TransNat0     -> https://oeis.org/A1870
    DyckPathsInv_PolyCol3      -> https://oeis.org/A4253
    DyckPathsInv_TablDiag1     -> https://oeis.org/A5408
    DyckPathsInv_CentralE      -> https://oeis.org/A5809
    DyckPathsInv_PosHalf       -> https://oeis.org/A7583
    DyckPathsInv_AltSum        -> https://oeis.org/A11655
    DyckPathsInv_RevCentralO   -> https://oeis.org/A25174
    DyckPathsInv_AccSum        -> https://oeis.org/A27989
    DyckPathsInv_RevAccRevSum  -> https://oeis.org/A27989
    DyckPathsInv_RevTransNat1  -> https://oeis.org/A27989
    DyckPathsInv_PolyRow2      -> https://oeis.org/A28387
    DyckPathsInv_RevPolyRow2   -> https://oeis.org/A28387
    DyckPathsInv_Tantidiag     -> https://oeis.org/A34839
    DyckPathsInv_RevTacc       -> https://oeis.org/A38730
    DyckPathsInv_AccRevSum     -> https://oeis.org/A38731
    DyckPathsInv_TransNat1     -> https://oeis.org/A38731
    DyckPathsInv_Tinv          -> https://oeis.org/A39599
    DyckPathsInv_Tinv11        -> https://oeis.org/A50155
    DyckPathsInv_RevAntiDSum   -> https://oeis.org/A52535
    DyckPathsInv_Trev          -> https://oeis.org/A54142
    DyckPathsInv_RevTalt       -> https://oeis.org/A54142
    DyckPathsInv_RevTransNat0  -> https://oeis.org/A54444
    DyckPathsInv_BinConv       -> https://oeis.org/A82759
    DyckPathsInv_Triangle      -> https://oeis.org/A85478
    DyckPathsInv_Talt          -> https://oeis.org/A85478
    DyckPathsInv_NegHalf       -> https://oeis.org/A87168
    DyckPathsInv_PolyDiag      -> https://oeis.org/A94955
    DyckPathsInv_Tinvrev       -> https://oeis.org/A98435
    DyckPathsInv_RevOddSum     -> https://oeis.org/A99511
    DyckPathsInv_RevPolyRow3   -> https://oeis.org/A106734
    DyckPathsInv_RevEvenSum    -> https://oeis.org/A108479
    DyckPathsInv_EvenSum       -> https://oeis.org/A109961
    DyckPathsInv_PolyRow3      -> https://oeis.org/A123972
    DyckPathsInv_Trev11        -> https://oeis.org/A210551
    DyckPathsInv_RevToff11     -> https://oeis.org/A210551
    DyckPathsInv_Toff11        -> https://oeis.org/A258993
    DyckPathsInv_RevTrev11     -> https://oeis.org/A258993

    DyckPathsInv: Distinct: 40, Hits: 52, Misses: 16
'''
