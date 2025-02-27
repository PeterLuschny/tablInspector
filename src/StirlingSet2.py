from functools import cache
from _tabltypes import Table

"""Stirling set numbers of second order.


[0] 1;
[1] 0, 0;
[2] 0, 1,   0;
[3] 0, 1,   0,    0;
[4] 0, 1,   3,    0,    0;
[5] 0, 1,  10,    0,    0,  0;
[6] 0, 1,  25,   15,    0,  0,  0;
[7] 0, 1,  56,  105,    0,  0,  0,  0;
[8] 0, 1, 119,  490,  105,  0,  0,  0,  0;
[9] 0, 1, 246, 1918, 1260,  0,  0,  0,  0,  0;
"""


@cache
def stirlingset2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 0]

    rov = stirlingset2(n - 2)
    row = stirlingset2(n - 1) + [0]
    for k in range(1, n // 2 + 1):
        row[k] = (n - 1) * rov[k - 1] + k * row[k]

    return row


StirlingSet2 = Table(
    stirlingset2,
    "StirlingSet2",
    ["A358623", "A008299", "A137375"],
    "",
    r"\sum_{j=0}^{k} (-1)^{k-j} \binom{n}{k-j} {n-k+j \brace j}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(StirlingSet2)






''' OEIS
    StirlingSet2_Trev          -> 0 
    StirlingSet2_Toff11        -> 0 
    StirlingSet2_Trev11        -> 0 
    StirlingSet2_Tantidiag     -> 0 
    StirlingSet2_Tacc          -> 0 
    StirlingSet2_Tder          -> 0 
    StirlingSet2_TablDiag2     -> 0 
    StirlingSet2_TablDiag3     -> 0 
    StirlingSet2_TablLcm       -> 0 
    StirlingSet2_TablGcd       -> 0 
    StirlingSet2_TablMax       -> 0 
    StirlingSet2_AccSum        -> 0 
    StirlingSet2_AccRevSum     -> 0 
    StirlingSet2_AntiDSum      -> 0 
    StirlingSet2_TransNat0     -> 0 
    StirlingSet2_TransNat1     -> 0 
    StirlingSet2_TransSqrs     -> 0 
    StirlingSet2_BinConv       -> 0 
    StirlingSet2_InvBinConv    -> 0 
    StirlingSet2_RevToff11     -> 0 
    StirlingSet2_RevTrev11     -> 0 
    StirlingSet2_RevTantidiag  -> 0 
    StirlingSet2_RevTacc       -> 0 
    StirlingSet2_RevTalt       -> 0 
    StirlingSet2_RevTder       -> 0 
    StirlingSet2_RevEvenSum    -> 0 
    StirlingSet2_RevOddSum     -> 0 
    StirlingSet2_RevAccRevSum  -> 0 
    StirlingSet2_RevAntiDSum   -> 0 
    StirlingSet2_RevNegHalf    -> 0 
    StirlingSet2_RevTransNat0  -> 0 
    StirlingSet2_RevTransNat1  -> 0 
    StirlingSet2_RevTransSqrs  -> 0 
    StirlingSet2_PolyRow1      -> https://oeis.org/A4
    StirlingSet2_RevCentralO   -> https://oeis.org/A4
    StirlingSet2_RevPolyRow1   -> https://oeis.org/A4
    StirlingSet2_TablCol0      -> https://oeis.org/A7
    StirlingSet2_TablDiag0     -> https://oeis.org/A7
    StirlingSet2_TablCol1      -> https://oeis.org/A12
    StirlingSet2_PolyRow2      -> https://oeis.org/A27
    StirlingSet2_PolyRow3      -> https://oeis.org/A27
    StirlingSet2_RevPolyRow2   -> https://oeis.org/A27
    StirlingSet2_TablCol2      -> https://oeis.org/A247
    StirlingSet2_RevPolyRow3   -> https://oeis.org/A290
    StirlingSet2_TablSum       -> https://oeis.org/A296
    StirlingSet2_AbsSum        -> https://oeis.org/A296
    StirlingSet2_CentralO      -> https://oeis.org/A457
    StirlingSet2_TablCol3      -> https://oeis.org/A478
    StirlingSet2_AltSum        -> https://oeis.org/A587
    StirlingSet2_CentralE      -> https://oeis.org/A1147
    StirlingSet2_OddSum        -> https://oeis.org/A97762
    StirlingSet2_EvenSum       -> https://oeis.org/A97763
    StirlingSet2_RevColMiddle  -> https://oeis.org/A123023
    StirlingSet2_PolyCol2      -> https://oeis.org/A194689
    StirlingSet2_RevPosHalf    -> https://oeis.org/A194689
    StirlingSet2_TablDiag1     -> https://oeis.org/A209229
    StirlingSet2_ColMiddle     -> https://oeis.org/A259877
    StirlingSet2_NegHalf       -> https://oeis.org/A334190
    StirlingSet2_PosHalf       -> https://oeis.org/A337038
    StirlingSet2_RevPolyCol3   -> https://oeis.org/A337039
    StirlingSet2_RevPolyDiag   -> https://oeis.org/A337043
    StirlingSet2_PolyDiag      -> https://oeis.org/A337057
    StirlingSet2_Triangle      -> https://oeis.org/A358623
    StirlingSet2_Talt          -> https://oeis.org/A358623
    StirlingSet2_PolyCol3      -> https://oeis.org/A367890

    StirlingSet2: Distinct: 25, Hits: 32, Misses: 33
'''
