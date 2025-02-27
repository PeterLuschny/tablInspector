from functools import cache
from _tabltypes import Table

"""Central set factorial numbers.

[0] [1]
[1] [0, 1]
[2] [0, 1,    1]
[3] [0, 1,    5,      1]
[4] [0, 1,   21,     14,      1]
[5] [0, 1,   85,    147,     30,     1]
[6] [0, 1,  341,   1408,    627,    55,    1]
[7] [0, 1, 1365,  13013,  11440,  2002,   91,   1]
[8] [0, 1, 5461, 118482, 196053, 61490, 5278, 140,  1]
"""


@cache
def centralset(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = centralset(n - 1) + [1]
    for k in range(n - 1, 1, -1):
        row[k] = k**2 * row[k] + row[k - 1]
    return row


CentralSet = Table(
    centralset,
    "CentralSet",
    ["A269945", "A008957", "A036969"],
    "A269944",  # also "A204579"
    r"is(k = n)\ ? \ 1 : T(n-1, k-1) + k^2\ T(n-1, k)",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(CentralSet)






''' OEIS
    CentralSet_Trev          -> 0 
    CentralSet_Trevinv       -> 0 
    CentralSet_Tinvrev11     -> 0 
    CentralSet_Tantidiag     -> 0 
    CentralSet_Tacc          -> 0 
    CentralSet_Tder          -> 0 
    CentralSet_TablLcm       -> 0 
    CentralSet_TablMax       -> 0 
    CentralSet_EvenSum       -> 0 
    CentralSet_OddSum        -> 0 
    CentralSet_AltSum        -> 0 
    CentralSet_AccSum        -> 0 
    CentralSet_AccRevSum     -> 0 
    CentralSet_AntiDSum      -> 0 
    CentralSet_ColMiddle     -> 0 
    CentralSet_CentralO      -> 0 
    CentralSet_PosHalf       -> 0 
    CentralSet_NegHalf       -> 0 
    CentralSet_TransNat0     -> 0 
    CentralSet_TransNat1     -> 0 
    CentralSet_TransSqrs     -> 0 
    CentralSet_BinConv       -> 0 
    CentralSet_InvBinConv    -> 0 
    CentralSet_PolyRow3      -> 0 
    CentralSet_PolyCol2      -> 0 
    CentralSet_PolyCol3      -> 0 
    CentralSet_PolyDiag      -> 0 
    CentralSet_RevToff11     -> 0 
    CentralSet_RevTrev11     -> 0 
    CentralSet_RevTantidiag  -> 0 
    CentralSet_RevTacc       -> 0 
    CentralSet_RevTalt       -> 0 
    CentralSet_RevTder       -> 0 
    CentralSet_RevEvenSum    -> 0 
    CentralSet_RevOddSum     -> 0 
    CentralSet_RevAccRevSum  -> 0 
    CentralSet_RevAntiDSum   -> 0 
    CentralSet_RevColMiddle  -> 0 
    CentralSet_RevCentralO   -> 0 
    CentralSet_RevPosHalf    -> 0 
    CentralSet_RevNegHalf    -> 0 
    CentralSet_RevTransNat0  -> 0 
    CentralSet_RevTransNat1  -> 0 
    CentralSet_RevTransSqrs  -> 0 
    CentralSet_RevPolyCol3   -> 0 
    CentralSet_RevPolyDiag   -> 0 
    CentralSet_TablCol0      -> https://oeis.org/A7
    CentralSet_TablCol1      -> https://oeis.org/A12
    CentralSet_TablDiag0     -> https://oeis.org/A12
    CentralSet_RevPolyRow1   -> https://oeis.org/A12
    CentralSet_PolyRow1      -> https://oeis.org/A27
    CentralSet_RevPolyRow2   -> https://oeis.org/A27
    CentralSet_TablDiag1     -> https://oeis.org/A330
    CentralSet_PolyRow2      -> https://oeis.org/A2378
    CentralSet_TablCol2      -> https://oeis.org/A2450
    CentralSet_TablCol3      -> https://oeis.org/A2451
    CentralSet_Trevinv11     -> https://oeis.org/A8955
    CentralSet_Trev11        -> https://oeis.org/A8957
    CentralSet_Toff11        -> https://oeis.org/A36969
    CentralSet_TablDiag2     -> https://oeis.org/A60493
    CentralSet_RevPolyRow3   -> https://oeis.org/A82111
    CentralSet_TablGcd       -> https://oeis.org/A128059
    CentralSet_TablSum       -> https://oeis.org/A135920
    CentralSet_AbsSum        -> https://oeis.org/A135920
    CentralSet_Tinv11        -> https://oeis.org/A204579
    CentralSet_Tinv          -> https://oeis.org/A269944
    CentralSet_Triangle      -> https://oeis.org/A269945
    CentralSet_Talt          -> https://oeis.org/A269945
    CentralSet_CentralE      -> https://oeis.org/A298851
    CentralSet_TablDiag3     -> https://oeis.org/A351105

    CentralSet: Distinct: 20, Hits: 24, Misses: 46
'''
