from functools import cache
from _tabltypes import Table

"""Binomial Pell triangle


[0]   1
[1]   2     2
[2]   5     6    3
[3]  12    20    12     4
[4]  29    60    50    20     5
[5]  70   174   180   100    30     6
[6] 169   490   609   420   175    42   7
[7] 408  1352  1960  1624   840   280   56   8
[8] 985  3672  6084  5880  3654  1512  420  72  9
"""


@cache
def binomialpell(n: int) -> list[int]:

    if n == 0:
        return [1]
    if n == 1:
        return [2, 2]

    arow = binomialpell(n - 1)
    row = arow + [n + 1]
    for k in range(1, n):
        row[k] = (arow[k - 1] * (n + 1)) // k
    row[0] = 2 * arow[0] + binomialpell(n - 2)[0]

    return row


BinomialPell = Table(
    binomialpell,
    "BinomialPell",
    ["A367211"],
    "", # not invertible
    r"\binom{n+1}{k}\, \text{Pell}(n+1-k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(BinomialPell)




''' OEIS
    BinomialPell_Trev          -> 0 
    BinomialPell_Toff11        -> 0 
    BinomialPell_Trev11        -> 0 
    BinomialPell_Tantidiag     -> 0 
    BinomialPell_Tacc          -> 0 
    BinomialPell_Tder          -> 0 
    BinomialPell_TablCol2      -> 0 
    BinomialPell_TablCol3      -> 0 
    BinomialPell_TablLcm       -> 0 
    BinomialPell_TablMax       -> 0 
    BinomialPell_OddSum        -> 0 
    BinomialPell_AccSum        -> 0 
    BinomialPell_AccRevSum     -> 0 
    BinomialPell_ColMiddle     -> 0 
    BinomialPell_CentralE      -> 0 
    BinomialPell_CentralO      -> 0 
    BinomialPell_TransNat0     -> 0 
    BinomialPell_TransNat1     -> 0 
    BinomialPell_TransSqrs     -> 0 
    BinomialPell_BinConv       -> 0 
    BinomialPell_InvBinConv    -> 0 
    BinomialPell_PolyDiag      -> 0 
    BinomialPell_RevToff11     -> 0 
    BinomialPell_RevTrev11     -> 0 
    BinomialPell_RevTantidiag  -> 0 
    BinomialPell_RevTacc       -> 0 
    BinomialPell_RevTalt       -> 0 
    BinomialPell_RevTder       -> 0 
    BinomialPell_RevOddSum     -> 0 
    BinomialPell_RevAccRevSum  -> 0 
    BinomialPell_RevAntiDSum   -> 0 
    BinomialPell_RevColMiddle  -> 0 
    BinomialPell_RevCentralO   -> 0 
    BinomialPell_RevTransNat0  -> 0 
    BinomialPell_RevTransNat1  -> 0 
    BinomialPell_RevTransSqrs  -> 0 
    BinomialPell_RevPolyRow2   -> 0 
    BinomialPell_RevPolyRow3   -> 0 
    BinomialPell_RevPolyDiag   -> 0 
    BinomialPell_TablDiag0     -> https://oeis.org/A27
    BinomialPell_TablCol0      -> https://oeis.org/A129
    BinomialPell_RevNegHalf    -> https://oeis.org/A129
    BinomialPell_PosHalf       -> https://oeis.org/A1109
    BinomialPell_TablDiag1     -> https://oeis.org/A2378
    BinomialPell_PolyRow1      -> https://oeis.org/A5843
    BinomialPell_RevPolyRow1   -> https://oeis.org/A5843
    BinomialPell_PolyRow2      -> https://oeis.org/A5918
    BinomialPell_TablGcd       -> https://oeis.org/A6519
    BinomialPell_TablSum       -> https://oeis.org/A7070
    BinomialPell_AbsSum        -> https://oeis.org/A7070
    BinomialPell_NegHalf       -> https://oeis.org/A15519
    BinomialPell_TablDiag3     -> https://oeis.org/A33486
    BinomialPell_AltSum        -> https://oeis.org/A77957
    BinomialPell_PolyCol2      -> https://oeis.org/A81179
    BinomialPell_RevPosHalf    -> https://oeis.org/A81179
    BinomialPell_PolyCol3      -> https://oeis.org/A81180
    BinomialPell_EvenSum       -> https://oeis.org/A94038
    BinomialPell_RevEvenSum    -> https://oeis.org/A94038
    BinomialPell_AntiDSum      -> https://oeis.org/A99626
    BinomialPell_TablDiag2     -> https://oeis.org/A134481
    BinomialPell_RevPolyCol3   -> https://oeis.org/A190331
    BinomialPell_PolyRow3      -> https://oeis.org/A292022
    BinomialPell_TablCol1      -> https://oeis.org/A361732
    BinomialPell_Triangle      -> https://oeis.org/A367211
    BinomialPell_Talt          -> https://oeis.org/A367211

    BinomialPell: Distinct: 21, Hits: 26, Misses: 39
'''
