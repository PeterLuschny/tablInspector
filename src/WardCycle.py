from functools import cache
from _tabltypes import Table

"""Ward cycle numbers.


[1]
[0,    1]
[0,    2,     3]
[0,    6,    20,     15]
[0,   24,   130,    210,    105]
[0,  120,   924,   2380,   2520,    945]
[0,  720,  7308,  26432,  44100,  34650,  10395]
[0, 5040, 64224, 303660, 705320, 866250, 540540, 135135]
"""


@cache
def wardcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = wardcycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k - 1] + row[k])

    return row


WardCycle = Table(
    wardcycle,
    "WardCycle",
    ["A269940", "A111999", "A259456"],
    "",
    r"\sum_{m=0}^{k} (-1)^{m+k} \binom{n+k}{n+m} { n + m \brack m}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(WardCycle)






''' OEIS
    WardCycle_Trev          -> 0 
    WardCycle_Tacc          -> 0 
    WardCycle_Tder          -> 0 
    WardCycle_TablLcm       -> 0 
    WardCycle_TablMax       -> 0 
    WardCycle_EvenSum       -> 0 
    WardCycle_OddSum        -> 0 
    WardCycle_AccSum        -> 0 
    WardCycle_AccRevSum     -> 0 
    WardCycle_ColMiddle     -> 0 
    WardCycle_CentralE      -> 0 
    WardCycle_CentralO      -> 0 
    WardCycle_PosHalf       -> 0 
    WardCycle_TransNat0     -> 0 
    WardCycle_TransNat1     -> 0 
    WardCycle_TransSqrs     -> 0 
    WardCycle_BinConv       -> 0 
    WardCycle_InvBinConv    -> 0 
    WardCycle_PolyRow3      -> 0 
    WardCycle_PolyCol2      -> 0 
    WardCycle_PolyCol3      -> 0 
    WardCycle_PolyDiag      -> 0 
    WardCycle_RevToff11     -> 0 
    WardCycle_RevTrev11     -> 0 
    WardCycle_RevTantidiag  -> 0 
    WardCycle_RevTacc       -> 0 
    WardCycle_RevTalt       -> 0 
    WardCycle_RevTder       -> 0 
    WardCycle_RevEvenSum    -> 0 
    WardCycle_RevOddSum     -> 0 
    WardCycle_RevAccRevSum  -> 0 
    WardCycle_RevAntiDSum   -> 0 
    WardCycle_RevColMiddle  -> 0 
    WardCycle_RevCentralO   -> 0 
    WardCycle_RevPosHalf    -> 0 
    WardCycle_RevTransNat0  -> 0 
    WardCycle_RevTransNat1  -> 0 
    WardCycle_RevTransSqrs  -> 0 
    WardCycle_RevPolyCol3   -> 0 
    WardCycle_RevPolyDiag   -> 0 
    WardCycle_TablCol0      -> https://oeis.org/A7
    WardCycle_TablGcd       -> https://oeis.org/A12
    WardCycle_RevPolyRow1   -> https://oeis.org/A12
    WardCycle_PolyRow1      -> https://oeis.org/A27
    WardCycle_TablCol1      -> https://oeis.org/A142
    WardCycle_AntiDSum      -> https://oeis.org/A166
    WardCycle_TablCol2      -> https://oeis.org/A276
    WardCycle_TablCol3      -> https://oeis.org/A483
    WardCycle_TablDiag1     -> https://oeis.org/A906
    WardCycle_TablDiag2     -> https://oeis.org/A907
    WardCycle_TablDiag0     -> https://oeis.org/A1147
    WardCycle_NegHalf       -> https://oeis.org/A1662
    WardCycle_TablDiag3     -> https://oeis.org/A1784
    WardCycle_RevPolyRow2   -> https://oeis.org/A5408
    WardCycle_RevNegHalf    -> https://oeis.org/A6351
    WardCycle_TablSum       -> https://oeis.org/A32188
    WardCycle_AbsSum        -> https://oeis.org/A32188
    WardCycle_AltSum        -> https://oeis.org/A33999
    WardCycle_PolyRow2      -> https://oeis.org/A45944
    WardCycle_Tantidiag     -> https://oeis.org/A106828
    WardCycle_Trev11        -> https://oeis.org/A111999
    WardCycle_RevPolyRow3   -> https://oeis.org/A239325
    WardCycle_Toff11        -> https://oeis.org/A259456
    WardCycle_Triangle      -> https://oeis.org/A269940
    WardCycle_Talt          -> https://oeis.org/A269940

    WardCycle: Distinct: 23, Hits: 25, Misses: 40
'''
