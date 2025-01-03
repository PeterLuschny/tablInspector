from functools import cache
from math import sqrt
from _tabltypes import Table

"""Partitions of n having exactly k distinct part sizes, A365676.

[0] 1;
[1] 0, 1;
[2] 0, 2,  0;
[3] 0, 2,  1,  0;
[4] 0, 3,  2,  0, 0;
[5] 0, 2,  5,  0, 0, 0;
[6] 0, 4,  6,  1, 0, 0, 0;
[7] 0, 2, 11,  2, 0, 0, 0, 0;
[8] 0, 4, 13,  5, 0, 0, 0, 0, 0;
[9] 0, 3, 17, 10, 0, 0, 0, 0, 0, 0;

[6, 1] -> [[1, 1, 1, 1, 1, 1], [2, 2, 2], [3, 3], [6]]
[6, 2] -> [[1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 1, 1, 3], [1, 1, 4], [2, 4], [1, 5]]
[6, 3] -> [[1, 2, 3]]
"""


@cache
def _partdistsize(n: int, k: int, r: int) -> int:
    if n == 0:
        return 1 if k == 0 else 0
    if k == 0 or r == 0:
        return 0
    if k > n // 2 + 1: return 0
    return (sum(_partdistsize(n - r * j, k - 1, r - 1) 
            for j in range(1, n // r + 1))
           + _partdistsize(n, k, r - 1))


@cache
def partdistsize(n: int) -> list[int]:
    f = (sqrt(1 + 8*n) - 1) // 2
    return [_partdistsize(n, k, n) if k <= f else 0 for k in range(n + 1)]


PartDistSize = Table(
    partdistsize, 
    "PartitionDistSize", 
    ["A365676", "A116608", "A060177"], 
    "", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(PartDistSize)


''' OEIS
    PartitionDistSize_Trev          -> 0 
    PartitionDistSize_Toff11        -> 0 
    PartitionDistSize_Trev11        -> 0 
    PartitionDistSize_Tantidiag     -> 0 
    PartitionDistSize_Tacc          -> 0 
    PartitionDistSize_Tder          -> 0 
    PartitionDistSize_TablLcm       -> 0 
    PartitionDistSize_TablGcd       -> 0 
    PartitionDistSize_TablMax       -> 0 
    PartitionDistSize_AntiDSum      -> 0 
    PartitionDistSize_ColMiddle     -> 0 
    PartitionDistSize_PosHalf       -> 0 
    PartitionDistSize_NegHalf       -> 0 
    PartitionDistSize_BinConv       -> 0 
    PartitionDistSize_InvBinConv    -> 0 
    PartitionDistSize_RevToff11     -> 0 
    PartitionDistSize_RevTrev11     -> 0 
    PartitionDistSize_RevTantidiag  -> 0 
    PartitionDistSize_RevTacc       -> 0 
    PartitionDistSize_RevTalt       -> 0 
    PartitionDistSize_RevTder       -> 0 
    PartitionDistSize_RevEvenSum    -> 0 
    PartitionDistSize_RevOddSum     -> 0 
    PartitionDistSize_RevAntiDSum   -> 0 
    PartitionDistSize_RevNegHalf    -> 0 
    PartitionDistSize_RevTransSqrs  -> 0 
    PartitionDistSize_RevPolyCol3   -> 0 
    PartitionDistSize_RevPolyDiag   -> 0 
    PartitionDistSize_TablCol1      -> https://oeis.org/A5
    PartitionDistSize_TablCol0      -> https://oeis.org/A7
    PartitionDistSize_TablDiag0     -> https://oeis.org/A7
    PartitionDistSize_TablDiag1     -> https://oeis.org/A7
    PartitionDistSize_TablDiag2     -> https://oeis.org/A7
    PartitionDistSize_TablDiag3     -> https://oeis.org/A7
    PartitionDistSize_CentralE      -> https://oeis.org/A7
    PartitionDistSize_RevCentralO   -> https://oeis.org/A7
    PartitionDistSize_RevPolyRow1   -> https://oeis.org/A12
    PartitionDistSize_PolyRow1      -> https://oeis.org/A27
    PartitionDistSize_CentralO      -> https://oeis.org/A38
    PartitionDistSize_TablSum       -> https://oeis.org/A41
    PartitionDistSize_AbsSum        -> https://oeis.org/A41
    PartitionDistSize_AccRevSum     -> https://oeis.org/A70
    PartitionDistSize_TransNat0     -> https://oeis.org/A70
    PartitionDistSize_TransNat1     -> https://oeis.org/A70
    PartitionDistSize_TablCol2      -> https://oeis.org/A2133
    PartitionDistSize_TablCol3      -> https://oeis.org/A2134
    PartitionDistSize_PolyRow3      -> https://oeis.org/A5563
    PartitionDistSize_PolyRow2      -> https://oeis.org/A5843
    PartitionDistSize_RevPolyRow2   -> https://oeis.org/A5843
    PartitionDistSize_RevPolyRow3   -> https://oeis.org/A14105
    PartitionDistSize_PolyCol2      -> https://oeis.org/A15128
    PartitionDistSize_OddSum        -> https://oeis.org/A90794
    PartitionDistSize_EvenSum       -> https://oeis.org/A92306
    PartitionDistSize_AltSum        -> https://oeis.org/A104575
    PartitionDistSize_TransSqrs     -> https://oeis.org/A135348
    PartitionDistSize_RevColMiddle  -> https://oeis.org/A138954
    PartitionDistSize_RevTransNat0  -> https://oeis.org/A194552
    PartitionDistSize_PolyCol3      -> https://oeis.org/A264686
    PartitionDistSize_PolyDiag      -> https://oeis.org/A321880
    PartitionDistSize_AccSum        -> https://oeis.org/A365675
    PartitionDistSize_RevAccRevSum  -> https://oeis.org/A365675
    PartitionDistSize_RevTransNat1  -> https://oeis.org/A365675
    PartitionDistSize_Triangle      -> https://oeis.org/A365676
    PartitionDistSize_Talt          -> https://oeis.org/A365676

    PartitionDistSize: Distinct: 24, Hits: 36, Misses: 28
'''
