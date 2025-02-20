from functools import cache
from itertools import accumulate
from _tabltypes import Table
from Partition import partition

"""Euler's table, partition numbers at most.

[0] 1
[1] 0, 1
[2] 0, 1, 2
[3] 0, 1, 2,  3
[4] 0, 1, 3,  4,  5
[5] 0, 1, 3,  5,  6,  7
[6] 0, 1, 4,  7,  9, 10, 11
[7] 0, 1, 4,  8, 11, 13, 14, 15
[8] 0, 1, 5, 10, 15, 18, 20, 21, 22
[9] 0, 1, 5, 12, 18, 23, 26, 28, 29, 30
"""


@cache
def partitionacc(n: int) -> list[int]:
    return list(accumulate(partition(n)))


PartitionAcc = Table(
    partitionacc, 
    "PartitionAcc", 
    ["A026820", "A058400"], 
    "",
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(PartitionAcc)






''' OEIS
    PartitionAcc_Trev          -> 0 
    PartitionAcc_Tantidiag     -> 0 
    PartitionAcc_Tacc          -> 0 
    PartitionAcc_Talt          -> 0 
    PartitionAcc_Tder          -> 0 
    PartitionAcc_TablLcm       -> 0 
    PartitionAcc_EvenSum       -> 0 
    PartitionAcc_OddSum        -> 0 
    PartitionAcc_AccSum        -> 0 
    PartitionAcc_AccRevSum     -> 0 
    PartitionAcc_CentralO      -> 0 
    PartitionAcc_PosHalf       -> 0 
    PartitionAcc_NegHalf       -> 0 
    PartitionAcc_TransNat0     -> 0 
    PartitionAcc_TransNat1     -> 0 
    PartitionAcc_TransSqrs     -> 0 
    PartitionAcc_BinConv       -> 0 
    PartitionAcc_InvBinConv    -> 0 
    PartitionAcc_PolyCol2      -> 0 
    PartitionAcc_PolyCol3      -> 0 
    PartitionAcc_PolyDiag      -> 0 
    PartitionAcc_RevToff11     -> 0 
    PartitionAcc_RevTrev11     -> 0 
    PartitionAcc_RevTantidiag  -> 0 
    PartitionAcc_RevTacc       -> 0 
    PartitionAcc_RevTalt       -> 0 
    PartitionAcc_RevTder       -> 0 
    PartitionAcc_RevEvenSum    -> 0 
    PartitionAcc_RevOddSum     -> 0 
    PartitionAcc_RevAccRevSum  -> 0 
    PartitionAcc_RevAntiDSum   -> 0 
    PartitionAcc_RevPosHalf    -> 0 
    PartitionAcc_RevNegHalf    -> 0 
    PartitionAcc_RevTransNat0  -> 0 
    PartitionAcc_RevTransNat1  -> 0 
    PartitionAcc_RevTransSqrs  -> 0 
    PartitionAcc_RevPolyCol3   -> 0 
    PartitionAcc_RevPolyDiag   -> 0 
    PartitionAcc_TablCol0      -> https://oeis.org/A7
    PartitionAcc_TablCol1      -> https://oeis.org/A12
    PartitionAcc_TablGcd       -> https://oeis.org/A12
    PartitionAcc_RevPolyRow1   -> https://oeis.org/A12
    PartitionAcc_PolyRow1      -> https://oeis.org/A27
    PartitionAcc_RevPolyRow2   -> https://oeis.org/A27
    PartitionAcc_TablDiag0     -> https://oeis.org/A41
    PartitionAcc_TablMax       -> https://oeis.org/A41
    PartitionAcc_TablDiag1     -> https://oeis.org/A65
    PartitionAcc_TablCol3      -> https://oeis.org/A1399
    PartitionAcc_TablCol2      -> https://oeis.org/A4526
    PartitionAcc_TablDiag2     -> https://oeis.org/A7042
    PartitionAcc_PolyRow2      -> https://oeis.org/A14105
    PartitionAcc_Triangle      -> https://oeis.org/A26820
    PartitionAcc_Toff11        -> https://oeis.org/A26820
    PartitionAcc_AltSum        -> https://oeis.org/A46682
    PartitionAcc_TablSum       -> https://oeis.org/A58397
    PartitionAcc_AbsSum        -> https://oeis.org/A58397
    PartitionAcc_Trev11        -> https://oeis.org/A58400
    PartitionAcc_RevPolyRow3   -> https://oeis.org/A59100
    PartitionAcc_PolyRow3      -> https://oeis.org/A67389
    PartitionAcc_AntiDSum      -> https://oeis.org/A110618
    PartitionAcc_ColMiddle     -> https://oeis.org/A110618
    PartitionAcc_RevCentralO   -> https://oeis.org/A171985
    PartitionAcc_CentralE      -> https://oeis.org/A209816
    PartitionAcc_TablDiag3     -> https://oeis.org/A335323
    PartitionAcc_RevColMiddle  -> https://oeis.org/A336106
    PartitionAcc_Tinvrev11     -> https://oeis.org/A375383

    PartitionAcc: Distinct: 22, Hits: 28, Misses: 38
'''
