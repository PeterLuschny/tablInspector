from functools import cache
from _tabltypes import Table
from Lah import lah

"""
Inverse of the Lah triangle.
A signed version of the Lah numbers.

[0] [1]
[1] [0,      1] 
[2] [0,     -2,        1] 
[3] [0,      6,       -6,       1] 
[4] [0,    -24,       36,     -12,       1] 
[5] [0,    120,     -240,     120,     -20,      1] 
[6] [0,   -720,     1800,   -1200,     300,    -30,      1] 
[7] [0,   5040,   -15120,   12600,   -4200,    630,    -42,    1] 
[8] [0, -40320,   141120, -141120,   58800, -11760,   1176,  -56,   1] 
[9] [0, 362880, -1451520, 1693440, -846720, 211680, -28224, 2016, -72, 1]
"""

@cache
def lahinv(n: int) -> list[int]:
    return [(-1)**(n - k) * lah(n)[k] for k in range(n+1)]


LahInv = Table(
    lahinv,
    "LahInv",
    ["A111596", "A271703", "A008297", "A066667", "A089231", "A105278"],
    "A271703",
    r"(-1)^{n-k} \binom{n}{k} \text{FallingFactorial}(n-1, n-k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(LahInv)


''' OEIS
    LahInv_Trev          -> 0
    LahInv_Trevinv       -> 0
    LahInv_Tacc          -> 0
    LahInv_Tder          -> 0
    LahInv_AccSum        -> 0
    LahInv_PolyRow3      -> 0
    LahInv_PolyCol3      -> 0
    LahInv_RevToff11     -> 0
    LahInv_RevTrev11     -> 0
    LahInv_RevTantidiag  -> 0
    LahInv_RevTacc       -> 0
    LahInv_RevTalt       -> 0
    LahInv_RevTder       -> 0
    LahInv_RevAccRevSum  -> 0
    LahInv_RevAntiDSum   -> 0
    LahInv_RevColMiddle  -> 0
    LahInv_RevNegHalf    -> 0
    LahInv_RevTransNat0  -> 0
    LahInv_RevTransNat1  -> 0
    LahInv_RevTransSqrs  -> 0
    LahInv_RevPolyCol3   -> 0
    LahInv_TablCol0      -> 7
    LahInv_TablDiag0     -> 12
    LahInv_RevPolyRow1   -> 12
    LahInv_PolyRow1      -> 27
    LahInv_TablCol1      -> 142
    LahInv_AltSum        -> 262
    LahInv_AbsSum        -> 262
    LahInv_AntiDSum      -> 1053
    LahInv_TablCol2      -> 1286
    LahInv_TablCol3      -> 1754
    LahInv_TablDiag1     -> 2378
    LahInv_TablGcd       -> 2378
    LahInv_TablMax       -> 2868
    LahInv_RevPolyRow3   -> 3154
    LahInv_RevPolyRow2   -> 5408
    LahInv_PolyRow2      -> 5563
    LahInv_NegHalf       -> 25168
    LahInv_TablDiag2     -> 83374
    LahInv_EvenSum       -> 88312
    LahInv_OddSum        -> 88313
    LahInv_Trev11        -> 89231
    LahInv_Trevinv11     -> 89231
    LahInv_RevOddSum     -> 96939
    LahInv_RevEvenSum    -> 96965
    LahInv_Toff11        -> 105278
    LahInv_Tinv11        -> 105278
    LahInv_TablSum       -> 111884
    LahInv_Tantidiag     -> 180047
    LahInv_CentralE      -> 187535
    LahInv_AccRevSum     -> 202410
    LahInv_TransNat1     -> 202410
    LahInv_RevCentralO   -> 248045
    LahInv_TablDiag3     -> 253285
    LahInv_TransSqrs     -> 256467
    LahInv_Triangle      -> 271703
    LahInv_Tinv          -> 271703
    LahInv_Talt          -> 271703
    LahInv_PolyDiag      -> 317279
    LahInv_PolyCol2      -> 317364
    LahInv_TransNat0     -> 317365
    LahInv_PosHalf       -> 318223
    LahInv_RevPolyDiag   -> 318224
    LahInv_ColMiddle     -> 343581
    LahInv_BinConv       -> 344050
    LahInv_InvBinConv    -> 344051
    LahInv_TablLcm       -> 359365
    LahInv_CentralO      -> 367776

    LahInv: Distinct: 39, Hits: 47, Misses: 21
'''