from functools import cache
from _tabltypes import Table

"""Stirling cycle numbers of second order.

[0]  1
[1]  0,     0
[2]  0,     1,     0
[3]  0,     2,     0,     0
[4]  0,     6,     3,     0,    0
[5]  0,    24,    20,     0,    0, 0
[6]  0,   120,   130,    15,    0, 0, 0
[7]  0,   720,   924,   210,    0, 0, 0, 0
[8]  0,  5040,  7308,  2380,  105, 0, 0, 0, 0
[9]  0, 40320, 64224, 26432, 2520, 0, 0, 0, 0, 0
"""


@cache
def stirlingcycle2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]

    rov = stirlingcycle2(n - 2)
    row = stirlingcycle2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * (rov[k - 1] + row[k])
    return row


StirlingCycle2 = Table(
    stirlingcycle2,
    "StirlingCycle2",
    ["A358622", "A008306", "A106828"],
    "",
    r"n! [z^k][t^n] (\exp(t) (1 - t))^{-z}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(StirlingCycle2)




''' OEIS
    StirlingCycle2_PolyRow1      -> https://oeis.org/A-999999
    StirlingCycle2_RevCentralO   -> https://oeis.org/A-999999
    StirlingCycle2_RevPolyRow1   -> https://oeis.org/A-999999
    StirlingCycle2_Trev          -> 0 
    StirlingCycle2_Toff11        -> 0 
    StirlingCycle2_Trev11        -> 0 
    StirlingCycle2_Tantidiag     -> 0 
    StirlingCycle2_Tacc          -> 0 
    StirlingCycle2_Tder          -> 0 
    StirlingCycle2_TablDiag3     -> 0 
    StirlingCycle2_TablLcm       -> 0 
    StirlingCycle2_TablMax       -> 0 
    StirlingCycle2_AccSum        -> 0 
    StirlingCycle2_AccRevSum     -> 0 
    StirlingCycle2_AntiDSum      -> 0 
    StirlingCycle2_ColMiddle     -> 0 
    StirlingCycle2_TransNat1     -> 0 
    StirlingCycle2_TransSqrs     -> 0 
    StirlingCycle2_BinConv       -> 0 
    StirlingCycle2_InvBinConv    -> 0 
    StirlingCycle2_RevToff11     -> 0 
    StirlingCycle2_RevTrev11     -> 0 
    StirlingCycle2_RevTantidiag  -> 0 
    StirlingCycle2_RevTacc       -> 0 
    StirlingCycle2_RevTalt       -> 0 
    StirlingCycle2_RevTder       -> 0 
    StirlingCycle2_RevAccRevSum  -> 0 
    StirlingCycle2_RevAntiDSum   -> 0 
    StirlingCycle2_RevNegHalf    -> 0 
    StirlingCycle2_RevTransNat0  -> 0 
    StirlingCycle2_RevTransNat1  -> 0 
    StirlingCycle2_RevTransSqrs  -> 0 
    StirlingCycle2_RevPolyDiag   -> 0 
    StirlingCycle2_TablCol0      -> https://oeis.org/A7
    StirlingCycle2_TablDiag0     -> https://oeis.org/A7
    StirlingCycle2_TablGcd       -> https://oeis.org/A27
    StirlingCycle2_AltSum        -> https://oeis.org/A27
    StirlingCycle2_PolyRow2      -> https://oeis.org/A27
    StirlingCycle2_RevPolyRow2   -> https://oeis.org/A27
    StirlingCycle2_TablCol1      -> https://oeis.org/A142
    StirlingCycle2_TablSum       -> https://oeis.org/A166
    StirlingCycle2_AbsSum        -> https://oeis.org/A166
    StirlingCycle2_TablCol2      -> https://oeis.org/A276
    StirlingCycle2_RevOddSum     -> https://oeis.org/A387
    StirlingCycle2_TablCol3      -> https://oeis.org/A483
    StirlingCycle2_CentralO      -> https://oeis.org/A906
    StirlingCycle2_RevPolyRow3   -> https://oeis.org/A1105
    StirlingCycle2_CentralE      -> https://oeis.org/A1147
    StirlingCycle2_RevEvenSum    -> https://oeis.org/A3221
    StirlingCycle2_PolyRow3      -> https://oeis.org/A5843
    StirlingCycle2_RevPolyCol3   -> https://oeis.org/A33030
    StirlingCycle2_PosHalf       -> https://oeis.org/A53871
    StirlingCycle2_NegHalf       -> https://oeis.org/A55142
    StirlingCycle2_PolyCol2      -> https://oeis.org/A87981
    StirlingCycle2_RevPosHalf    -> https://oeis.org/A87981
    StirlingCycle2_RevColMiddle  -> https://oeis.org/A123023
    StirlingCycle2_PolyCol3      -> https://oeis.org/A137775
    StirlingCycle2_TransNat0     -> https://oeis.org/A162973
    StirlingCycle2_TablDiag1     -> https://oeis.org/A209229
    StirlingCycle2_EvenSum       -> https://oeis.org/A216778
    StirlingCycle2_OddSum        -> https://oeis.org/A216779
    StirlingCycle2_TablDiag2     -> https://oeis.org/A281669
    StirlingCycle2_PolyDiag      -> https://oeis.org/A295182
    StirlingCycle2_Triangle      -> https://oeis.org/A358622
    StirlingCycle2_Talt          -> https://oeis.org/A358622

    StirlingCycle2: Distinct: 27, Hits: 35, Misses: 30
'''
