from functools import cache
from _tabltypes import Table


"""Levin's Triangle, RisingFactorial(n + 1, n) / (k! * (n - k)!).

[0]     1;
[1]     2,      2;
[2]     6,     12,      6;
[3]    20,     60,     60,     20;
[4]    70,    280,    420,    280,     70;
[5]   252,   1260,   2520,   2520,   1260,    252;
[6]   924,   5544,  13860,  18480,  13860,   5544,    924;
[7]  3432,  24024,  72072, 120120, 120120,  72072,  24024,   3432;
[8] 12870, 102960, 360360, 720720, 900900, 720720, 360360, 102960, 12870;
"""


@cache
def levin(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = levin(n - 1) + [1]
    row[0] = row[n] = (row[n - 1] * (4 * n - 2)) // n
    for k in range(1, n):
        row[k] = ((n - k + 1) * row[k - 1]) // k
    return row


Levin = Table(
    levin, 
    "Levin", 
    ["A356546"], 
    "", 
    r"\binom{2n}{n} \ \binom{n}{k}"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Levin)




''' OEIS
    Levin_Toff11        -> 0 
    Levin_Trev11        -> 0 
    Levin_Tacc          -> 0 
    Levin_Tder          -> 0 
    Levin_TablCol3      -> 0 
    Levin_TablDiag3     -> 0 
    Levin_TablLcm       -> 0 
    Levin_TablMax       -> 0 
    Levin_AccSum        -> 0 
    Levin_AccRevSum     -> 0 
    Levin_ColMiddle     -> 0 
    Levin_CentralO      -> 0 
    Levin_TransNat0     -> 0 
    Levin_TransNat1     -> 0 
    Levin_TransSqrs     -> 0 
    Levin_PolyRow3      -> 0 
    Levin_PolyDiag      -> 0 
    Levin_RevToff11     -> 0 
    Levin_RevTrev11     -> 0 
    Levin_RevTacc       -> 0 
    Levin_RevTder       -> 0 
    Levin_RevAccRevSum  -> 0 
    Levin_RevColMiddle  -> 0 
    Levin_RevCentralO   -> 0 
    Levin_RevTransNat0  -> 0 
    Levin_RevTransNat1  -> 0 
    Levin_RevTransSqrs  -> 0 
    Levin_RevPolyRow3   -> 0 
    Levin_RevPolyDiag   -> 0 
    Levin_AltSum        -> https://oeis.org/A7
    Levin_CentralE      -> https://oeis.org/A897
    Levin_InvBinConv    -> https://oeis.org/A897
    Levin_TablCol2      -> https://oeis.org/A911
    Levin_TablDiag2     -> https://oeis.org/A911
    Levin_TablCol0      -> https://oeis.org/A984
    Levin_TablDiag0     -> https://oeis.org/A984
    Levin_TablGcd       -> https://oeis.org/A984
    Levin_NegHalf       -> https://oeis.org/A984
    Levin_RevNegHalf    -> https://oeis.org/A984
    Levin_BinConv       -> https://oeis.org/A2894
    Levin_TablCol1      -> https://oeis.org/A5430
    Levin_TablDiag1     -> https://oeis.org/A5430
    Levin_PolyRow1      -> https://oeis.org/A5843
    Levin_RevPolyRow1   -> https://oeis.org/A5843
    Levin_AntiDSum      -> https://oeis.org/A6139
    Levin_RevAntiDSum   -> https://oeis.org/A6139
    Levin_Tantidiag     -> https://oeis.org/A8556
    Levin_RevTantidiag  -> https://oeis.org/A8556
    Levin_PolyRow2      -> https://oeis.org/A33581
    Levin_RevPolyRow2   -> https://oeis.org/A33581
    Levin_TablSum       -> https://oeis.org/A59304
    Levin_AbsSum        -> https://oeis.org/A59304
    Levin_EvenSum       -> https://oeis.org/A69723
    Levin_OddSum        -> https://oeis.org/A69723
    Levin_RevEvenSum    -> https://oeis.org/A69723
    Levin_RevOddSum     -> https://oeis.org/A69723
    Levin_PolyCol3      -> https://oeis.org/A98430
    Levin_RevPolyCol3   -> https://oeis.org/A98430
    Levin_PosHalf       -> https://oeis.org/A98658
    Levin_PolyCol2      -> https://oeis.org/A98658
    Levin_RevPosHalf    -> https://oeis.org/A98658
    Levin_Triangle      -> https://oeis.org/A356546
    Levin_Trev          -> https://oeis.org/A356546
    Levin_Talt          -> https://oeis.org/A356546
    Levin_RevTalt       -> https://oeis.org/A356546

    Levin: Distinct: 16, Hits: 36, Misses: 29
'''
