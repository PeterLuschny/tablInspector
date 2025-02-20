from functools import cache
from _tabltypes import Table

"""Stirling set B-type.


[0]     1;
[1]     1,     1;
[2]     3,     4,     1;
[3]    11,    19,     9,     1;
[4]    49,   104,    70,    16,    1;
[5]   257,   641,   550,   190,   25,   1;
[6]  1539,  4380,  4531,  2080,  425,  36,  1;
[7] 10299, 32803, 39515, 22491, 6265, 833, 49, 1;
"""


@cache
def stirlingsetb(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    pow = stirlingsetb(n - 1)
    row = stirlingsetb(n - 1) + [1]

    row[0] += 2 * row[1]

    for k in range(1, n - 1):
        row[k] = 2 * (k + 1) * pow[k + 1] + (2 * k + 1) * pow[k] + pow[k - 1]

    row[n - 1] = (2 * n - 1) * pow[n - 1] + pow[n - 2]
    return row


StirlingSetB = Table(
    stirlingsetb,
    "StirlingSetB",
    ["A154602"],
    "A000000",
    r"\sum_{j=k}^{n} 2^{n-j} \binom{j}{k} {n \brace j}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(StirlingSetB)






''' OEIS
    StirlingSetB_Tinv          -> 0 
    StirlingSetB_Trev          -> 0 
    StirlingSetB_Trevinv       -> 0 
    StirlingSetB_Toff11        -> 0 
    StirlingSetB_Trev11        -> 0 
    StirlingSetB_Tinv11        -> 0 
    StirlingSetB_Trevinv11     -> 0 
    StirlingSetB_Tantidiag     -> 0 
    StirlingSetB_Tacc          -> 0 
    StirlingSetB_Tder          -> 0 
    StirlingSetB_TablCol1      -> 0 
    StirlingSetB_TablCol2      -> 0 
    StirlingSetB_TablCol3      -> 0 
    StirlingSetB_TablDiag2     -> 0 
    StirlingSetB_TablDiag3     -> 0 
    StirlingSetB_TablLcm       -> 0 
    StirlingSetB_TablMax       -> 0 
    StirlingSetB_EvenSum       -> 0 
    StirlingSetB_OddSum        -> 0 
    StirlingSetB_AccSum        -> 0 
    StirlingSetB_AccRevSum     -> 0 
    StirlingSetB_AntiDSum      -> 0 
    StirlingSetB_ColMiddle     -> 0 
    StirlingSetB_CentralE      -> 0 
    StirlingSetB_CentralO      -> 0 
    StirlingSetB_PosHalf       -> 0 
    StirlingSetB_TransNat0     -> 0 
    StirlingSetB_TransNat1     -> 0 
    StirlingSetB_TransSqrs     -> 0 
    StirlingSetB_BinConv       -> 0 
    StirlingSetB_InvBinConv    -> 0 
    StirlingSetB_PolyRow3      -> 0 
    StirlingSetB_PolyCol2      -> 0 
    StirlingSetB_PolyDiag      -> 0 
    StirlingSetB_RevToff11     -> 0 
    StirlingSetB_RevTrev11     -> 0 
    StirlingSetB_RevTantidiag  -> 0 
    StirlingSetB_RevTacc       -> 0 
    StirlingSetB_RevTalt       -> 0 
    StirlingSetB_RevTder       -> 0 
    StirlingSetB_RevEvenSum    -> 0 
    StirlingSetB_RevOddSum     -> 0 
    StirlingSetB_RevAccRevSum  -> 0 
    StirlingSetB_RevAntiDSum   -> 0 
    StirlingSetB_RevColMiddle  -> 0 
    StirlingSetB_RevCentralO   -> 0 
    StirlingSetB_RevPosHalf    -> 0 
    StirlingSetB_RevTransNat0  -> 0 
    StirlingSetB_RevTransNat1  -> 0 
    StirlingSetB_RevTransSqrs  -> 0 
    StirlingSetB_RevPolyRow3   -> 0 
    StirlingSetB_RevPolyCol3   -> 0 
    StirlingSetB_RevPolyDiag   -> 0 
    StirlingSetB_AltSum        -> https://oeis.org/A7
    StirlingSetB_TablDiag0     -> https://oeis.org/A12
    StirlingSetB_TablGcd       -> https://oeis.org/A12
    StirlingSetB_PolyRow1      -> https://oeis.org/A27
    StirlingSetB_RevPolyRow1   -> https://oeis.org/A27
    StirlingSetB_TablDiag1     -> https://oeis.org/A290
    StirlingSetB_RevPolyRow2   -> https://oeis.org/A567
    StirlingSetB_TablCol0      -> https://oeis.org/A4211
    StirlingSetB_NegHalf       -> https://oeis.org/A4213
    StirlingSetB_PolyRow2      -> https://oeis.org/A5563
    StirlingSetB_RevNegHalf    -> https://oeis.org/A9235
    StirlingSetB_TablSum       -> https://oeis.org/A55882
    StirlingSetB_AbsSum        -> https://oeis.org/A55882
    StirlingSetB_Triangle      -> https://oeis.org/A154602
    StirlingSetB_Talt          -> https://oeis.org/A154602
    StirlingSetB_PolyCol3      -> https://oeis.org/A308543

    StirlingSetB: Distinct: 13, Hits: 16, Misses: 53
'''
