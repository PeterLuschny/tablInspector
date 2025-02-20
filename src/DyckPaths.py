from functools import cache
from _tabltypes import Table

"""DyckPaths

[0]    1;
[1]    1,     1;
[2]    2,     3,     1;
[3]    5,     9,     5,    1;
[4]   14,    28,    20,    7,    1;
[5]   42,    90,    75,   35,    9,    1;
[6]  132,   297,   275,  154,   54,   11,   1;
[7]  429,  1001,  1001,  637,  273,   77,  13,   1;
[8] 1430,  3432,  3640, 2548, 1260,  440, 104,  15,  1;
[9] 4862, 11934, 13260, 9996, 5508, 2244, 663, 135, 17, 1;
"""


@cache
def dyckpaths(n: int) -> list[int]:
    if n == 0:
        return [1]

    pow = dyckpaths(n - 1) + [0]
    row = pow.copy()
    row[0] += row[1]
    row[n] = 1

    for k in range(n - 1, 0, -1):
        row[k] = pow[k - 1] + 2 * pow[k] + pow[k + 1]

    return row


DyckPaths = Table(
    dyckpaths,
    "DyckPaths",
    ["A039599", "A050155"],
    "A000000",
    r"\binom{2n}{n - k} (2k + 1) / (n + k + 1)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(DyckPaths)






''' OEIS
    DyckPaths_Trev11        -> 0 
    DyckPaths_Tantidiag     -> 0 
    DyckPaths_Tder          -> 0 
    DyckPaths_TablDiag3     -> 0 
    DyckPaths_TablLcm       -> 0 
    DyckPaths_TablMax       -> 0 
    DyckPaths_ColMiddle     -> 0 
    DyckPaths_CentralO      -> 0 
    DyckPaths_InvBinConv    -> 0 
    DyckPaths_PolyDiag      -> 0 
    DyckPaths_RevToff11     -> 0 
    DyckPaths_RevTrev11     -> 0 
    DyckPaths_RevTantidiag  -> 0 
    DyckPaths_RevTder       -> 0 
    DyckPaths_RevColMiddle  -> 0 
    DyckPaths_RevCentralO   -> 0 
    DyckPaths_RevTransSqrs  -> 0 
    DyckPaths_RevPolyDiag   -> 0 
    DyckPaths_AltSum        -> https://oeis.org/A7
    DyckPaths_TablDiag0     -> https://oeis.org/A12
    DyckPaths_TablGcd       -> https://oeis.org/A12
    DyckPaths_PolyRow1      -> https://oeis.org/A27
    DyckPaths_RevPolyRow1   -> https://oeis.org/A27
    DyckPaths_TablCol0      -> https://oeis.org/A108
    DyckPaths_TablCol1      -> https://oeis.org/A245
    DyckPaths_TablCol2      -> https://oeis.org/A344
    DyckPaths_TransNat0     -> https://oeis.org/A346
    DyckPaths_RevPolyRow2   -> https://oeis.org/A384
    DyckPaths_TransSqrs     -> https://oeis.org/A531
    DyckPaths_RevTransNat0  -> https://oeis.org/A531
    DyckPaths_TablCol3      -> https://oeis.org/A588
    DyckPaths_RevNegHalf    -> https://oeis.org/A957
    DyckPaths_AntiDSum      -> https://oeis.org/A958
    DyckPaths_TablSum       -> https://oeis.org/A984
    DyckPaths_AbsSum        -> https://oeis.org/A984
    DyckPaths_EvenSum       -> https://oeis.org/A1700
    DyckPaths_OddSum        -> https://oeis.org/A1700
    DyckPaths_RevEvenSum    -> https://oeis.org/A1700
    DyckPaths_RevOddSum     -> https://oeis.org/A1700
    DyckPaths_PolyRow2      -> https://oeis.org/A2378
    DyckPaths_TablDiag1     -> https://oeis.org/A5408
    DyckPaths_PolyCol2      -> https://oeis.org/A7854
    DyckPaths_RevPosHalf    -> https://oeis.org/A7854
    DyckPaths_TablDiag2     -> https://oeis.org/A14107
    DyckPaths_RevPolyRow3   -> https://oeis.org/A27849
    DyckPaths_AccRevSum     -> https://oeis.org/A32443
    DyckPaths_TransNat1     -> https://oeis.org/A32443
    DyckPaths_RevPolyCol3   -> https://oeis.org/A35610
    DyckPaths_Triangle      -> https://oeis.org/A39599
    DyckPaths_Talt          -> https://oeis.org/A39599
    DyckPaths_Toff11        -> https://oeis.org/A50155
    DyckPaths_Tacc          -> https://oeis.org/A50157
    DyckPaths_Trev          -> https://oeis.org/A50165
    DyckPaths_RevTalt       -> https://oeis.org/A50165
    DyckPaths_Trevinv       -> https://oeis.org/A54142
    DyckPaths_PolyRow3      -> https://oeis.org/A62158
    DyckPaths_RevTacc       -> https://oeis.org/A62344
    DyckPaths_NegHalf       -> https://oeis.org/A64062
    DyckPaths_PolyCol3      -> https://oeis.org/A76035
    DyckPaths_Tinv          -> https://oeis.org/A85478
    DyckPaths_PosHalf       -> https://oeis.org/A89022
    DyckPaths_CentralE      -> https://oeis.org/A126596
    DyckPaths_BinConv       -> https://oeis.org/A174687
    DyckPaths_Trevinv11     -> https://oeis.org/A210551
    DyckPaths_Tinv11        -> https://oeis.org/A258993
    DyckPaths_RevAntiDSum   -> https://oeis.org/A274115
    DyckPaths_AccSum        -> https://oeis.org/A296771
    DyckPaths_RevAccRevSum  -> https://oeis.org/A296771
    DyckPaths_RevTransNat1  -> https://oeis.org/A296771

    DyckPaths: Distinct: 39, Hits: 51, Misses: 18
'''
