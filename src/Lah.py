from functools import cache
from _tabltypes import Table

"""Lah numbers (unsigned).


[0]  1
[1]  0       1
[2]  0       2        1
[3]  0       6        6        1
[4]  0      24       36       12        1
[5]  0     120      240      120       20       1
[6]  0     720     1800     1200      300      30      1
[7]  0    5040    15120    12600     4200     630     42     1
[8]  0   40320   141120   141120    58800   11760   1176    56    1
[9]  0  362880  1451520  1693440   846720  211680  28224  2016   72   1
"""


@cache
def lah(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = lah(n - 1) + [1]
    row[0] = 0
    for k in range(n - 1, 0, -1):
        row[k] = row[k] * (n + k - 1) + row[k - 1]
    return row


Lah = Table(
    lah,
    "Lah",
    ["A271703", "A008297", "A066667", "A089231", "A105278", "A111596"],
    "A111596",
    r"\binom{n}{k} \text{FallingFactorial}(n-1, n-k)",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Lah)






''' OEIS
    Lah_Trev          -> 0 
    Lah_Trevinv       -> 0 
    Lah_Tder          -> 0 
    Lah_RevToff11     -> 0 
    Lah_RevTrev11     -> 0 
    Lah_RevTantidiag  -> 0 
    Lah_RevTacc       -> 0 
    Lah_RevTalt       -> 0 
    Lah_RevTder       -> 0 
    Lah_RevAntiDSum   -> 0 
    Lah_RevColMiddle  -> 0 
    Lah_RevTransNat0  -> 0 
    Lah_RevTransSqrs  -> 0 
    Lah_TablCol0      -> https://oeis.org/A7
    Lah_TablDiag0     -> https://oeis.org/A12
    Lah_RevPolyRow1   -> https://oeis.org/A12
    Lah_PolyRow1      -> https://oeis.org/A27
    Lah_TablCol1      -> https://oeis.org/A142
    Lah_TablSum       -> https://oeis.org/A262
    Lah_AbsSum        -> https://oeis.org/A262
    Lah_AntiDSum      -> https://oeis.org/A1053
    Lah_TablCol2      -> https://oeis.org/A1286
    Lah_TablCol3      -> https://oeis.org/A1754
    Lah_TablDiag1     -> https://oeis.org/A2378
    Lah_TablGcd       -> https://oeis.org/A2378
    Lah_AccRevSum     -> https://oeis.org/A2720
    Lah_TransNat1     -> https://oeis.org/A2720
    Lah_TablMax       -> https://oeis.org/A2868
    Lah_RevPolyRow3   -> https://oeis.org/A3154
    Lah_RevPolyRow2   -> https://oeis.org/A5408
    Lah_PolyRow2      -> https://oeis.org/A5563
    Lah_PosHalf       -> https://oeis.org/A25168
    Lah_TransNat0     -> https://oeis.org/A52852
    Lah_PolyCol2      -> https://oeis.org/A52897
    Lah_RevPosHalf    -> https://oeis.org/A52897
    Lah_AccSum        -> https://oeis.org/A62147
    Lah_RevAccRevSum  -> https://oeis.org/A62147
    Lah_RevTransNat1  -> https://oeis.org/A62147
    Lah_TablDiag2     -> https://oeis.org/A83374
    Lah_EvenSum       -> https://oeis.org/A88312
    Lah_OddSum        -> https://oeis.org/A88313
    Lah_Trev11        -> https://oeis.org/A89231
    Lah_Trevinv11     -> https://oeis.org/A89231
    Lah_RevOddSum     -> https://oeis.org/A96939
    Lah_RevEvenSum    -> https://oeis.org/A96965
    Lah_TransSqrs     -> https://oeis.org/A103194
    Lah_Toff11        -> https://oeis.org/A105278
    Lah_Tinv11        -> https://oeis.org/A105278
    Lah_AltSum        -> https://oeis.org/A111884
    Lah_Tantidiag     -> https://oeis.org/A180047
    Lah_CentralE      -> https://oeis.org/A187535
    Lah_PolyRow3      -> https://oeis.org/A226514
    Lah_RevCentralO   -> https://oeis.org/A248045
    Lah_TablDiag3     -> https://oeis.org/A253285
    Lah_PolyCol3      -> https://oeis.org/A255806
    Lah_Triangle      -> https://oeis.org/A271703
    Lah_Tinv          -> https://oeis.org/A271703
    Lah_Talt          -> https://oeis.org/A271703
    Lah_PolyDiag      -> https://oeis.org/A293145
    Lah_RevPolyDiag   -> https://oeis.org/A293146
    Lah_RevNegHalf    -> https://oeis.org/A317364
    Lah_NegHalf       -> https://oeis.org/A318223
    Lah_RevPolyCol3   -> https://oeis.org/A321837
    Lah_ColMiddle     -> https://oeis.org/A343581
    Lah_InvBinConv    -> https://oeis.org/A344050
    Lah_BinConv       -> https://oeis.org/A344051
    Lah_Tacc          -> https://oeis.org/A349776
    Lah_TablLcm       -> https://oeis.org/A359365
    Lah_CentralO      -> https://oeis.org/A367776

    Lah: Distinct: 46, Hits: 56, Misses: 13
'''
