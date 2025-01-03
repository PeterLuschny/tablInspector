from functools import cache
from math import sqrt
from _tabltypes import Table

"""Compositions of n into k distinct parts.

[ 0] [1]
[ 1] [0, 1]
[ 2] [0, 1,  0]
[ 3] [0, 1,  2,  0]
[ 4] [0, 1,  2,  0,  0]
[ 5] [0, 1,  4,  0,  0, 0]
[ 6] [0, 1,  4,  6,  0, 0, 0]
[ 7] [0, 1,  6,  6,  0, 0, 0, 0]
[ 8] [0, 1,  6, 12,  0, 0, 0, 0, 0]
[ 9] [0, 1,  8, 18,  0, 0, 0, 0, 0, 0]
[10] [0, 1,  8, 24, 24, 0, 0, 0, 0, 0, 0]
[11] [0, 1, 10, 30, 24, 0, 0, 0, 0, 0, 0, 0]
[12] [0, 1, 10, 42, 48, 0, 0, 0, 0, 0, 0, 0, 0]
"""

@cache
def _compodist(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        if n == 0:
            return 1
        else:
            return 0
    return _compodist(n - k, k) + k * _compodist(n - k, k - 1)


@cache
def compodist(n: int) -> list[int]:
    f = (sqrt(1 + 8*n) - 1) // 2
    return [_compodist(n, k) if k <= f else 0 for k in range(n + 1)]


CompoDist = Table(
    compodist, 
    "CompositionDist", 
    ["A072574", "A216652"],
    "",
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CompoDist)


''' OEIS
    CompositionDist_Triangle      -> 0 
    CompositionDist_Trev          -> 0 
    CompositionDist_Trev11        -> 0 
    CompositionDist_Tinvrev11     -> 0 
    CompositionDist_Tantidiag     -> 0 
    CompositionDist_Tacc          -> 0 
    CompositionDist_Talt          -> 0 
    CompositionDist_Tder          -> 0 
    CompositionDist_TablCol3      -> 0 
    CompositionDist_TablLcm       -> 0 
    CompositionDist_TablGcd       -> 0 
    CompositionDist_TablMax       -> 0 
    CompositionDist_AccSum        -> 0 
    CompositionDist_ColMiddle     -> 0 
    CompositionDist_NegHalf       -> 0 
    CompositionDist_TransSqrs     -> 0 
    CompositionDist_InvBinConv    -> 0 
    CompositionDist_PolyCol3      -> 0 
    CompositionDist_PolyDiag      -> 0 
    CompositionDist_RevToff11     -> 0 
    CompositionDist_RevTantidiag  -> 0 
    CompositionDist_RevTacc       -> 0 
    CompositionDist_RevTalt       -> 0 
    CompositionDist_RevTder       -> 0 
    CompositionDist_RevEvenSum    -> 0 
    CompositionDist_RevOddSum     -> 0 
    CompositionDist_RevAccRevSum  -> 0 
    CompositionDist_RevColMiddle  -> 0 
    CompositionDist_RevNegHalf    -> 0 
    CompositionDist_RevTransNat0  -> 0 
    CompositionDist_RevTransNat1  -> 0 
    CompositionDist_RevTransSqrs  -> 0 
    CompositionDist_RevPolyCol3   -> 0 
    CompositionDist_RevPolyDiag   -> 0 
    CompositionDist_TablCol0      -> https://oeis.org/A7
    CompositionDist_TablDiag0     -> https://oeis.org/A7
    CompositionDist_TablDiag1     -> https://oeis.org/A7
    CompositionDist_TablDiag2     -> https://oeis.org/A7
    CompositionDist_RevCentralO   -> https://oeis.org/A7
    CompositionDist_TablCol1      -> https://oeis.org/A12
    CompositionDist_RevPolyRow1   -> https://oeis.org/A12
    CompositionDist_PolyRow1      -> https://oeis.org/A27
    CompositionDist_PolyRow2      -> https://oeis.org/A27
    CompositionDist_RevPolyRow2   -> https://oeis.org/A27
    CompositionDist_RevPolyRow3   -> https://oeis.org/A5563
    CompositionDist_PolyRow3      -> https://oeis.org/A14105
    CompositionDist_PolyCol2      -> https://oeis.org/A32005
    CompositionDist_TablSum       -> https://oeis.org/A32020
    CompositionDist_AbsSum        -> https://oeis.org/A32020
    CompositionDist_RevAntiDSum   -> https://oeis.org/A32021
    CompositionDist_AntiDSum      -> https://oeis.org/A32022
    CompositionDist_TablCol2      -> https://oeis.org/A52928
    CompositionDist_Toff11        -> https://oeis.org/A72574
    CompositionDist_RevTrev11     -> https://oeis.org/A72574
    CompositionDist_AccRevSum     -> https://oeis.org/A72576
    CompositionDist_TransNat1     -> https://oeis.org/A72576
    CompositionDist_TransNat0     -> https://oeis.org/A97910
    CompositionDist_BinConv       -> https://oeis.org/A97965
    CompositionDist_TablDiag3     -> https://oeis.org/A186685
    CompositionDist_CentralE      -> https://oeis.org/A186685
    CompositionDist_CentralO      -> https://oeis.org/A186685
    CompositionDist_OddSum        -> https://oeis.org/A332304
    CompositionDist_EvenSum       -> https://oeis.org/A332305
    CompositionDist_PosHalf       -> https://oeis.org/A336127
    CompositionDist_AltSum        -> https://oeis.org/A339435

    CompositionDist: Distinct: 20, Hits: 31, Misses: 34
'''
