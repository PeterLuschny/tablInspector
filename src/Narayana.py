from functools import cache
from _tabltypes import Table


"""Narayana triangle.

[0]  1;
[1]  0,  1;
[2]  0,  1,   1;
[3]  0,  1,   3,    1;
[4]  0,  1,   6,    6,     1;
[5]  0,  1,  10,   20,    10,     1;
[6]  0,  1,  15,   50,    50,    15,     1;
[7]  0,  1,  21,  105,   175,   105,    21,    1;
[8]  0,  1,  28,  196,   490,   490,   196,   28,   1;
[9]  0,  1,  36,  336,  1176,  1764,  1176,  336,  36,  1;
"""


@cache
def narayana(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = narayana(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] += ((2*n - k) * row[k - 1]) // k 
    return row


Narayana = Table(
    narayana,
    "Narayana",
    ["A090181", "A001263", "A131198"],
    "A103364",
    r"\binom{n}{n-k} \binom{n-1}{n-k} \frac{1}{n-k+1}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Narayana)


''' OEIS
    Narayana_Tinv          -> 0 
    Narayana_Tantidiag     -> 0 
    Narayana_TablLcm       -> 0 
    Narayana_TablGcd       -> 0 
    Narayana_ColMiddle     -> 0 
    Narayana_BinConv       -> 0 
    Narayana_InvBinConv    -> 0 
    Narayana_PolyDiag      -> 0 
    Narayana_RevToff11     -> 0 
    Narayana_RevTrev11     -> 0 
    Narayana_RevTantidiag  -> 0 
    Narayana_RevTacc       -> 0 
    Narayana_RevTder       -> 0 
    Narayana_TablCol0      -> https://oeis.org/A7
    Narayana_TablCol1      -> https://oeis.org/A12
    Narayana_TablDiag0     -> https://oeis.org/A12
    Narayana_RevPolyRow1   -> https://oeis.org/A12
    Narayana_PolyRow1      -> https://oeis.org/A27
    Narayana_RevPolyRow2   -> https://oeis.org/A27
    Narayana_TablSum       -> https://oeis.org/A108
    Narayana_AbsSum        -> https://oeis.org/A108
    Narayana_TablCol2      -> https://oeis.org/A217
    Narayana_TablDiag1     -> https://oeis.org/A217
    Narayana_RevCentralO   -> https://oeis.org/A891
    Narayana_PosHalf       -> https://oeis.org/A1003
    Narayana_Toff11        -> https://oeis.org/A1263
    Narayana_Trev11        -> https://oeis.org/A1263
    Narayana_AccSum        -> https://oeis.org/A1700
    Narayana_TransNat0     -> https://oeis.org/A1700
    Narayana_RevAccRevSum  -> https://oeis.org/A1700
    Narayana_RevTransNat1  -> https://oeis.org/A1700
    Narayana_RevTransNat0  -> https://oeis.org/A2054
    Narayana_PolyRow2      -> https://oeis.org/A2378
    Narayana_TablCol3      -> https://oeis.org/A2415
    Narayana_TablDiag2     -> https://oeis.org/A2415
    Narayana_AntiDSum      -> https://oeis.org/A4148
    Narayana_RevAntiDSum   -> https://oeis.org/A4148
    Narayana_TablMax       -> https://oeis.org/A5558
    Narayana_RevColMiddle  -> https://oeis.org/A5558
    Narayana_PolyCol2      -> https://oeis.org/A6318
    Narayana_TablDiag3     -> https://oeis.org/A6542
    Narayana_RevPolyCol3   -> https://oeis.org/A7564
    Narayana_RevPolyRow3   -> https://oeis.org/A28387
    Narayana_PolyRow3      -> https://oeis.org/A33445
    Narayana_RevTransSqrs  -> https://oeis.org/A34267
    Narayana_CentralO      -> https://oeis.org/A46715
    Narayana_PolyCol3      -> https://oeis.org/A47891
    Narayana_OddSum        -> https://oeis.org/A71684
    Narayana_RevEvenSum    -> https://oeis.org/A71684
    Narayana_EvenSum       -> https://oeis.org/A71688
    Narayana_RevOddSum     -> https://oeis.org/A71688
    Narayana_Triangle      -> https://oeis.org/A90181
    Narayana_Trev          -> https://oeis.org/A90181
    Narayana_Talt          -> https://oeis.org/A90181
    Narayana_RevTalt       -> https://oeis.org/A90181
    Narayana_NegHalf       -> https://oeis.org/A91593
    Narayana_Tinv11        -> https://oeis.org/A103364
    Narayana_Tinvrev11     -> https://oeis.org/A103364
    Narayana_CentralE      -> https://oeis.org/A125558
    Narayana_AltSum        -> https://oeis.org/A126120
    Narayana_Tder          -> https://oeis.org/A132813
    Narayana_TransSqrs     -> https://oeis.org/A141222
    Narayana_RevNegHalf    -> https://oeis.org/A152681
    Narayana_AccRevSum     -> https://oeis.org/A189176
    Narayana_TransNat1     -> https://oeis.org/A189176
    Narayana_RevPolyDiag   -> https://oeis.org/A242369
    Narayana_Tacc          -> https://oeis.org/A349740

    Narayana: Distinct: 36, Hits: 54, Misses: 13
'''
