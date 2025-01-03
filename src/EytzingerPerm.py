from functools import cache
from _tabltypes import Table
from EytzingerOrder import eytzingerorder

"""
    Let T(n) denote the triangular numbers. Set, for n >= 0,
    I(n) = [T(n), T(n+1)), lower bound included, upper bound excluded.
    Applying the Eytzinger ordering to I(n) gives
    E(n) = [eytzingerorder(n + 1, k + 1) + T(n) - 1 for k in 0..n].
    Joining E(0), E(1), E(2), ... gives a permutation of the nonnegative integers.

    [0] [ 0]
    [1] [ 2,  1]
    [2] [ 4,  3,  5]
    [3] [ 8,  7,  9, 6]
    [4] [13, 11, 14, 10, 12]
    [5] [18, 16, 20, 15, 17, 19]
    [6] [24, 22, 26, 21, 23, 25, 27]
    [7] [32, 30, 34, 29, 31, 33, 35, 28]
    [8] [41, 39, 43, 37, 40, 42, 44, 36, 38]
    [9] [51, 48, 53, 46, 50, 52, 54, 45, 47, 49]
"""


@cache
def eytzingerperm(n: int) -> list[int]:
    t = n * (n + 1) // 2
    return [eytzingerorder(n)[k] + t for k in range(n + 1)]


EytzingerPerm = Table(
    eytzingerperm, 
    "EytzingerPerm", 
    ["A375469"],
    "",
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(EytzingerPerm)


''' OEIS
    EytzingerPerm_Trev          -> 0 
    EytzingerPerm_Toff11        -> 0 
    EytzingerPerm_Trev11        -> 0 
    EytzingerPerm_Tantidiag     -> 0 
    EytzingerPerm_Tacc          -> 0 
    EytzingerPerm_Tder          -> 0 
    EytzingerPerm_TablCol0      -> 0 
    EytzingerPerm_TablCol1      -> 0 
    EytzingerPerm_TablCol2      -> 0 
    EytzingerPerm_TablCol3      -> 0 
    EytzingerPerm_TablDiag0     -> 0 
    EytzingerPerm_TablDiag1     -> 0 
    EytzingerPerm_TablDiag2     -> 0 
    EytzingerPerm_TablDiag3     -> 0 
    EytzingerPerm_TablLcm       -> 0 
    EytzingerPerm_EvenSum       -> 0 
    EytzingerPerm_OddSum        -> 0 
    EytzingerPerm_AltSum        -> 0 
    EytzingerPerm_AccSum        -> 0 
    EytzingerPerm_AccRevSum     -> 0 
    EytzingerPerm_AntiDSum      -> 0 
    EytzingerPerm_ColMiddle     -> 0 
    EytzingerPerm_CentralE      -> 0 
    EytzingerPerm_CentralO      -> 0 
    EytzingerPerm_PosHalf       -> 0 
    EytzingerPerm_NegHalf       -> 0 
    EytzingerPerm_TransNat0     -> 0 
    EytzingerPerm_TransNat1     -> 0 
    EytzingerPerm_TransSqrs     -> 0 
    EytzingerPerm_BinConv       -> 0 
    EytzingerPerm_InvBinConv    -> 0 
    EytzingerPerm_PolyRow2      -> 0 
    EytzingerPerm_PolyRow3      -> 0 
    EytzingerPerm_PolyCol2      -> 0 
    EytzingerPerm_PolyCol3      -> 0 
    EytzingerPerm_PolyDiag      -> 0 
    EytzingerPerm_RevToff11     -> 0 
    EytzingerPerm_RevTrev11     -> 0 
    EytzingerPerm_RevTantidiag  -> 0 
    EytzingerPerm_RevTacc       -> 0 
    EytzingerPerm_RevTalt       -> 0 
    EytzingerPerm_RevTder       -> 0 
    EytzingerPerm_RevEvenSum    -> 0 
    EytzingerPerm_RevOddSum     -> 0 
    EytzingerPerm_RevAccRevSum  -> 0 
    EytzingerPerm_RevAntiDSum   -> 0 
    EytzingerPerm_RevColMiddle  -> 0 
    EytzingerPerm_RevCentralO   -> 0 
    EytzingerPerm_RevNegHalf    -> 0 
    EytzingerPerm_RevTransNat0  -> 0 
    EytzingerPerm_RevTransNat1  -> 0 
    EytzingerPerm_RevTransSqrs  -> 0 
    EytzingerPerm_RevPolyRow2   -> 0 
    EytzingerPerm_RevPolyRow3   -> 0 
    EytzingerPerm_RevPolyCol3   -> 0 
    EytzingerPerm_RevPolyDiag   -> 0 
    EytzingerPerm_TablGcd       -> https://oeis.org/A12
    EytzingerPerm_PolyRow1      -> https://oeis.org/A27
    EytzingerPerm_TablMax       -> https://oeis.org/A96
    EytzingerPerm_RevPolyRow1   -> https://oeis.org/A5408
    EytzingerPerm_TablSum       -> https://oeis.org/A27480
    EytzingerPerm_AbsSum        -> https://oeis.org/A27480
    EytzingerPerm_Triangle      -> https://oeis.org/A375469
    EytzingerPerm_Talt          -> https://oeis.org/A375469

    EytzingerPerm: Distinct: 7, Hits: 8, Misses: 56
'''
