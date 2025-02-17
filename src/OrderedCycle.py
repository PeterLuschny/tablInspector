from functools import cache
from _tabltypes import Table

"""Ordered cycle numbers.

[0] [1]
[1] [0,    1]
[2] [0,    1,     2]
[3] [0,    2,     6,     6]
[4] [0,    6,    22,    36,     24]
[5] [0,   24,   100,   210,    240,    120]
[6] [0,  120,   548,  1350,   2040,   1800,    720]
[7] [0,  720,  3528,  9744,  17640,  21000,  15120,   5040]
[8] [0, 5040, 26136, 78792, 162456, 235200, 231840, 141120, 40320]
"""


@cache
def orderedcycle(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = orderedcycle(n - 1) + [0]
    row[n] = row[n] * n
    for k in range(n, 0, -1):
        row[k] = (n - 1) * row[k] + k * row[k - 1]
    return row


OrderedCycle = Table(
    orderedcycle,
    "OrderedCycle",
    ["A225479", "A048594", "A075181"],
    "",  # not invertible
    r"k! {n \brack k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(OrderedCycle)




''' OEIS
    OrderedCycle_Trev          -> 0 
    OrderedCycle_Tantidiag     -> 0 
    OrderedCycle_Tacc          -> 0 
    OrderedCycle_Tder          -> 0 
    OrderedCycle_TablDiag2     -> 0 
    OrderedCycle_TablDiag3     -> 0 
    OrderedCycle_TablLcm       -> 0 
    OrderedCycle_OddSum        -> 0 
    OrderedCycle_AccSum        -> 0 
    OrderedCycle_CentralO      -> 0 
    OrderedCycle_TransSqrs     -> 0 
    OrderedCycle_PolyRow3      -> 0 
    OrderedCycle_RevToff11     -> 0 
    OrderedCycle_RevTrev11     -> 0 
    OrderedCycle_RevTantidiag  -> 0 
    OrderedCycle_RevTacc       -> 0 
    OrderedCycle_RevTalt       -> 0 
    OrderedCycle_RevTder       -> 0 
    OrderedCycle_RevEvenSum    -> 0 
    OrderedCycle_RevOddSum     -> 0 
    OrderedCycle_RevAccRevSum  -> 0 
    OrderedCycle_RevAntiDSum   -> 0 
    OrderedCycle_RevColMiddle  -> 0 
    OrderedCycle_RevTransNat0  -> 0 
    OrderedCycle_RevTransNat1  -> 0 
    OrderedCycle_RevTransSqrs  -> 0 
    OrderedCycle_TablCol0      -> https://oeis.org/A7
    OrderedCycle_RevPolyRow1   -> https://oeis.org/A12
    OrderedCycle_PolyRow1      -> https://oeis.org/A27
    OrderedCycle_RevPolyRow2   -> https://oeis.org/A27
    OrderedCycle_TablCol1      -> https://oeis.org/A142
    OrderedCycle_TablDiag0     -> https://oeis.org/A142
    OrderedCycle_TablDiag1     -> https://oeis.org/A1286
    OrderedCycle_AltSum        -> https://oeis.org/A6252
    OrderedCycle_TablSum       -> https://oeis.org/A7840
    OrderedCycle_AbsSum        -> https://oeis.org/A7840
    OrderedCycle_PolyRow2      -> https://oeis.org/A14105
    OrderedCycle_Toff11        -> https://oeis.org/A48594
    OrderedCycle_RevPolyRow3   -> https://oeis.org/A51890
    OrderedCycle_TablCol2      -> https://oeis.org/A52517
    OrderedCycle_TablCol3      -> https://oeis.org/A52748
    OrderedCycle_AccRevSum     -> https://oeis.org/A52801
    OrderedCycle_TransNat1     -> https://oeis.org/A52801
    OrderedCycle_EvenSum       -> https://oeis.org/A52811
    OrderedCycle_TablMax       -> https://oeis.org/A58583
    OrderedCycle_Trev11        -> https://oeis.org/A75181
    OrderedCycle_TablGcd       -> https://oeis.org/A75182
    OrderedCycle_PolyCol2      -> https://oeis.org/A88500
    OrderedCycle_RevPosHalf    -> https://oeis.org/A88500
    OrderedCycle_RevNegHalf    -> https://oeis.org/A88501
    OrderedCycle_AntiDSum      -> https://oeis.org/A129841
    OrderedCycle_TransNat0     -> https://oeis.org/A215916
    OrderedCycle_Triangle      -> https://oeis.org/A225479
    OrderedCycle_Talt          -> https://oeis.org/A225479
    OrderedCycle_PosHalf       -> https://oeis.org/A227917
    OrderedCycle_RevCentralO   -> https://oeis.org/A238685
    OrderedCycle_BinConv       -> https://oeis.org/A277759
    OrderedCycle_InvBinConv    -> https://oeis.org/A308565
    OrderedCycle_PolyDiag      -> https://oeis.org/A317171
    OrderedCycle_ColMiddle     -> https://oeis.org/A344498
    OrderedCycle_RevPolyCol3   -> https://oeis.org/A352069
    OrderedCycle_RevPolyDiag   -> https://oeis.org/A352074
    OrderedCycle_NegHalf       -> https://oeis.org/A354237
    OrderedCycle_PolyCol3      -> https://oeis.org/A354263
    OrderedCycle_CentralE      -> https://oeis.org/A376873

    OrderedCycle: Distinct: 34, Hits: 39, Misses: 26
'''
