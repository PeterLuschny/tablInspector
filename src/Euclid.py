from functools import cache
from _tabltypes import Table

"""Euclid's triangle.

[ 0] [0]
[ 1] [1, 1]
[ 2] [0, 1, 0]
[ 3] [0, 1, 1, 0]
[ 4] [0, 1, 0, 1, 0]
[ 5] [0, 1, 1, 1, 1, 0]
[ 6] [0, 1, 0, 0, 0, 1, 0]
[ 7] [0, 1, 1, 1, 1, 1, 1, 0]
[ 8] [0, 1, 0, 1, 0, 1, 0, 1, 0]
[ 9] [0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
[10] [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
[11] [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
"""


@cache
def _euclid(n: int, k: int) -> int:
    while k != 0:
        t = k
        k = n % k
        n = t
    return 1 if n == 1 else 0


@cache
def euclid(n: int) -> list[int]:
    return [_euclid(i, n) for i in range(n + 1)]


Euclid = Table(
    euclid, 
    "Euclid", 
    ["A217831"], 
    "",
    r"is(k \text{ prime to } n ) \ ? \ 1 : 0"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Euclid)






''' OEIS
    Euclid_Tinvrev11     -> 0 
    Euclid_InvBinConv    -> 0 
    Euclid_PolyCol3      -> 0 
    Euclid_RevPolyCol3   -> 0 
    Euclid_TablSum       -> https://oeis.org/A10
    Euclid_AbsSum        -> https://oeis.org/A10
    Euclid_TablCol1      -> https://oeis.org/A12
    Euclid_TablDiag1     -> https://oeis.org/A12
    Euclid_TablLcm       -> https://oeis.org/A12
    Euclid_TablGcd       -> https://oeis.org/A12
    Euclid_TablMax       -> https://oeis.org/A12
    Euclid_CentralO      -> https://oeis.org/A12
    Euclid_RevCentralO   -> https://oeis.org/A12
    Euclid_PolyRow1      -> https://oeis.org/A27
    Euclid_PolyRow2      -> https://oeis.org/A27
    Euclid_RevPolyRow1   -> https://oeis.org/A27
    Euclid_RevPolyRow2   -> https://oeis.org/A27
    Euclid_TablCol2      -> https://oeis.org/A35
    Euclid_TablDiag2     -> https://oeis.org/A35
    Euclid_ColMiddle     -> https://oeis.org/A35
    Euclid_RevColMiddle  -> https://oeis.org/A35
    Euclid_PolyRow3      -> https://oeis.org/A2378
    Euclid_RevPolyRow3   -> https://oeis.org/A2378
    Euclid_TablCol3      -> https://oeis.org/A11655
    Euclid_TablDiag3     -> https://oeis.org/A11655
    Euclid_AntiDSum      -> https://oeis.org/A23022
    Euclid_RevAntiDSum   -> https://oeis.org/A23022
    Euclid_TransNat0     -> https://oeis.org/A23896
    Euclid_RevTransNat0  -> https://oeis.org/A23896
    Euclid_TransSqrs     -> https://oeis.org/A53818
    Euclid_RevTransSqrs  -> https://oeis.org/A53818
    Euclid_Toff11        -> https://oeis.org/A54521
    Euclid_Trev11        -> https://oeis.org/A54521
    Euclid_RevToff11     -> https://oeis.org/A54521
    Euclid_RevTrev11     -> https://oeis.org/A54521
    Euclid_OddSum        -> https://oeis.org/A55034
    Euclid_RevOddSum     -> https://oeis.org/A55034
    Euclid_BinConv       -> https://oeis.org/A56188
    Euclid_AltSum        -> https://oeis.org/A62570
    Euclid_AccSum        -> https://oeis.org/A92790
    Euclid_AccRevSum     -> https://oeis.org/A92790
    Euclid_TransNat1     -> https://oeis.org/A92790
    Euclid_RevAccRevSum  -> https://oeis.org/A92790
    Euclid_RevTransNat1  -> https://oeis.org/A92790
    Euclid_Tder          -> https://oeis.org/A127368
    Euclid_RevTder       -> https://oeis.org/A127368
    Euclid_TablCol0      -> https://oeis.org/A209229
    Euclid_TablDiag0     -> https://oeis.org/A209229
    Euclid_CentralE      -> https://oeis.org/A209229
    Euclid_Triangle      -> https://oeis.org/A217831
    Euclid_Trev          -> https://oeis.org/A217831
    Euclid_Talt          -> https://oeis.org/A217831
    Euclid_RevTalt       -> https://oeis.org/A217831
    Euclid_EvenSum       -> https://oeis.org/A349136
    Euclid_RevEvenSum    -> https://oeis.org/A349136
    Euclid_Tantidiag     -> https://oeis.org/A359592
    Euclid_RevTantidiag  -> https://oeis.org/A359592
    Euclid_PosHalf       -> https://oeis.org/A367544
    Euclid_PolyCol2      -> https://oeis.org/A367544
    Euclid_RevPosHalf    -> https://oeis.org/A367544
    Euclid_NegHalf       -> https://oeis.org/A367545
    Euclid_RevNegHalf    -> https://oeis.org/A367545
    Euclid_PolyDiag      -> https://oeis.org/A367546
    Euclid_RevPolyDiag   -> https://oeis.org/A367546
    Euclid_Tacc          -> https://oeis.org/A378068
    Euclid_RevTacc       -> https://oeis.org/A378068

    Euclid: Distinct: 24, Hits: 62, Misses: 4
'''
