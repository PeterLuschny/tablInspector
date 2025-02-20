from functools import cache
from _tabltypes import Table

"""Binomial Diff Pell triangle


[0]    1;
[1]    1,    1;
[2]    3,    2,    1;
[3]    7,    9,    3,    1;
[4]   17,   28,   18,    4,    1;
[5]   41,   85,   70,   30,    5,    1;
[6]   99,  246,  255,  140,   45,    6,   1;
[7]  239,  693,  861,  595,  245,   63,   7,   1;
[8]  577, 1912, 2772, 2296, 1190,  392,  84,   8, 1;
[9] 1393, 5193, 8604, 8316, 5166, 2142, 588, 108, 9, 1;
"""


@cache
def binomialdiffpell(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]

    arow = binomialdiffpell(n - 1)
    row = arow + [1]
    for k in range(1, n):
        row[k] = (arow[k - 1] * n) // k
    row[0] = 2 * arow[0] + binomialdiffpell(n - 2)[0]

    return row


BinomialDiffPell = Table(
    binomialdiffpell,
    "BinomialDiffPell",
    ["A367564"],
    "A000000",
    r"\frac{1}{2} \binom{n}{k} ((1-\sqrt{2})^{n-k} + (1+\sqrt{2})^{n-k})"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(BinomialDiffPell)






''' OEIS
    BinomialDiffPell_Tinv          -> 0 
    BinomialDiffPell_Trev          -> 0 
    BinomialDiffPell_Trevinv       -> 0 
    BinomialDiffPell_Toff11        -> 0 
    BinomialDiffPell_Trev11        -> 0 
    BinomialDiffPell_Tinv11        -> 0 
    BinomialDiffPell_Trevinv11     -> 0 
    BinomialDiffPell_Tantidiag     -> 0 
    BinomialDiffPell_Tacc          -> 0 
    BinomialDiffPell_Tder          -> 0 
    BinomialDiffPell_TablCol1      -> 0 
    BinomialDiffPell_TablCol2      -> 0 
    BinomialDiffPell_TablCol3      -> 0 
    BinomialDiffPell_TablDiag3     -> 0 
    BinomialDiffPell_TablLcm       -> 0 
    BinomialDiffPell_TablMax       -> 0 
    BinomialDiffPell_AccSum        -> 0 
    BinomialDiffPell_AccRevSum     -> 0 
    BinomialDiffPell_AntiDSum      -> 0 
    BinomialDiffPell_ColMiddle     -> 0 
    BinomialDiffPell_CentralE      -> 0 
    BinomialDiffPell_CentralO      -> 0 
    BinomialDiffPell_TransNat0     -> 0 
    BinomialDiffPell_TransNat1     -> 0 
    BinomialDiffPell_TransSqrs     -> 0 
    BinomialDiffPell_BinConv       -> 0 
    BinomialDiffPell_InvBinConv    -> 0 
    BinomialDiffPell_PolyRow3      -> 0 
    BinomialDiffPell_PolyDiag      -> 0 
    BinomialDiffPell_RevToff11     -> 0 
    BinomialDiffPell_RevTrev11     -> 0 
    BinomialDiffPell_RevTantidiag  -> 0 
    BinomialDiffPell_RevTacc       -> 0 
    BinomialDiffPell_RevTalt       -> 0 
    BinomialDiffPell_RevTder       -> 0 
    BinomialDiffPell_RevAccRevSum  -> 0 
    BinomialDiffPell_RevAntiDSum   -> 0 
    BinomialDiffPell_RevColMiddle  -> 0 
    BinomialDiffPell_RevCentralO   -> 0 
    BinomialDiffPell_RevTransNat0  -> 0 
    BinomialDiffPell_RevTransNat1  -> 0 
    BinomialDiffPell_RevTransSqrs  -> 0 
    BinomialDiffPell_RevPolyRow3   -> 0 
    BinomialDiffPell_RevPolyCol3   -> 0 
    BinomialDiffPell_RevPolyDiag   -> 0 
    BinomialDiffPell_TablDiag0     -> https://oeis.org/A12
    BinomialDiffPell_TablGcd       -> https://oeis.org/A12
    BinomialDiffPell_TablDiag1     -> https://oeis.org/A27
    BinomialDiffPell_PolyRow1      -> https://oeis.org/A27
    BinomialDiffPell_RevPolyRow1   -> https://oeis.org/A27
    BinomialDiffPell_TablCol0      -> https://oeis.org/A1333
    BinomialDiffPell_RevNegHalf    -> https://oeis.org/A1333
    BinomialDiffPell_PosHalf       -> https://oeis.org/A1541
    BinomialDiffPell_TablSum       -> https://oeis.org/A6012
    BinomialDiffPell_AbsSum        -> https://oeis.org/A6012
    BinomialDiffPell_TablDiag2     -> https://oeis.org/A45943
    BinomialDiffPell_RevPolyRow2   -> https://oeis.org/A56109
    BinomialDiffPell_PolyRow2      -> https://oeis.org/A59100
    BinomialDiffPell_AltSum        -> https://oeis.org/A77957
    BinomialDiffPell_NegHalf       -> https://oeis.org/A83100
    BinomialDiffPell_PolyCol2      -> https://oeis.org/A83878
    BinomialDiffPell_RevPosHalf    -> https://oeis.org/A83878
    BinomialDiffPell_PolyCol3      -> https://oeis.org/A83879
    BinomialDiffPell_OddSum        -> https://oeis.org/A84154
    BinomialDiffPell_RevOddSum     -> https://oeis.org/A84154
    BinomialDiffPell_EvenSum       -> https://oeis.org/A88013
    BinomialDiffPell_RevEvenSum    -> https://oeis.org/A88013
    BinomialDiffPell_Triangle      -> https://oeis.org/A367564
    BinomialDiffPell_Talt          -> https://oeis.org/A367564

    BinomialDiffPell: Distinct: 16, Hits: 24, Misses: 45
'''
