from functools import cache
from _tabltypes import Table

"""Expansion of x^n in terms of Laguerre (unsigned).

[0] [   1]
[1] [   1,     1]
[2] [   2,     4,      2]
[3] [   6,    18,     18,      6]
[4] [  24,    96,    144,     96,     24]
[5] [ 120,   600,   1200,   1200,    600,    120]
[6] [ 720,  4320,  10800,  14400,  10800,   4320,   720]
[7] [5040, 35280, 105840, 176400, 176400, 105840, 35280, 5040]
"""

@cache
def powlaguerre(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = powlaguerre(n - 1) + [1]
    row[0] = row[n] = row[0] * n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


PowLaguerre = Table(
    powlaguerre, 
    "PowLaguerre", 
    ["A196347", "A021012"], 
    "", 
    r"n! \binom{n}{k}"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(PowLaguerre)






''' OEIS
    PowLaguerre_Toff11        -> 0 
    PowLaguerre_Trev11        -> 0 
    PowLaguerre_Tantidiag     -> 0 
    PowLaguerre_Tacc          -> 0 
    PowLaguerre_Tder          -> 0 
    PowLaguerre_TransSqrs     -> 0 
    PowLaguerre_RevToff11     -> 0 
    PowLaguerre_RevTrev11     -> 0 
    PowLaguerre_RevTantidiag  -> 0 
    PowLaguerre_RevTacc       -> 0 
    PowLaguerre_RevTder       -> 0 
    PowLaguerre_RevTransSqrs  -> 0 
    PowLaguerre_AltSum        -> https://oeis.org/A7
    PowLaguerre_PolyRow1      -> https://oeis.org/A27
    PowLaguerre_RevPolyRow1   -> https://oeis.org/A27
    PowLaguerre_TablCol0      -> https://oeis.org/A142
    PowLaguerre_TablDiag0     -> https://oeis.org/A142
    PowLaguerre_TablGcd       -> https://oeis.org/A142
    PowLaguerre_NegHalf       -> https://oeis.org/A142
    PowLaguerre_RevNegHalf    -> https://oeis.org/A142
    PowLaguerre_TablSum       -> https://oeis.org/A165
    PowLaguerre_AbsSum        -> https://oeis.org/A165
    PowLaguerre_PolyRow2      -> https://oeis.org/A1105
    PowLaguerre_RevPolyRow2   -> https://oeis.org/A1105
    PowLaguerre_TablCol1      -> https://oeis.org/A1563
    PowLaguerre_TablDiag1     -> https://oeis.org/A1563
    PowLaguerre_TablCol2      -> https://oeis.org/A1804
    PowLaguerre_TablDiag2     -> https://oeis.org/A1804
    PowLaguerre_TablCol3      -> https://oeis.org/A1805
    PowLaguerre_TablDiag3     -> https://oeis.org/A1805
    PowLaguerre_BinConv       -> https://oeis.org/A1813
    PowLaguerre_EvenSum       -> https://oeis.org/A2866
    PowLaguerre_OddSum        -> https://oeis.org/A2866
    PowLaguerre_RevEvenSum    -> https://oeis.org/A2866
    PowLaguerre_RevOddSum     -> https://oeis.org/A2866
    PowLaguerre_TransNat0     -> https://oeis.org/A14479
    PowLaguerre_RevTransNat0  -> https://oeis.org/A14479
    PowLaguerre_PosHalf       -> https://oeis.org/A32031
    PowLaguerre_PolyCol2      -> https://oeis.org/A32031
    PowLaguerre_RevPosHalf    -> https://oeis.org/A32031
    PowLaguerre_PolyCol3      -> https://oeis.org/A47053
    PowLaguerre_RevPolyCol3   -> https://oeis.org/A47053
    PowLaguerre_TablMax       -> https://oeis.org/A59837
    PowLaguerre_ColMiddle     -> https://oeis.org/A59837
    PowLaguerre_RevColMiddle  -> https://oeis.org/A59837
    PowLaguerre_CentralE      -> https://oeis.org/A122747
    PowLaguerre_InvBinConv    -> https://oeis.org/A122747
    PowLaguerre_PolyDiag      -> https://oeis.org/A152684
    PowLaguerre_RevPolyDiag   -> https://oeis.org/A152684
    PowLaguerre_AccSum        -> https://oeis.org/A187735
    PowLaguerre_AccRevSum     -> https://oeis.org/A187735
    PowLaguerre_TransNat1     -> https://oeis.org/A187735
    PowLaguerre_RevAccRevSum  -> https://oeis.org/A187735
    PowLaguerre_RevTransNat1  -> https://oeis.org/A187735
    PowLaguerre_Triangle      -> https://oeis.org/A196347
    PowLaguerre_Trev          -> https://oeis.org/A196347
    PowLaguerre_Talt          -> https://oeis.org/A196347
    PowLaguerre_RevTalt       -> https://oeis.org/A196347
    PowLaguerre_AntiDSum      -> https://oeis.org/A240172
    PowLaguerre_RevAntiDSum   -> https://oeis.org/A240172
    PowLaguerre_PolyRow3      -> https://oeis.org/A244726
    PowLaguerre_RevPolyRow3   -> https://oeis.org/A244726
    PowLaguerre_TablLcm       -> https://oeis.org/A360283
    PowLaguerre_CentralO      -> https://oeis.org/A360602
    PowLaguerre_RevCentralO   -> https://oeis.org/A360602

    PowLaguerre: Distinct: 23, Hits: 53, Misses: 12
'''
