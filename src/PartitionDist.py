from functools import cache
from math import sqrt
from _tabltypes import Table

"""Partitions of n having k distinct parts.

[0]  [1]
[1]  [0, 1]
[2]  [0, 1, 0]
[3]  [0, 1, 1, 0]
[4]  [0, 1, 1, 0, 0]
[5]  [0, 1, 2, 0, 0, 0]
[6]  [0, 1, 2, 1, 0, 0, 0]
[7]  [0, 1, 3, 1, 0, 0, 0, 0]
[8]  [0, 1, 3, 2, 0, 0, 0, 0, 0]
[9]  [0, 1, 4, 3, 0, 0, 0, 0, 0, 0]
[10] [0, 1, 4, 4, 1, 0, 0, 0, 0, 0, 0]

"""


@cache
def _partdist(n: int, k: int) -> int:
    if k < 1 or n < k:
        return 0
    if n == 1:
        return 1

    return _partdist(n - k, k) + _partdist(n - k, k - 1)


@cache
def partdist(n: int) -> list[int]:
    if n == 0:
        return [1]

    f = (sqrt(1 + 8*n) - 1) // 2
    return [_partdist(n, k) if k <= f else 0 for k in range(n + 1)]


PartDist = Table(
    partdist, 
    "PartitionDist", 
    ["A008289"], 
    "",
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(PartDist)




''' OEIS
    PartitionDist_Tinvrev11     -> https://oeis.org/A-999999
    PartitionDist_Talt          -> https://oeis.org/A-999999
    PartitionDist_RevTalt       -> https://oeis.org/A-999999
    PartitionDist_Triangle      -> 0 
    PartitionDist_Trev11        -> 0 
    PartitionDist_Tantidiag     -> 0 
    PartitionDist_Tacc          -> 0 
    PartitionDist_Tder          -> 0 
    PartitionDist_TablLcm       -> 0 
    PartitionDist_TablGcd       -> 0 
    PartitionDist_AccSum        -> 0 
    PartitionDist_AccRevSum     -> 0 
    PartitionDist_ColMiddle     -> 0 
    PartitionDist_TransNat1     -> 0 
    PartitionDist_TransSqrs     -> 0 
    PartitionDist_BinConv       -> 0 
    PartitionDist_InvBinConv    -> 0 
    PartitionDist_RevToff11     -> 0 
    PartitionDist_RevTantidiag  -> 0 
    PartitionDist_RevTacc       -> 0 
    PartitionDist_RevTder       -> 0 
    PartitionDist_RevAccRevSum  -> 0 
    PartitionDist_RevTransNat0  -> 0 
    PartitionDist_RevTransNat1  -> 0 
    PartitionDist_RevTransSqrs  -> 0 
    PartitionDist_TablCol0      -> https://oeis.org/A7
    PartitionDist_TablDiag3     -> https://oeis.org/A7
    PartitionDist_CentralE      -> https://oeis.org/A7
    PartitionDist_CentralO      -> https://oeis.org/A7
    PartitionDist_TablSum       -> https://oeis.org/A9
    PartitionDist_AbsSum        -> https://oeis.org/A9
    PartitionDist_TablCol1      -> https://oeis.org/A12
    PartitionDist_RevPolyRow1   -> https://oeis.org/A12
    PartitionDist_PolyRow1      -> https://oeis.org/A27
    PartitionDist_PolyRow2      -> https://oeis.org/A27
    PartitionDist_RevPolyRow2   -> https://oeis.org/A27
    PartitionDist_RevAntiDSum   -> https://oeis.org/A700
    PartitionDist_TablCol3      -> https://oeis.org/A1399
    PartitionDist_PolyRow3      -> https://oeis.org/A2378
    PartitionDist_RevPolyRow3   -> https://oeis.org/A2378
    PartitionDist_TablCol2      -> https://oeis.org/A4526
    PartitionDist_TransNat0     -> https://oeis.org/A15723
    PartitionDist_TablDiag0     -> https://oeis.org/A19590
    PartitionDist_RevCentralO   -> https://oeis.org/A19590
    PartitionDist_AntiDSum      -> https://oeis.org/A25147
    PartitionDist_TablMax       -> https://oeis.org/A30699
    PartitionDist_PolyCol2      -> https://oeis.org/A32302
    PartitionDist_RevPosHalf    -> https://oeis.org/A32302
    PartitionDist_PolyCol3      -> https://oeis.org/A32308
    PartitionDist_Toff11        -> https://oeis.org/A60016
    PartitionDist_RevTrev11     -> https://oeis.org/A60016
    PartitionDist_OddSum        -> https://oeis.org/A67659
    PartitionDist_EvenSum       -> https://oeis.org/A67661
    PartitionDist_RevNegHalf    -> https://oeis.org/A70877
    PartitionDist_AltSum        -> https://oeis.org/A80995
    PartitionDist_RevEvenSum    -> https://oeis.org/A96791
    PartitionDist_RevOddSum     -> https://oeis.org/A96792
    PartitionDist_Trev          -> https://oeis.org/A124788
    PartitionDist_RevColMiddle  -> https://oeis.org/A183918
    PartitionDist_TablDiag1     -> https://oeis.org/A279329
    PartitionDist_TablDiag2     -> https://oeis.org/A279329
    PartitionDist_PolyDiag      -> https://oeis.org/A291698
    PartitionDist_PosHalf       -> https://oeis.org/A304961
    PartitionDist_NegHalf       -> https://oeis.org/A337299
    PartitionDist_RevPolyDiag   -> https://oeis.org/A340103
    PartitionDist_RevPolyCol3   -> https://oeis.org/A344062

    PartitionDist: Distinct: 31, Hits: 44, Misses: 22
'''
