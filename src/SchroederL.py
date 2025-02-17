from functools import cache
from _tabltypes import Table

"""Little Schroeder triangle.

[0]      1;
[1]      1,      1;
[2]      3,      4,      1;
[3]     11,     17,      7,     1;
[4]     45,     76,     40,    10,     1;
[5]    197,    353,    216,    72,    13,     1;
[6]    903,   1688,   1345,   458,   113,    16,    1;
[7]   4279,   8257,   6039,  2745,   829,   163,   19,   1;
[8]  20793,  41128,  31864, 15932,  5558,  1356,  222,  22,  1;
[9] 103049, 207905, 168584, 90776, 35318, 10070, 2066, 290, 25, 1;
"""


@cache
def schroederl(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    arow = schroederl(n - 1) + [0]
    row = schroederl(n - 1) + [1]

    row[0] = row[0] + 2 * row[1]
    for k in range(1, n):
        row[k] = arow[k - 1] + 3 * arow[k] + 2 * arow[k + 1]

    return row


SchroederL = Table(
    schroederl, 
    "SchroederL", 
    ["A172094"], 
    "A000000", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(SchroederL)




''' OEIS
    SchroederL_Trev          -> 0 
    SchroederL_Trevinv       -> 0 
    SchroederL_Toff11        -> 0 
    SchroederL_Trev11        -> 0 
    SchroederL_Tinv11        -> 0 
    SchroederL_Trevinv11     -> 0 
    SchroederL_Tantidiag     -> 0 
    SchroederL_Tacc          -> 0 
    SchroederL_Tder          -> 0 
    SchroederL_TablCol2      -> 0 
    SchroederL_TablCol3      -> 0 
    SchroederL_TablDiag2     -> 0 
    SchroederL_TablDiag3     -> 0 
    SchroederL_TablLcm       -> 0 
    SchroederL_TablMax       -> 0 
    SchroederL_AccSum        -> 0 
    SchroederL_AccRevSum     -> 0 
    SchroederL_AntiDSum      -> 0 
    SchroederL_ColMiddle     -> 0 
    SchroederL_CentralE      -> 0 
    SchroederL_CentralO      -> 0 
    SchroederL_TransNat0     -> 0 
    SchroederL_TransNat1     -> 0 
    SchroederL_TransSqrs     -> 0 
    SchroederL_BinConv       -> 0 
    SchroederL_InvBinConv    -> 0 
    SchroederL_PolyRow3      -> 0 
    SchroederL_PolyCol2      -> 0 
    SchroederL_PolyCol3      -> 0 
    SchroederL_PolyDiag      -> 0 
    SchroederL_RevToff11     -> 0 
    SchroederL_RevTrev11     -> 0 
    SchroederL_RevTantidiag  -> 0 
    SchroederL_RevTacc       -> 0 
    SchroederL_RevTalt       -> 0 
    SchroederL_RevTder       -> 0 
    SchroederL_RevAccRevSum  -> 0 
    SchroederL_RevAntiDSum   -> 0 
    SchroederL_RevColMiddle  -> 0 
    SchroederL_RevCentralO   -> 0 
    SchroederL_RevPosHalf    -> 0 
    SchroederL_RevTransNat0  -> 0 
    SchroederL_RevTransNat1  -> 0 
    SchroederL_RevTransSqrs  -> 0 
    SchroederL_RevPolyRow3   -> 0 
    SchroederL_RevPolyCol3   -> 0 
    SchroederL_RevPolyDiag   -> 0 
    SchroederL_AltSum        -> https://oeis.org/A7
    SchroederL_TablDiag0     -> https://oeis.org/A12
    SchroederL_TablGcd       -> https://oeis.org/A12
    SchroederL_PolyRow1      -> https://oeis.org/A27
    SchroederL_RevPolyRow1   -> https://oeis.org/A27
    SchroederL_RevPolyRow2   -> https://oeis.org/A567
    SchroederL_TablCol0      -> https://oeis.org/A1003
    SchroederL_RevNegHalf    -> https://oeis.org/A1003
    SchroederL_PolyRow2      -> https://oeis.org/A5563
    SchroederL_TablDiag1     -> https://oeis.org/A16777
    SchroederL_TablSum       -> https://oeis.org/A109980
    SchroederL_AbsSum        -> https://oeis.org/A109980
    SchroederL_Triangle      -> https://oeis.org/A172094
    SchroederL_Talt          -> https://oeis.org/A172094
    SchroederL_EvenSum       -> https://oeis.org/A225887
    SchroederL_OddSum        -> https://oeis.org/A225887
    SchroederL_RevEvenSum    -> https://oeis.org/A225887
    SchroederL_RevOddSum     -> https://oeis.org/A225887
    SchroederL_TablCol1      -> https://oeis.org/A239204
    SchroederL_NegHalf       -> https://oeis.org/A330802
    SchroederL_PosHalf       -> https://oeis.org/A331328
    SchroederL_Tinv          -> https://oeis.org/A331969

    SchroederL: Distinct: 15, Hits: 22, Misses: 47
'''
