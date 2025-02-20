from functools import cache
from _tabltypes import Table

"""Leibniz's Table, multiplication table read by antidiagonals.

[0]  0
[1]  0   1
[2]  0   2    2
[3]  0   3    4   3
[4]  0   4    6   6    4
[5]  0   5    8   9    8    5
[6]  0   6   10  12   12   10    6
[7]  0   7   12  15   16   15   12    7
[8]  0   8   14  18   20   20   18   14   8
[9]  0   9   16  21   24   25   24   21  16  9
"""

@cache
def leibniztable(n: int) -> list[int]:
    if n == 0: return [0]
    L = leibniztable(n - 1)
    return [L[k] + k for k in range(n)] + [n]

LeibnizTable = Table(
    leibniztable, 
    "LeibnizTable", 
    ["A003991"], 
    "", 
    r"k\,(n - k + 1)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(LeibnizTable)






''' OEIS
    LeibnizTable_Tantidiag     -> 0 
    LeibnizTable_Tacc          -> 0 
    LeibnizTable_Tder          -> 0 
    LeibnizTable_PolyRow3      -> 0 
    LeibnizTable_PolyCol2      -> 0 
    LeibnizTable_PolyCol3      -> 0 
    LeibnizTable_PolyDiag      -> 0 
    LeibnizTable_RevToff11     -> 0 
    LeibnizTable_RevTrev11     -> 0 
    LeibnizTable_RevTantidiag  -> 0 
    LeibnizTable_RevTder       -> 0 
    LeibnizTable_RevPosHalf    -> 0 
    LeibnizTable_RevTransSqrs  -> 0 
    LeibnizTable_RevPolyDiag   -> 0 
    LeibnizTable_TablCol0      -> https://oeis.org/A4
    LeibnizTable_RevPolyRow1   -> https://oeis.org/A12
    LeibnizTable_TablCol1      -> https://oeis.org/A27
    LeibnizTable_TablDiag0     -> https://oeis.org/A27
    LeibnizTable_PolyRow1      -> https://oeis.org/A27
    LeibnizTable_TablGcd       -> https://oeis.org/A34
    LeibnizTable_RevCentralO   -> https://oeis.org/A290
    LeibnizTable_TablSum       -> https://oeis.org/A292
    LeibnizTable_AbsSum        -> https://oeis.org/A292
    LeibnizTable_BinConv       -> https://oeis.org/A1788
    LeibnizTable_CentralE      -> https://oeis.org/A2378
    LeibnizTable_AccSum        -> https://oeis.org/A2415
    LeibnizTable_TransNat0     -> https://oeis.org/A2415
    LeibnizTable_RevAccRevSum  -> https://oeis.org/A2415
    LeibnizTable_RevTransNat1  -> https://oeis.org/A2415
    LeibnizTable_TablMax       -> https://oeis.org/A2620
    LeibnizTable_RevColMiddle  -> https://oeis.org/A2620
    LeibnizTable_Toff11        -> https://oeis.org/A3991
    LeibnizTable_Trev11        -> https://oeis.org/A3991
    LeibnizTable_CentralO      -> https://oeis.org/A5563
    LeibnizTable_TablCol2      -> https://oeis.org/A5843
    LeibnizTable_TablDiag1     -> https://oeis.org/A5843
    LeibnizTable_RevPolyRow2   -> https://oeis.org/A5843
    LeibnizTable_OddSum        -> https://oeis.org/A5993
    LeibnizTable_RevEvenSum    -> https://oeis.org/A5993
    LeibnizTable_EvenSum       -> https://oeis.org/A6584
    LeibnizTable_RevOddSum     -> https://oeis.org/A6584
    LeibnizTable_AntiDSum      -> https://oeis.org/A6918
    LeibnizTable_RevAntiDSum   -> https://oeis.org/A6918
    LeibnizTable_TablCol3      -> https://oeis.org/A8585
    LeibnizTable_TablDiag2     -> https://oeis.org/A8585
    LeibnizTable_TablDiag3     -> https://oeis.org/A8586
    LeibnizTable_TransSqrs     -> https://oeis.org/A24166
    LeibnizTable_AccRevSum     -> https://oeis.org/A34827
    LeibnizTable_TransNat1     -> https://oeis.org/A34827
    LeibnizTable_RevTransNat0  -> https://oeis.org/A34827
    LeibnizTable_ColMiddle     -> https://oeis.org/A35106
    LeibnizTable_PosHalf       -> https://oeis.org/A45618
    LeibnizTable_PolyRow2      -> https://oeis.org/A46092
    LeibnizTable_NegHalf       -> https://oeis.org/A73371
    LeibnizTable_Triangle      -> https://oeis.org/A94053
    LeibnizTable_Trev          -> https://oeis.org/A94053
    LeibnizTable_Talt          -> https://oeis.org/A94053
    LeibnizTable_RevTalt       -> https://oeis.org/A94053
    LeibnizTable_RevNegHalf    -> https://oeis.org/A95977
    LeibnizTable_RevTacc       -> https://oeis.org/A140765
    LeibnizTable_AltSum        -> https://oeis.org/A142150
    LeibnizTable_TablLcm       -> https://oeis.org/A169900
    LeibnizTable_RevPolyCol3   -> https://oeis.org/A212337
    LeibnizTable_InvBinConv    -> https://oeis.org/A245196
    LeibnizTable_RevPolyRow3   -> https://oeis.org/A271740

    LeibnizTable: Distinct: 33, Hits: 51, Misses: 14
'''
