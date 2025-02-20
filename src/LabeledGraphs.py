from functools import cache
from Binomial import Binomial
from _tabltypes import Table

"""Labeled graphs.

[0] 1;
[1] 0,       1;
[2] 0,       1,      1;
[3] 0,       2,      2,     4;
[4] 0,       8,      6,    12,    38;
[5] 0,      64,     32,    48,   152,    728;
[6] 0,    1024,    320,   320,   760,   3640,   26704;
[7] 0,   32768,   6144,  3840,  6080,  21840,  160224,  1866256;
"""


@cache
def labeledgraphs(n: int) -> list[int]:
    if n == 0:
        return [1]

    s = [
        2 ** (((k - n + 1) * (k - n)) // 2)
        * Binomial(n - 1, k - 1)
        * labeledgraphs(k)[k]
        for k in range(1, n)
    ]
    b = 2 ** (((n - 1) * n) // 2) - sum(s)

    return [0] + s + [b]


LabeledGraphs = Table(
    labeledgraphs,
    "LabeledGraphs",
    ["A360603"],
    "",
    r"2^{\binom{n-k}{2}} \binom{n-1}{k-1} \text{A001187}(k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(LabeledGraphs)






''' OEIS
    LabeledGraphs_Trev          -> 0 
    LabeledGraphs_Toff11        -> 0 
    LabeledGraphs_Trev11        -> 0 
    LabeledGraphs_Tantidiag     -> 0 
    LabeledGraphs_Tder          -> 0 
    LabeledGraphs_TablCol3      -> 0 
    LabeledGraphs_TablDiag3     -> 0 
    LabeledGraphs_TablLcm       -> 0 
    LabeledGraphs_EvenSum       -> 0 
    LabeledGraphs_OddSum        -> 0 
    LabeledGraphs_AltSum        -> 0 
    LabeledGraphs_AccSum        -> 0 
    LabeledGraphs_AccRevSum     -> 0 
    LabeledGraphs_AntiDSum      -> 0 
    LabeledGraphs_ColMiddle     -> 0 
    LabeledGraphs_CentralE      -> 0 
    LabeledGraphs_CentralO      -> 0 
    LabeledGraphs_PosHalf       -> 0 
    LabeledGraphs_NegHalf       -> 0 
    LabeledGraphs_TransNat0     -> 0 
    LabeledGraphs_TransNat1     -> 0 
    LabeledGraphs_TransSqrs     -> 0 
    LabeledGraphs_BinConv       -> 0 
    LabeledGraphs_InvBinConv    -> 0 
    LabeledGraphs_PolyRow3      -> 0 
    LabeledGraphs_PolyCol2      -> 0 
    LabeledGraphs_PolyCol3      -> 0 
    LabeledGraphs_PolyDiag      -> 0 
    LabeledGraphs_RevToff11     -> 0 
    LabeledGraphs_RevTrev11     -> 0 
    LabeledGraphs_RevTantidiag  -> 0 
    LabeledGraphs_RevTacc       -> 0 
    LabeledGraphs_RevTalt       -> 0 
    LabeledGraphs_RevTder       -> 0 
    LabeledGraphs_RevEvenSum    -> 0 
    LabeledGraphs_RevOddSum     -> 0 
    LabeledGraphs_RevAccRevSum  -> 0 
    LabeledGraphs_RevAntiDSum   -> 0 
    LabeledGraphs_RevColMiddle  -> 0 
    LabeledGraphs_RevCentralO   -> 0 
    LabeledGraphs_RevPosHalf    -> 0 
    LabeledGraphs_RevNegHalf    -> 0 
    LabeledGraphs_RevTransNat0  -> 0 
    LabeledGraphs_RevTransNat1  -> 0 
    LabeledGraphs_RevTransSqrs  -> 0 
    LabeledGraphs_RevPolyCol3   -> 0 
    LabeledGraphs_RevPolyDiag   -> 0 
    LabeledGraphs_TablCol0      -> https://oeis.org/A7
    LabeledGraphs_RevPolyRow1   -> https://oeis.org/A12
    LabeledGraphs_PolyRow1      -> https://oeis.org/A27
    LabeledGraphs_RevPolyRow2   -> https://oeis.org/A27
    LabeledGraphs_TablDiag0     -> https://oeis.org/A1187
    LabeledGraphs_TablMax       -> https://oeis.org/A1187
    LabeledGraphs_PolyRow2      -> https://oeis.org/A2378
    LabeledGraphs_TablCol1      -> https://oeis.org/A6125
    LabeledGraphs_TablSum       -> https://oeis.org/A6125
    LabeledGraphs_AbsSum        -> https://oeis.org/A6125
    LabeledGraphs_TablDiag1     -> https://oeis.org/A53549
    LabeledGraphs_TablGcd       -> https://oeis.org/A60818
    LabeledGraphs_TablCol2      -> https://oeis.org/A123903
    LabeledGraphs_RevPolyRow3   -> https://oeis.org/A137882
    LabeledGraphs_TablDiag2     -> https://oeis.org/A275462
    LabeledGraphs_Triangle      -> https://oeis.org/A360603
    LabeledGraphs_Talt          -> https://oeis.org/A360603
    LabeledGraphs_Tacc          -> https://oeis.org/A360860

    LabeledGraphs: Distinct: 14, Hits: 18, Misses: 47
'''
