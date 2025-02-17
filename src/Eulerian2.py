from functools import cache
from _tabltypes import Table

"""Eulerian2 triangle.

[0] 1;
[1] 0, 1;
[2] 0, 1,   2;
[3] 0, 1,   8,     6;
[4] 0, 1,  22,    58,     24;
[5] 0, 1,  52,   328,    444,    120;
[6] 0, 1, 114,  1452,   4400,   3708,    720;
[7] 0, 1, 240,  5610,  32120,  58140,  33984,  5040;
[8] 0, 1, 494, 19950, 195800, 644020, 785304, 341136, 40320;
"""


@cache
def eulerian2(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = eulerian2(n - 1) + [0]
    for k in range(n, 1, -1):
        row[k] = (2 * n - k) * row[k - 1] + k * row[k]
    return row


Eulerian2 = Table(
    eulerian2,
    "Eulerian2",
    ["A340556", "A201637", "A008517", "A112007", "A163936"],
    "A000000",
    r"%%",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Eulerian2)

# See also http://luschny.de/math/oeis/A340556.html




''' OEIS
    Eulerian2_Tinvrev11     -> 0 
    Eulerian2_Tantidiag     -> 0 
    Eulerian2_Tacc          -> 0 
    Eulerian2_Tder          -> 0 
    Eulerian2_TablLcm       -> 0 
    Eulerian2_TablGcd       -> 0 
    Eulerian2_EvenSum       -> 0 
    Eulerian2_OddSum        -> 0 
    Eulerian2_AccRevSum     -> 0 
    Eulerian2_AntiDSum      -> 0 
    Eulerian2_ColMiddle     -> 0 
    Eulerian2_CentralO      -> 0 
    Eulerian2_TransNat1     -> 0 
    Eulerian2_TransSqrs     -> 0 
    Eulerian2_BinConv       -> 0 
    Eulerian2_InvBinConv    -> 0 
    Eulerian2_PolyRow3      -> 0 
    Eulerian2_PolyCol3      -> 0 
    Eulerian2_PolyDiag      -> 0 
    Eulerian2_RevToff11     -> 0 
    Eulerian2_RevTrev11     -> 0 
    Eulerian2_RevTantidiag  -> 0 
    Eulerian2_RevTacc       -> 0 
    Eulerian2_RevTder       -> 0 
    Eulerian2_RevEvenSum    -> 0 
    Eulerian2_RevOddSum     -> 0 
    Eulerian2_RevAntiDSum   -> 0 
    Eulerian2_RevColMiddle  -> 0 
    Eulerian2_RevCentralO   -> 0 
    Eulerian2_RevNegHalf    -> 0 
    Eulerian2_RevTransSqrs  -> 0 
    Eulerian2_RevPolyRow3   -> 0 
    Eulerian2_RevPolyCol3   -> 0 
    Eulerian2_RevPolyDiag   -> 0 
    Eulerian2_TablCol0      -> https://oeis.org/A7
    Eulerian2_TablCol1      -> https://oeis.org/A12
    Eulerian2_RevPolyRow1   -> https://oeis.org/A12
    Eulerian2_PolyRow1      -> https://oeis.org/A27
    Eulerian2_RevPolyRow2   -> https://oeis.org/A27
    Eulerian2_TablDiag0     -> https://oeis.org/A142
    Eulerian2_PosHalf       -> https://oeis.org/A311
    Eulerian2_RevTransNat0  -> https://oeis.org/A457
    Eulerian2_TablSum       -> https://oeis.org/A1147
    Eulerian2_AbsSum        -> https://oeis.org/A1147
    Eulerian2_AltSum        -> https://oeis.org/A1662
    Eulerian2_TablDiag1     -> https://oeis.org/A2538
    Eulerian2_TablDiag2     -> https://oeis.org/A2539
    Eulerian2_TablCol3      -> https://oeis.org/A4301
    Eulerian2_TablCol2      -> https://oeis.org/A5803
    Eulerian2_TablMax       -> https://oeis.org/A7347
    Eulerian2_Toff11        -> https://oeis.org/A8517
    Eulerian2_PolyRow2      -> https://oeis.org/A14105
    Eulerian2_TransNat0     -> https://oeis.org/A51577
    Eulerian2_Trev11        -> https://oeis.org/A112007
    Eulerian2_TablDiag3     -> https://oeis.org/A112008
    Eulerian2_PolyCol2      -> https://oeis.org/A112487
    Eulerian2_RevPosHalf    -> https://oeis.org/A112487
    Eulerian2_Trev          -> https://oeis.org/A163936
    Eulerian2_RevTalt       -> https://oeis.org/A163936
    Eulerian2_Triangle      -> https://oeis.org/A201637
    Eulerian2_Talt          -> https://oeis.org/A201637
    Eulerian2_AccSum        -> https://oeis.org/A261898
    Eulerian2_RevAccRevSum  -> https://oeis.org/A261898
    Eulerian2_RevTransNat1  -> https://oeis.org/A261898
    Eulerian2_NegHalf       -> https://oeis.org/A341106
    Eulerian2_CentralE      -> https://oeis.org/A367369

    Eulerian2: Distinct: 25, Hits: 32, Misses: 34
'''
