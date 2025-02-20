from functools import cache
from _tabltypes import Table

"""Stirling cycle numbers, unsigned Stirling numbers of the 1. kind.


[0]  1
[1]  0,     1
[2]  0,     1,      1
[3]  0,     2,      3,      1
[4]  0,     6,     11,      6,     1
[5]  0,    24,     50,     35,    10,     1
[6]  0,   120,    274,    225,    85,    15,    1
[7]  0,   720,   1764,   1624,   735,   175,   21,   1
[8]  0,  5040,  13068,  13132,  6769,  1960,  322,  28,  1
[9]  0, 40320, 109584, 118124, 67284, 22449, 4536, 546, 36, 1
"""


@cache
def stirlingcycle(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [0] + stirlingcycle(n - 1)
    for k in range(1, n):
        row[k] = row[k] + (n - 1) * row[k + 1]

    return row


StirlingCycle = Table(
    stirlingcycle,
    "StirlingCycle",
    ["A132393", "A008275", "A008276", "A048994", "A054654", "A094638", "A130534"],
    "A000000",
    r"{n \brack k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(StirlingCycle)






''' OEIS
    StirlingCycle_RevToff11     -> 0 
    StirlingCycle_RevTrev11     -> 0 
    StirlingCycle_RevTantidiag  -> 0 
    StirlingCycle_RevTder       -> 0 
    StirlingCycle_RevColMiddle  -> 0 
    StirlingCycle_RevTransSqrs  -> 0 
    StirlingCycle_TablCol0      -> https://oeis.org/A7
    StirlingCycle_TablDiag0     -> https://oeis.org/A12
    StirlingCycle_TablGcd       -> https://oeis.org/A12
    StirlingCycle_RevPolyRow1   -> https://oeis.org/A12
    StirlingCycle_PolyRow1      -> https://oeis.org/A27
    StirlingCycle_RevPolyRow2   -> https://oeis.org/A27
    StirlingCycle_TablCol1      -> https://oeis.org/A142
    StirlingCycle_TablSum       -> https://oeis.org/A142
    StirlingCycle_AbsSum        -> https://oeis.org/A142
    StirlingCycle_PolyCol2      -> https://oeis.org/A142
    StirlingCycle_RevPosHalf    -> https://oeis.org/A142
    StirlingCycle_TablDiag1     -> https://oeis.org/A217
    StirlingCycle_TablCol2      -> https://oeis.org/A254
    StirlingCycle_TransNat0     -> https://oeis.org/A254
    StirlingCycle_RevPolyRow3   -> https://oeis.org/A384
    StirlingCycle_TablCol3      -> https://oeis.org/A399
    StirlingCycle_PolyDiag      -> https://oeis.org/A407
    StirlingCycle_AccRevSum     -> https://oeis.org/A774
    StirlingCycle_TransNat1     -> https://oeis.org/A774
    StirlingCycle_TablDiag2     -> https://oeis.org/A914
    StirlingCycle_PosHalf       -> https://oeis.org/A1147
    StirlingCycle_NegHalf       -> https://oeis.org/A1147
    StirlingCycle_TablDiag3     -> https://oeis.org/A1303
    StirlingCycle_EvenSum       -> https://oeis.org/A1710
    StirlingCycle_OddSum        -> https://oeis.org/A1710
    StirlingCycle_PolyCol3      -> https://oeis.org/A1710
    StirlingCycle_RevEvenSum    -> https://oeis.org/A1710
    StirlingCycle_RevOddSum     -> https://oeis.org/A1710
    StirlingCycle_PolyRow2      -> https://oeis.org/A2378
    StirlingCycle_PolyRow3      -> https://oeis.org/A7531
    StirlingCycle_RevPolyCol3   -> https://oeis.org/A7559
    StirlingCycle_Tinv11        -> https://oeis.org/A8277
    StirlingCycle_Trevinv11     -> https://oeis.org/A8278
    StirlingCycle_Tder          -> https://oeis.org/A28421
    StirlingCycle_RevNegHalf    -> https://oeis.org/A39972
    StirlingCycle_Tinv          -> https://oeis.org/A48993
    StirlingCycle_Talt          -> https://oeis.org/A48994
    StirlingCycle_Trev          -> https://oeis.org/A54654
    StirlingCycle_RevTalt       -> https://oeis.org/A54654
    StirlingCycle_TablLcm       -> https://oeis.org/A63039
    StirlingCycle_TablMax       -> https://oeis.org/A65048
    StirlingCycle_RevTransNat0  -> https://oeis.org/A67318
    StirlingCycle_RevPolyDiag   -> https://oeis.org/A92985
    StirlingCycle_Trev11        -> https://oeis.org/A94638
    StirlingCycle_RevTacc       -> https://oeis.org/A96747
    StirlingCycle_Trevinv       -> https://oeis.org/A106800
    StirlingCycle_AccSum        -> https://oeis.org/A121586
    StirlingCycle_RevAccRevSum  -> https://oeis.org/A121586
    StirlingCycle_RevTransNat1  -> https://oeis.org/A121586
    StirlingCycle_RevAntiDSum   -> https://oeis.org/A124380
    StirlingCycle_RevCentralO   -> https://oeis.org/A129505
    StirlingCycle_Toff11        -> https://oeis.org/A130534
    StirlingCycle_Triangle      -> https://oeis.org/A132393
    StirlingCycle_TransSqrs     -> https://oeis.org/A151881
    StirlingCycle_ColMiddle     -> https://oeis.org/A154415
    StirlingCycle_AltSum        -> https://oeis.org/A154955
    StirlingCycle_CentralE      -> https://oeis.org/A187646
    StirlingCycle_BinConv       -> https://oeis.org/A211210
    StirlingCycle_InvBinConv    -> https://oeis.org/A317274
    StirlingCycle_Tantidiag     -> https://oeis.org/A331327
    StirlingCycle_AntiDSum      -> https://oeis.org/A343579
    StirlingCycle_Tacc          -> https://oeis.org/A349782
    StirlingCycle_CentralO      -> https://oeis.org/A367777

    StirlingCycle: Distinct: 47, Hits: 63, Misses: 6
'''
