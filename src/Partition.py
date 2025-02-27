from functools import cache
from _tabltypes import Table

"""Partition numbers (Euler's table), see also A026820, A000041.

[0] [1]
[1] [0, 1]
[2] [0, 1, 1]
[3] [0, 1, 1, 1]
[4] [0, 1, 2, 1, 1]
[5] [0, 1, 2, 2, 1, 1]
[6] [0, 1, 3, 3, 2, 1, 1]
[7] [0, 1, 3, 4, 3, 2, 1, 1]
[8] [0, 1, 4, 5, 5, 3, 2, 1, 1]
[9] [0, 1, 4, 7, 6, 5, 3, 2, 1, 1]
"""


@cache
def part(n: int, k: int) -> int:
    if k < 0 or n < 0:
        return 0
    if k == 0:
        return 1 if n == 0 else 0

    return part(n - 1, k - 1) + part(n - k, k)


@cache
def partition(n: int) -> list[int]:
    return [part(n, k) for k in range(n + 1)]


Partition = Table(
    partition,
    "Partition",
    ["A072233", "A008284", "A058398"],
    "A000000",
    r"T_{n - 1, k - 1} + T_{n - k, k}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Partition)






''' OEIS
    Partition_Tinv          -> 0 
    Partition_Trev          -> 0 
    Partition_Tinvrev11     -> 0 
    Partition_Trevinv11     -> 0 
    Partition_Tantidiag     -> 0 
    Partition_Tacc          -> 0 
    Partition_TablLcm       -> 0 
    Partition_InvBinConv    -> 0 
    Partition_RevToff11     -> 0 
    Partition_RevTrev11     -> 0 
    Partition_RevTantidiag  -> 0 
    Partition_RevTacc       -> 0 
    Partition_RevTalt       -> 0 
    Partition_RevTder       -> 0 
    Partition_RevTransSqrs  -> 0 
    Partition_TablCol0      -> https://oeis.org/A7
    Partition_RevAntiDSum   -> https://oeis.org/A9
    Partition_Trevinv       -> https://oeis.org/A12
    Partition_TablCol1      -> https://oeis.org/A12
    Partition_TablDiag0     -> https://oeis.org/A12
    Partition_TablDiag1     -> https://oeis.org/A12
    Partition_RevPolyRow1   -> https://oeis.org/A12
    Partition_PolyRow1      -> https://oeis.org/A27
    Partition_RevPolyRow2   -> https://oeis.org/A27
    Partition_TablSum       -> https://oeis.org/A41
    Partition_AbsSum        -> https://oeis.org/A41
    Partition_CentralE      -> https://oeis.org/A41
    Partition_RevCentralO   -> https://oeis.org/A41
    Partition_CentralO      -> https://oeis.org/A65
    Partition_AltSum        -> https://oeis.org/A700
    Partition_RevOddSum     -> https://oeis.org/A701
    Partition_TablCol3      -> https://oeis.org/A1399
    Partition_RevPolyRow3   -> https://oeis.org/A2061
    Partition_PolyRow2      -> https://oeis.org/A2378
    Partition_TablMax       -> https://oeis.org/A2569
    Partition_AntiDSum      -> https://oeis.org/A2865
    Partition_TablCol2      -> https://oeis.org/A4526
    Partition_TransNat0     -> https://oeis.org/A6128
    Partition_Toff11        -> https://oeis.org/A8284
    Partition_TablDiag3     -> https://oeis.org/A10701
    Partition_EvenSum       -> https://oeis.org/A27187
    Partition_OddSum        -> https://oeis.org/A27193
    Partition_PolyRow3      -> https://oeis.org/A27444
    Partition_Tinv11        -> https://oeis.org/A38498
    Partition_RevEvenSum    -> https://oeis.org/A46682
    Partition_TablDiag2     -> https://oeis.org/A55642
    Partition_AccSum        -> https://oeis.org/A58397
    Partition_RevAccRevSum  -> https://oeis.org/A58397
    Partition_RevTransNat1  -> https://oeis.org/A58397
    Partition_Trev11        -> https://oeis.org/A58398
    Partition_ColMiddle     -> https://oeis.org/A66639
    Partition_PolyCol2      -> https://oeis.org/A70933
    Partition_RevPosHalf    -> https://oeis.org/A70933
    Partition_RevNegHalf    -> https://oeis.org/A71109
    Partition_Triangle      -> https://oeis.org/A72233
    Partition_Talt          -> https://oeis.org/A72233
    Partition_PosHalf       -> https://oeis.org/A75900
    Partition_AccRevSum     -> https://oeis.org/A93694
    Partition_TransNat1     -> https://oeis.org/A93694
    Partition_BinConv       -> https://oeis.org/A98545
    Partition_RevColMiddle  -> https://oeis.org/A119620
    Partition_PolyDiag      -> https://oeis.org/A124577
    Partition_Tder          -> https://oeis.org/A172467
    Partition_RevTransNat0  -> https://oeis.org/A196087
    Partition_PolyCol3      -> https://oeis.org/A242587
    Partition_TransSqrs     -> https://oeis.org/A296010
    Partition_RevPolyCol3   -> https://oeis.org/A300579
    Partition_RevPolyDiag   -> https://oeis.org/A338697
    Partition_NegHalf       -> https://oeis.org/A352402
    Partition_TablGcd       -> https://oeis.org/A373820

    Partition: Distinct: 43, Hits: 55, Misses: 15
'''
