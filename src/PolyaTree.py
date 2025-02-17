from functools import cache
from _tabltypes import Table
from PolyaTreeAcc import polyatreeacc

"""Polya Trees by height
[0] [1]
[1] [0, 1]
[2] [0, 1,  1]
[3] [0, 1,  2,   1]
[4] [0, 1,  4,   3,   1]
[5] [0, 1,  6,   8,   4,   1]
[6] [0, 1, 10,  18,  13,   5,  1]
[7] [0, 1, 14,  38,  36,  19,  6,  1]
[8] [0, 1, 21,  76,  93,  61, 26,  7, 1]
[9] [0, 1, 29, 147, 225, 180, 94, 34, 8, 1]
"""


@cache
def polyatree(n: int) -> list[int]:
    p = polyatreeacc(n)
    return [int(n < 1)] + [p[k] - p[k-1] for k in range(1, n + 1)]


PolyaTree = Table(
    polyatree, 
    "PolyaTree", 
    ["A034781"], 
    "", 
    r"A375467(n, k) - A375467(n, k - 1)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(PolyaTree)




''' OEIS
    PolyaTree_Triangle      -> 0 
    PolyaTree_Trev          -> 0 
    PolyaTree_Trev11        -> 0 
    PolyaTree_Tinv11        -> 0 
    PolyaTree_Tinvrev11     -> 0 
    PolyaTree_Trevinv11     -> 0 
    PolyaTree_Tantidiag     -> 0 
    PolyaTree_Tacc          -> 0 
    PolyaTree_Talt          -> 0 
    PolyaTree_Tder          -> 0 
    PolyaTree_TablLcm       -> 0 
    PolyaTree_TablMax       -> 0 
    PolyaTree_EvenSum       -> 0 
    PolyaTree_OddSum        -> 0 
    PolyaTree_AltSum        -> 0 
    PolyaTree_AccRevSum     -> 0 
    PolyaTree_AntiDSum      -> 0 
    PolyaTree_ColMiddle     -> 0 
    PolyaTree_CentralO      -> 0 
    PolyaTree_PosHalf       -> 0 
    PolyaTree_NegHalf       -> 0 
    PolyaTree_TransNat1     -> 0 
    PolyaTree_TransSqrs     -> 0 
    PolyaTree_BinConv       -> 0 
    PolyaTree_InvBinConv    -> 0 
    PolyaTree_PolyCol2      -> 0 
    PolyaTree_PolyCol3      -> 0 
    PolyaTree_PolyDiag      -> 0 
    PolyaTree_RevToff11     -> 0 
    PolyaTree_RevTrev11     -> 0 
    PolyaTree_RevTantidiag  -> 0 
    PolyaTree_RevTacc       -> 0 
    PolyaTree_RevTalt       -> 0 
    PolyaTree_RevTder       -> 0 
    PolyaTree_RevEvenSum    -> 0 
    PolyaTree_RevOddSum     -> 0 
    PolyaTree_RevAntiDSum   -> 0 
    PolyaTree_RevColMiddle  -> 0 
    PolyaTree_RevPosHalf    -> 0 
    PolyaTree_RevNegHalf    -> 0 
    PolyaTree_RevTransNat0  -> 0 
    PolyaTree_RevTransSqrs  -> 0 
    PolyaTree_RevPolyCol3   -> 0 
    PolyaTree_RevPolyDiag   -> 0 
    PolyaTree_TablCol0      -> https://oeis.org/A7
    PolyaTree_TablCol1      -> https://oeis.org/A12
    PolyaTree_TablDiag0     -> https://oeis.org/A12
    PolyaTree_RevPolyRow1   -> https://oeis.org/A12
    PolyaTree_TablDiag1     -> https://oeis.org/A27
    PolyaTree_PolyRow1      -> https://oeis.org/A27
    PolyaTree_RevPolyRow2   -> https://oeis.org/A27
    PolyaTree_TablCol2      -> https://oeis.org/A65
    PolyaTree_TablSum       -> https://oeis.org/A81
    PolyaTree_AbsSum        -> https://oeis.org/A81
    PolyaTree_TablCol3      -> https://oeis.org/A235
    PolyaTree_RevPolyRow3   -> https://oeis.org/A290
    PolyaTree_TransNat0     -> https://oeis.org/A1853
    PolyaTree_PolyRow2      -> https://oeis.org/A2378
    PolyaTree_Toff11        -> https://oeis.org/A34781
    PolyaTree_TablDiag2     -> https://oeis.org/A34856
    PolyaTree_TablDiag3     -> https://oeis.org/A34857
    PolyaTree_PolyRow3      -> https://oeis.org/A45991
    PolyaTree_RevCentralO   -> https://oeis.org/A245102
    PolyaTree_CentralE      -> https://oeis.org/A245103
    PolyaTree_TablGcd       -> https://oeis.org/A326753
    PolyaTree_AccSum        -> https://oeis.org/A375468
    PolyaTree_RevAccRevSum  -> https://oeis.org/A375468
    PolyaTree_RevTransNat1  -> https://oeis.org/A375468

    PolyaTree: Distinct: 18, Hits: 24, Misses: 44
'''
