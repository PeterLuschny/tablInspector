from functools import cache
from _tabltypes import Table

"""Stirling cycle B-type.

[0]      1;
[1]      1,      1;
[2]      3,      4,      1;
[3]     15,     23,      9,     1;
[4]    105,    176,     86,    16,     1;
[5]    945,   1689,    950,   230,    25,   1;
[6]  10395,  19524,  12139,  3480,   505,  36,  1;
[7] 135135, 264207, 177331, 57379, 10045, 973, 49, 1;
"""


@cache
def stirlingcycleb(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = stirlingcycleb(n - 1) + [1]

    m = 2 * n - 1
    for k in range(n - 1, 0, -1):
        row[k] = m * row[k] + row[k - 1]
    row[0] *= m

    return row


StirlingCycleB = Table(
    stirlingcycleb,
    "StirlingCycleB",
    ["A028338", "A039757", "A039758", "A109692"],
    "A000000",
    r"\sum_{i=k}^{n} (-2)^{n-i} \binom{i}{k} {n \brack i}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(StirlingCycleB)


''' OEIS
    StirlingCycleB_Toff11        -> 0 
    StirlingCycleB_Trev11        -> 0 
    StirlingCycleB_Tinv11        -> 0 
    StirlingCycleB_Tantidiag     -> 0 
    StirlingCycleB_Tacc          -> 0 
    StirlingCycleB_Tder          -> 0 
    StirlingCycleB_TablLcm       -> 0 
    StirlingCycleB_AccSum        -> 0 
    StirlingCycleB_AccRevSum     -> 0 
    StirlingCycleB_AntiDSum      -> 0 
    StirlingCycleB_ColMiddle     -> 0 
    StirlingCycleB_CentralO      -> 0 
    StirlingCycleB_TransNat1     -> 0 
    StirlingCycleB_TransSqrs     -> 0 
    StirlingCycleB_BinConv       -> 0 
    StirlingCycleB_InvBinConv    -> 0 
    StirlingCycleB_RevToff11     -> 0 
    StirlingCycleB_RevTrev11     -> 0 
    StirlingCycleB_RevTantidiag  -> 0 
    StirlingCycleB_RevTacc       -> 0 
    StirlingCycleB_RevTder       -> 0 
    StirlingCycleB_RevAccRevSum  -> 0 
    StirlingCycleB_RevColMiddle  -> 0 
    StirlingCycleB_RevCentralO   -> 0 
    StirlingCycleB_RevTransNat1  -> 0 
    StirlingCycleB_RevTransSqrs  -> 0 
    StirlingCycleB_RevPolyRow3   -> 0 
    StirlingCycleB_RevPolyDiag   -> 0 
    StirlingCycleB_AltSum        -> https://oeis.org/A7
    StirlingCycleB_TablDiag0     -> https://oeis.org/A12
    StirlingCycleB_TablGcd       -> https://oeis.org/A12
    StirlingCycleB_PolyRow1      -> https://oeis.org/A27
    StirlingCycleB_RevPolyRow1   -> https://oeis.org/A27
    StirlingCycleB_TablSum       -> https://oeis.org/A165
    StirlingCycleB_AbsSum        -> https://oeis.org/A165
    StirlingCycleB_TablDiag1     -> https://oeis.org/A290
    StirlingCycleB_RevPolyRow2   -> https://oeis.org/A567
    StirlingCycleB_TablCol0      -> https://oeis.org/A1147
    StirlingCycleB_PolyCol2      -> https://oeis.org/A1147
    StirlingCycleB_RevNegHalf    -> https://oeis.org/A1147
    StirlingCycleB_EvenSum       -> https://oeis.org/A2866
    StirlingCycleB_OddSum        -> https://oeis.org/A2866
    StirlingCycleB_PolyCol3      -> https://oeis.org/A2866
    StirlingCycleB_RevEvenSum    -> https://oeis.org/A2866
    StirlingCycleB_RevOddSum     -> https://oeis.org/A2866
    StirlingCycleB_TablCol1      -> https://oeis.org/A4041
    StirlingCycleB_TablMax       -> https://oeis.org/A4041
    StirlingCycleB_PolyRow2      -> https://oeis.org/A5563
    StirlingCycleB_NegHalf       -> https://oeis.org/A7696
    StirlingCycleB_PosHalf       -> https://oeis.org/A8545
    StirlingCycleB_TablDiag2     -> https://oeis.org/A24196
    StirlingCycleB_TablDiag3     -> https://oeis.org/A24197
    StirlingCycleB_Triangle      -> https://oeis.org/A28338
    StirlingCycleB_Talt          -> https://oeis.org/A28338
    StirlingCycleB_TablCol2      -> https://oeis.org/A28339
    StirlingCycleB_TablCol3      -> https://oeis.org/A28340
    StirlingCycleB_Tinv          -> https://oeis.org/A39755
    StirlingCycleB_RevPolyCol3   -> https://oeis.org/A49308
    StirlingCycleB_Trev          -> https://oeis.org/A109692
    StirlingCycleB_RevTalt       -> https://oeis.org/A109692
    StirlingCycleB_RevTransNat0  -> https://oeis.org/A197130
    StirlingCycleB_RevAntiDSum   -> https://oeis.org/A202153
    StirlingCycleB_TransNat0     -> https://oeis.org/A203159
    StirlingCycleB_CentralE      -> https://oeis.org/A293318
    StirlingCycleB_PolyRow3      -> https://oeis.org/A370912
    StirlingCycleB_PolyDiag      -> https://oeis.org/A374866

    StirlingCycleB: Distinct: 27, Hits: 38, Misses: 28
'''
