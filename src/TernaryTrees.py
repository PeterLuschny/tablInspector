from functools import cache
from itertools import accumulate
from _tabltypes import Table

"""Ternary trees, Fuss-Catalan 2.


[0] [1]
[1] [0, 1]
[2] [0, 1,  3]
[3] [0, 1,  5, 12]
[4] [0, 1,  7, 25,  55]
[5] [0, 1,  9, 42, 130,  273]
[6] [0, 1, 11, 63, 245,  700, 1428]
[7] [0, 1, 13, 88, 408, 1428, 3876, 7752]
"""


@cache
def ternarytree(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = ternarytree(n - 1) + [ternarytree(n - 1)[n - 1]]

    return list(accumulate(accumulate(row)))


TernaryTree = Table(
    ternarytree,
    "TernaryTrees",
    ["A355172"],
    "",
    r"is(k=0)\, ?\, 0^n : \frac{(2n-2k+3) \, (2n+k-1)!}{(2n+1)! \, (k-1)!}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(TernaryTree)






''' OEIS
    TernaryTrees_Trev          -> 0 
    TernaryTrees_Toff11        -> 0 
    TernaryTrees_Trev11        -> 0 
    TernaryTrees_Tinvrev11     -> 0 
    TernaryTrees_Tantidiag     -> 0 
    TernaryTrees_Tacc          -> 0 
    TernaryTrees_Tder          -> 0 
    TernaryTrees_TablLcm       -> 0 
    TernaryTrees_EvenSum       -> 0 
    TernaryTrees_OddSum        -> 0 
    TernaryTrees_AltSum        -> 0 
    TernaryTrees_AccRevSum     -> 0 
    TernaryTrees_AntiDSum      -> 0 
    TernaryTrees_ColMiddle     -> 0 
    TernaryTrees_CentralE      -> 0 
    TernaryTrees_CentralO      -> 0 
    TernaryTrees_PosHalf       -> 0 
    TernaryTrees_NegHalf       -> 0 
    TernaryTrees_TransNat0     -> 0 
    TernaryTrees_TransNat1     -> 0 
    TernaryTrees_TransSqrs     -> 0 
    TernaryTrees_BinConv       -> 0 
    TernaryTrees_PolyRow3      -> 0 
    TernaryTrees_PolyCol2      -> 0 
    TernaryTrees_PolyCol3      -> 0 
    TernaryTrees_PolyDiag      -> 0 
    TernaryTrees_RevToff11     -> 0 
    TernaryTrees_RevTrev11     -> 0 
    TernaryTrees_RevTantidiag  -> 0 
    TernaryTrees_RevTacc       -> 0 
    TernaryTrees_RevTalt       -> 0 
    TernaryTrees_RevTder       -> 0 
    TernaryTrees_RevEvenSum    -> 0 
    TernaryTrees_RevOddSum     -> 0 
    TernaryTrees_RevAntiDSum   -> 0 
    TernaryTrees_RevColMiddle  -> 0 
    TernaryTrees_RevCentralO   -> 0 
    TernaryTrees_RevPosHalf    -> 0 
    TernaryTrees_RevNegHalf    -> 0 
    TernaryTrees_RevTransSqrs  -> 0 
    TernaryTrees_RevPolyDiag   -> 0 
    TernaryTrees_TablCol0      -> https://oeis.org/A7
    TernaryTrees_TablCol1      -> https://oeis.org/A12
    TernaryTrees_RevPolyRow1   -> https://oeis.org/A12
    TernaryTrees_PolyRow1      -> https://oeis.org/A27
    TernaryTrees_RevPolyRow2   -> https://oeis.org/A27
    TernaryTrees_TablDiag0     -> https://oeis.org/A1764
    TernaryTrees_TablMax       -> https://oeis.org/A1764
    TernaryTrees_RevPolyCol3   -> https://oeis.org/A4319
    TernaryTrees_TablCol2      -> https://oeis.org/A5408
    TernaryTrees_TablSum       -> https://oeis.org/A6629
    TernaryTrees_AbsSum        -> https://oeis.org/A6629
    TernaryTrees_RevPolyRow3   -> https://oeis.org/A27691
    TernaryTrees_PolyRow2      -> https://oeis.org/A49451
    TernaryTrees_TablCol3      -> https://oeis.org/A71355
    TernaryTrees_TablDiag2     -> https://oeis.org/A102594
    TernaryTrees_RevTransNat0  -> https://oeis.org/A102594
    TernaryTrees_TablDiag1     -> https://oeis.org/A102893
    TernaryTrees_AccSum        -> https://oeis.org/A102893
    TernaryTrees_RevAccRevSum  -> https://oeis.org/A102893
    TernaryTrees_RevTransNat1  -> https://oeis.org/A102893
    TernaryTrees_TablDiag3     -> https://oeis.org/A230547
    TernaryTrees_InvBinConv    -> https://oeis.org/A246434
    TernaryTrees_TablGcd       -> https://oeis.org/A349509
    TernaryTrees_Triangle      -> https://oeis.org/A355172
    TernaryTrees_Talt          -> https://oeis.org/A355172

    TernaryTrees: Distinct: 17, Hits: 25, Misses: 41
'''
