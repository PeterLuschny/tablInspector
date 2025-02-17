from functools import cache
from _tabltypes import Table

"""Nicomachus triangle.

[0] [  1]
[1] [  2,   3]
[2] [  4,   6,   9]
[3] [  8,  12,  18,  27]
[4] [ 16,  24,  36,  54,  81]
[5] [ 32,  48,  72, 108, 162, 243]
[6] [ 64,  96, 144, 216, 324, 486,  729]
[7] [128, 192, 288, 432, 648, 972, 1458, 2187]
"""


@cache
def nicomachus(n: int) -> list[int]:
    if n == 0:
        return [1]

    prev_row = nicomachus(n - 1)
    row = prev_row + [3 * prev_row[-1]]
    for k in range(0, n):
        row[k] *= 2
    return row


Nicomachus = Table(
    nicomachus, 
    "Nicomachus", 
    ["A036561", "A081954", "A175840"], 
    "", 
    r"2^{n - k}\, 3^{k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Nicomachus)




''' OEIS
    Nicomachus_Toff11        -> 0 
    Nicomachus_Trev11        -> 0 
    Nicomachus_Tantidiag     -> 0 
    Nicomachus_Tder          -> 0 
    Nicomachus_EvenSum       -> 0 
    Nicomachus_OddSum        -> 0 
    Nicomachus_AccRevSum     -> 0 
    Nicomachus_TransNat0     -> 0 
    Nicomachus_TransNat1     -> 0 
    Nicomachus_TransSqrs     -> 0 
    Nicomachus_PolyRow2      -> 0 
    Nicomachus_PolyRow3      -> 0 
    Nicomachus_PolyDiag      -> 0 
    Nicomachus_RevToff11     -> 0 
    Nicomachus_RevTantidiag  -> 0 
    Nicomachus_RevTacc       -> 0 
    Nicomachus_RevTder       -> 0 
    Nicomachus_RevOddSum     -> 0 
    Nicomachus_RevTransNat0  -> 0 
    Nicomachus_RevTransSqrs  -> 0 
    Nicomachus_RevPolyRow2   -> 0 
    Nicomachus_RevPolyRow3   -> 0 
    Nicomachus_RevPolyDiag   -> 0 
    Nicomachus_TablGcd       -> https://oeis.org/A12
    Nicomachus_InvBinConv    -> https://oeis.org/A12
    Nicomachus_TablCol0      -> https://oeis.org/A79
    Nicomachus_TablDiag0     -> https://oeis.org/A244
    Nicomachus_TablMax       -> https://oeis.org/A244
    Nicomachus_BinConv       -> https://oeis.org/A351
    Nicomachus_TablLcm       -> https://oeis.org/A400
    Nicomachus_CentralE      -> https://oeis.org/A400
    Nicomachus_TablSum       -> https://oeis.org/A1047
    Nicomachus_AbsSum        -> https://oeis.org/A1047
    Nicomachus_TablDiag2     -> https://oeis.org/A3946
    Nicomachus_TablCol2      -> https://oeis.org/A5010
    Nicomachus_TablDiag3     -> https://oeis.org/A5051
    Nicomachus_PosHalf       -> https://oeis.org/A5061
    Nicomachus_RevPolyRow1   -> https://oeis.org/A5408
    Nicomachus_TablCol1      -> https://oeis.org/A7283
    Nicomachus_TablDiag1     -> https://oeis.org/A8776
    Nicomachus_AltSum        -> https://oeis.org/A15441
    Nicomachus_PolyCol2      -> https://oeis.org/A16129
    Nicomachus_RevPosHalf    -> https://oeis.org/A16129
    Nicomachus_PolyCol3      -> https://oeis.org/A16133
    Nicomachus_RevPolyCol3   -> https://oeis.org/A16137
    Nicomachus_PolyRow1      -> https://oeis.org/A16789
    Nicomachus_RevColMiddle  -> https://oeis.org/A26532
    Nicomachus_ColMiddle     -> https://oeis.org/A26549
    Nicomachus_Triangle      -> https://oeis.org/A36561
    Nicomachus_Talt          -> https://oeis.org/A36561
    Nicomachus_NegHalf       -> https://oeis.org/A53404
    Nicomachus_RevNegHalf    -> https://oeis.org/A53524
    Nicomachus_AccSum        -> https://oeis.org/A66810
    Nicomachus_RevAccRevSum  -> https://oeis.org/A66810
    Nicomachus_RevTransNat1  -> https://oeis.org/A66810
    Nicomachus_RevCentralO   -> https://oeis.org/A81341
    Nicomachus_RevTrev11     -> https://oeis.org/A81954
    Nicomachus_RevAntiDSum   -> https://oeis.org/A135247
    Nicomachus_CentralO      -> https://oeis.org/A167747
    Nicomachus_AntiDSum      -> https://oeis.org/A167762
    Nicomachus_RevEvenSum    -> https://oeis.org/A167910
    Nicomachus_TablCol3      -> https://oeis.org/A175806
    Nicomachus_Trev          -> https://oeis.org/A175840
    Nicomachus_RevTalt       -> https://oeis.org/A175840
    Nicomachus_Tacc          -> https://oeis.org/A230435

    Nicomachus: Distinct: 34, Hits: 42, Misses: 23
'''
