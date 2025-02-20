from functools import cache
from _tabltypes import Table

"""Central cycle factorial numbers.

[0] [1]
[1] [0,    1]
[2] [0,    2,     3]
[3] [0,    6,    20,     15]
[4] [0,   24,   130,    210,    105]
[5] [0,  120,   924,   2380,   2520,    945]
[6] [0,  720,  7308,  26432,  44100,  34650,  10395]
[7] [0, 5040, 64224, 303660, 705320, 866250, 540540, 135135]
"""


@cache
def centralcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = centralcycle(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] = (n + k - 1) * (row[k] + row[k - 1])

    return row


CentralCycle = Table(
    centralcycle, 
    "CentralCycle", 
    ["A269940", "A111999", "A259456"], 
    "",  # not ivertible
    r"\sum_{m=0}^k (-1)^{m+k} \binom{n+k}{n+m}\, {n + m \brack m}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CentralCycle)






''' OEIS
    CentralCycle_Trev          -> 0 
    CentralCycle_Tacc          -> 0 
    CentralCycle_Tder          -> 0 
    CentralCycle_TablLcm       -> 0 
    CentralCycle_TablMax       -> 0 
    CentralCycle_EvenSum       -> 0 
    CentralCycle_OddSum        -> 0 
    CentralCycle_AccSum        -> 0 
    CentralCycle_AccRevSum     -> 0 
    CentralCycle_ColMiddle     -> 0 
    CentralCycle_CentralE      -> 0 
    CentralCycle_CentralO      -> 0 
    CentralCycle_PosHalf       -> 0 
    CentralCycle_TransNat0     -> 0 
    CentralCycle_TransNat1     -> 0 
    CentralCycle_TransSqrs     -> 0 
    CentralCycle_BinConv       -> 0 
    CentralCycle_InvBinConv    -> 0 
    CentralCycle_PolyRow3      -> 0 
    CentralCycle_PolyCol2      -> 0 
    CentralCycle_PolyCol3      -> 0 
    CentralCycle_PolyDiag      -> 0 
    CentralCycle_RevToff11     -> 0 
    CentralCycle_RevTrev11     -> 0 
    CentralCycle_RevTantidiag  -> 0 
    CentralCycle_RevTacc       -> 0 
    CentralCycle_RevTalt       -> 0 
    CentralCycle_RevTder       -> 0 
    CentralCycle_RevEvenSum    -> 0 
    CentralCycle_RevOddSum     -> 0 
    CentralCycle_RevAccRevSum  -> 0 
    CentralCycle_RevAntiDSum   -> 0 
    CentralCycle_RevColMiddle  -> 0 
    CentralCycle_RevCentralO   -> 0 
    CentralCycle_RevPosHalf    -> 0 
    CentralCycle_RevTransNat0  -> 0 
    CentralCycle_RevTransNat1  -> 0 
    CentralCycle_RevTransSqrs  -> 0 
    CentralCycle_RevPolyCol3   -> 0 
    CentralCycle_RevPolyDiag   -> 0 
    CentralCycle_TablCol0      -> https://oeis.org/A7
    CentralCycle_TablGcd       -> https://oeis.org/A12
    CentralCycle_RevPolyRow1   -> https://oeis.org/A12
    CentralCycle_PolyRow1      -> https://oeis.org/A27
    CentralCycle_TablCol1      -> https://oeis.org/A142
    CentralCycle_AntiDSum      -> https://oeis.org/A166
    CentralCycle_TablCol2      -> https://oeis.org/A276
    CentralCycle_TablCol3      -> https://oeis.org/A483
    CentralCycle_TablDiag1     -> https://oeis.org/A906
    CentralCycle_TablDiag2     -> https://oeis.org/A907
    CentralCycle_TablDiag0     -> https://oeis.org/A1147
    CentralCycle_NegHalf       -> https://oeis.org/A1662
    CentralCycle_TablDiag3     -> https://oeis.org/A1784
    CentralCycle_RevPolyRow2   -> https://oeis.org/A5408
    CentralCycle_RevNegHalf    -> https://oeis.org/A6351
    CentralCycle_TablSum       -> https://oeis.org/A32188
    CentralCycle_AbsSum        -> https://oeis.org/A32188
    CentralCycle_AltSum        -> https://oeis.org/A33999
    CentralCycle_PolyRow2      -> https://oeis.org/A45944
    CentralCycle_Tantidiag     -> https://oeis.org/A106828
    CentralCycle_Trev11        -> https://oeis.org/A111999
    CentralCycle_RevPolyRow3   -> https://oeis.org/A239325
    CentralCycle_Toff11        -> https://oeis.org/A259456
    CentralCycle_Triangle      -> https://oeis.org/A269940
    CentralCycle_Talt          -> https://oeis.org/A269940

    CentralCycle: Distinct: 23, Hits: 25, Misses: 40
'''
