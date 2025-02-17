from functools import cache
from _tabltypes import Table

"""Falling factorial, number of permutations of n things k at a time.

[0]  1
[1]  1,  1
[2]  1,  2,  2
[3]  1,  3,  6,   6
[4]  1,  4, 12,  24,   24
[5]  1,  5, 20,  60,  120,  120
[6]  1,  6, 30, 120,  360,  720,     720
[7]  1,  7, 42, 210,  840,  2520,   5040,   5040;
[8]  1,  8, 56, 336, 1680,  6720,  20160,  40320,   40320;
[9]  1,  9, 72, 504, 3024, 15120,  60480, 181440,  362880,  362880;
"""


@cache
def fallingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]

    r = fallingfactorial(n - 1)
    row = [n * r[k] for k in range(-1, n)]
    row[0] = 1
    return row


FallingFactorial = Table(
    fallingfactorial,
    "FallingFactorial",
    ["A008279", "A068424", "A094587", "A173333", "A181511"],
    "",
    r"n! / (n - k)!",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(FallingFactorial)




''' OEIS
    FallingFactorial_Trev11        -> 0 
    FallingFactorial_Tder          -> 0 
    FallingFactorial_PolyRow3      -> 0 
    FallingFactorial_RevTinv11     -> 0 
    FallingFactorial_RevTantidiag  -> 0 
    FallingFactorial_RevTder       -> 0 
    FallingFactorial_RevPolyRow3   -> 0 
    FallingFactorial_TablCol0      -> https://oeis.org/A12
    FallingFactorial_NegHalf       -> https://oeis.org/A23
    FallingFactorial_TablCol1      -> https://oeis.org/A27
    FallingFactorial_TablGcd       -> https://oeis.org/A27
    FallingFactorial_PolyRow1      -> https://oeis.org/A27
    FallingFactorial_RevPolyRow1   -> https://oeis.org/A27
    FallingFactorial_TablDiag0     -> https://oeis.org/A142
    FallingFactorial_TablDiag1     -> https://oeis.org/A142
    FallingFactorial_TablLcm       -> https://oeis.org/A142
    FallingFactorial_TablMax       -> https://oeis.org/A142
    FallingFactorial_AltSum        -> https://oeis.org/A166
    FallingFactorial_RevNegHalf    -> https://oeis.org/A354
    FallingFactorial_RevCentralO   -> https://oeis.org/A407
    FallingFactorial_TablSum       -> https://oeis.org/A522
    FallingFactorial_AbsSum        -> https://oeis.org/A522
    FallingFactorial_AccRevSum     -> https://oeis.org/A1339
    FallingFactorial_TransNat1     -> https://oeis.org/A1339
    FallingFactorial_TablDiag2     -> https://oeis.org/A1710
    FallingFactorial_TablDiag3     -> https://oeis.org/A1715
    FallingFactorial_CentralE      -> https://oeis.org/A1813
    FallingFactorial_PolyRow2      -> https://oeis.org/A1844
    FallingFactorial_TablCol2      -> https://oeis.org/A2378
    FallingFactorial_RevPolyRow2   -> https://oeis.org/A2522
    FallingFactorial_BinConv       -> https://oeis.org/A2720
    FallingFactorial_OddSum        -> https://oeis.org/A2747
    FallingFactorial_RevAntiDSum   -> https://oeis.org/A3470
    FallingFactorial_CentralO      -> https://oeis.org/A6963
    FallingFactorial_RevTransNat0  -> https://oeis.org/A7526
    FallingFactorial_TablCol3      -> https://oeis.org/A7531
    FallingFactorial_Triangle      -> https://oeis.org/A8279
    FallingFactorial_Talt          -> https://oeis.org/A8279
    FallingFactorial_RevEvenSum    -> https://oeis.org/A9179
    FallingFactorial_InvBinConv    -> https://oeis.org/A9940
    FallingFactorial_PosHalf       -> https://oeis.org/A10842
    FallingFactorial_PolyCol2      -> https://oeis.org/A10844
    FallingFactorial_RevPosHalf    -> https://oeis.org/A10844
    FallingFactorial_PolyCol3      -> https://oeis.org/A10845
    FallingFactorial_RevTransSqrs  -> https://oeis.org/A30297
    FallingFactorial_RevPolyCol3   -> https://oeis.org/A53486
    FallingFactorial_RevPolyDiag   -> https://oeis.org/A63170
    FallingFactorial_Toff11        -> https://oeis.org/A68424
    FallingFactorial_AntiDSum      -> https://oeis.org/A72374
    FallingFactorial_RevColMiddle  -> https://oeis.org/A81125
    FallingFactorial_EvenSum       -> https://oeis.org/A87208
    FallingFactorial_TransNat0     -> https://oeis.org/A93964
    FallingFactorial_Trev          -> https://oeis.org/A94587
    FallingFactorial_RevTalt       -> https://oeis.org/A94587
    FallingFactorial_AccSum        -> https://oeis.org/A111063
    FallingFactorial_RevAccRevSum  -> https://oeis.org/A111063
    FallingFactorial_RevTransNat1  -> https://oeis.org/A111063
    FallingFactorial_Tinvrev       -> https://oeis.org/A128229
    FallingFactorial_RevToff11     -> https://oeis.org/A173333
    FallingFactorial_RevTrev11     -> https://oeis.org/A181511
    FallingFactorial_RevOddSum     -> https://oeis.org/A186763
    FallingFactorial_ColMiddle     -> https://oeis.org/A205825
    FallingFactorial_PolyDiag      -> https://oeis.org/A277452
    FallingFactorial_TransSqrs     -> https://oeis.org/A343276
    FallingFactorial_Tantidiag     -> https://oeis.org/A344391
    FallingFactorial_Tacc          -> https://oeis.org/A347667
    FallingFactorial_RevTacc       -> https://oeis.org/A367962

    FallingFactorial: Distinct: 48, Hits: 60, Misses: 7
'''
