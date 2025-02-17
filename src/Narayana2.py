from functools import cache
from _tabltypes import Table

"""
[0] [1]
[1] [0, 1]
[2] [0, 1,  1]
[3] [0, 1,  2,   1]
[4] [0, 1,  4,   4,   1]
[5] [0, 1,  7,  12,   7,   1]
[6] [0, 1, 11,  30,  30,  11,   1]
[7] [0, 1, 16,  65, 100,  65,  16,   1]
[8] [0, 1, 22, 126, 280, 280, 126,  22,  1]
[9] [0, 1, 29, 224, 686, 980, 686, 224, 29, 1]
"""

@cache
def narayana2(n: int) -> list[int]:

    if n < 3: return ([1], [0, 1], [0, 1, 1])[n]

    a = narayana2(n - 2) + [0, 0]
    b = narayana2(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        b[k] = (((b[k] + b[k - 1]) * (2 * n - 3)
               - (a[k] - 2 * a[k - 1] + a[k - 2]) * (n - 3)) // n)
    return b


Narayana2 = Table(
    narayana2,
    "Narayana2",
    ["A352687"],
    "A000000",
    r"%%",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Narayana2)




''' OEIS
    Narayana2_Talt          -> https://oeis.org/A-999999
    Narayana2_AltSum        -> https://oeis.org/A-999999
    Narayana2_Tinv          -> 0 
    Narayana2_Trevinv       -> 0 
    Narayana2_Toff11        -> 0 
    Narayana2_Trev11        -> 0 
    Narayana2_Tinv11        -> 0 
    Narayana2_Tinvrev11     -> 0 
    Narayana2_Trevinv11     -> 0 
    Narayana2_Tantidiag     -> 0 
    Narayana2_Tacc          -> 0 
    Narayana2_Tder          -> 0 
    Narayana2_TablCol3      -> 0 
    Narayana2_TablDiag2     -> 0 
    Narayana2_TablDiag3     -> 0 
    Narayana2_TablLcm       -> 0 
    Narayana2_TablGcd       -> 0 
    Narayana2_TablMax       -> 0 
    Narayana2_AccRevSum     -> 0 
    Narayana2_AntiDSum      -> 0 
    Narayana2_ColMiddle     -> 0 
    Narayana2_CentralO      -> 0 
    Narayana2_TransNat1     -> 0 
    Narayana2_TransSqrs     -> 0 
    Narayana2_BinConv       -> 0 
    Narayana2_InvBinConv    -> 0 
    Narayana2_PolyCol2      -> 0 
    Narayana2_PolyCol3      -> 0 
    Narayana2_PolyDiag      -> 0 
    Narayana2_RevToff11     -> 0 
    Narayana2_RevTrev11     -> 0 
    Narayana2_RevTantidiag  -> 0 
    Narayana2_RevTacc       -> 0 
    Narayana2_RevTalt       -> 0 
    Narayana2_RevTder       -> 0 
    Narayana2_RevAntiDSum   -> 0 
    Narayana2_RevColMiddle  -> 0 
    Narayana2_RevPosHalf    -> 0 
    Narayana2_RevTransSqrs  -> 0 
    Narayana2_RevPolyCol3   -> 0 
    Narayana2_RevPolyDiag   -> 0 
    Narayana2_TablCol0      -> https://oeis.org/A7
    Narayana2_TablCol1      -> https://oeis.org/A12
    Narayana2_TablDiag0     -> https://oeis.org/A12
    Narayana2_RevPolyRow1   -> https://oeis.org/A12
    Narayana2_PolyRow1      -> https://oeis.org/A27
    Narayana2_RevPolyRow2   -> https://oeis.org/A27
    Narayana2_EvenSum       -> https://oeis.org/A108
    Narayana2_OddSum        -> https://oeis.org/A108
    Narayana2_RevEvenSum    -> https://oeis.org/A108
    Narayana2_RevOddSum     -> https://oeis.org/A108
    Narayana2_TablCol2      -> https://oeis.org/A124
    Narayana2_TablDiag1     -> https://oeis.org/A124
    Narayana2_RevPolyRow3   -> https://oeis.org/A290
    Narayana2_RevCentralO   -> https://oeis.org/A888
    Narayana2_RevTransNat0  -> https://oeis.org/A1791
    Narayana2_PolyRow2      -> https://oeis.org/A2378
    Narayana2_AccSum        -> https://oeis.org/A38665
    Narayana2_TransNat0     -> https://oeis.org/A38665
    Narayana2_RevAccRevSum  -> https://oeis.org/A38665
    Narayana2_RevTransNat1  -> https://oeis.org/A38665
    Narayana2_PolyRow3      -> https://oeis.org/A45991
    Narayana2_TablSum       -> https://oeis.org/A68875
    Narayana2_AbsSum        -> https://oeis.org/A68875
    Narayana2_NegHalf       -> https://oeis.org/A91593
    Narayana2_RevNegHalf    -> https://oeis.org/A152681
    Narayana2_CentralE      -> https://oeis.org/A172392
    Narayana2_PosHalf       -> https://oeis.org/A238113
    Narayana2_Triangle      -> https://oeis.org/A352687
    Narayana2_Trev          -> https://oeis.org/A352687

    Narayana2: Distinct: 19, Hits: 31, Misses: 39
'''
