from functools import cache
from PolyaTreeAcc import polyatreeacc
from _tabltypes import Table

"""
[ 0] 0
[ 1] 0, 1
[ 2] 0, 0, 1
[ 3] 0, 0, 1,  1
[ 4] 0, 0, 1,  2,  1
[ 5] 0, 0, 1,  4,  3,    1
[ 6] 0, 0, 1,  6,  8,    4,   1
[ 7] 0, 0, 1, 10,  18,  13,   5,  1
[ 8] 0, 0, 1, 14,  38,  36,  19,  6,  1
[ 9] 0, 0, 1, 21,  76,  93,  61, 26,  7, 1
"""


@cache
def rootedtree(n: int) -> list[int]:
    p = polyatreeacc(n)
    return [0] + [p[k + 1] - p[k] for k in range(n)]


RootedTree = Table(
    rootedtree,
    "RootedTree",
    ["A034781"],
    "",
    r"A375467(n, k) - A375467(n, k - 1)",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(RootedTree)






''' OEIS
    RootedTree_Trev          -> 0 
    RootedTree_Trev11        -> 0 
    RootedTree_Tinv11        -> 0 
    RootedTree_Tinvrev11     -> 0 
    RootedTree_Trevinv11     -> 0 
    RootedTree_Tantidiag     -> 0 
    RootedTree_Tacc          -> 0 
    RootedTree_Talt          -> 0 
    RootedTree_Tder          -> 0 
    RootedTree_TablLcm       -> 0 
    RootedTree_TablMax       -> 0 
    RootedTree_EvenSum       -> 0 
    RootedTree_OddSum        -> 0 
    RootedTree_AltSum        -> 0 
    RootedTree_AccRevSum     -> 0 
    RootedTree_AntiDSum      -> 0 
    RootedTree_ColMiddle     -> 0 
    RootedTree_CentralO      -> 0 
    RootedTree_PosHalf       -> 0 
    RootedTree_NegHalf       -> 0 
    RootedTree_TransNat1     -> 0 
    RootedTree_TransSqrs     -> 0 
    RootedTree_BinConv       -> 0 
    RootedTree_InvBinConv    -> 0 
    RootedTree_PolyCol2      -> 0 
    RootedTree_PolyCol3      -> 0 
    RootedTree_PolyDiag      -> 0 
    RootedTree_RevToff11     -> 0 
    RootedTree_RevTrev11     -> 0 
    RootedTree_RevTantidiag  -> 0 
    RootedTree_RevTacc       -> 0 
    RootedTree_RevTalt       -> 0 
    RootedTree_RevTder       -> 0 
    RootedTree_RevEvenSum    -> 0 
    RootedTree_RevOddSum     -> 0 
    RootedTree_RevAntiDSum   -> 0 
    RootedTree_RevColMiddle  -> 0 
    RootedTree_RevPosHalf    -> 0 
    RootedTree_RevNegHalf    -> 0 
    RootedTree_RevTransNat0  -> 0 
    RootedTree_RevTransSqrs  -> 0 
    RootedTree_RevPolyCol3   -> 0 
    RootedTree_RevPolyDiag   -> 0 
    RootedTree_TablCol0      -> https://oeis.org/A4
    RootedTree_TablCol1      -> https://oeis.org/A12
    RootedTree_TablDiag0     -> https://oeis.org/A12
    RootedTree_RevPolyRow1   -> https://oeis.org/A12
    RootedTree_TablDiag1     -> https://oeis.org/A27
    RootedTree_PolyRow1      -> https://oeis.org/A27
    RootedTree_RevPolyRow2   -> https://oeis.org/A27
    RootedTree_TablCol2      -> https://oeis.org/A65
    RootedTree_TablSum       -> https://oeis.org/A81
    RootedTree_AbsSum        -> https://oeis.org/A81
    RootedTree_TablCol3      -> https://oeis.org/A235
    RootedTree_RevPolyRow3   -> https://oeis.org/A290
    RootedTree_TransNat0     -> https://oeis.org/A1853
    RootedTree_PolyRow2      -> https://oeis.org/A2378
    RootedTree_Triangle      -> https://oeis.org/A34781
    RootedTree_Toff11        -> https://oeis.org/A34781
    RootedTree_TablDiag2     -> https://oeis.org/A34856
    RootedTree_TablDiag3     -> https://oeis.org/A34857
    RootedTree_PolyRow3      -> https://oeis.org/A45991
    RootedTree_RevCentralO   -> https://oeis.org/A245102
    RootedTree_CentralE      -> https://oeis.org/A245103
    RootedTree_TablGcd       -> https://oeis.org/A326753
    RootedTree_AccSum        -> https://oeis.org/A375468
    RootedTree_RevAccRevSum  -> https://oeis.org/A375468
    RootedTree_RevTransNat1  -> https://oeis.org/A375468

    RootedTree: Distinct: 18, Hits: 25, Misses: 43
'''
