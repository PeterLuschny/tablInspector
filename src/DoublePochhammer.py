from functools import cache
from Tables import Table

"""
DoublePochhammer

[0] 1;
[1] 0,      1;
[2] 0,      2,      1;
[3] 0,      8,      6,      1;
[4] 0,     48,     44,     12,      1;
[5] 0,    384,    400,    140,     20,     1;
[6] 0,   3840,   4384,   1800,    340,    30,    1;
[7] 0,  46080,  56448,  25984,   5880,   700,   42,  1;
[8] 0, 645120, 836352, 420224, 108304, 15680, 1288, 56, 1;
"""

@cache
def doublepochhammer(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = doublepochhammer(n - 1) + [1]
    for k in range(n - 1, 0, -1):
        row[k] = row[k - 1] + 2 * (n - 1) * row[k]
    return row


DoublePochhammer = Table(
    doublepochhammer,
    "DoublePochhammer",
    ["A039683"],
    "A00000",
    r"[x^k]\, x(x-2)(x-4)...(x-2n+2)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(DoublePochhammer)  # type: ignore






''' OEIS
    DoublePochhammer_Tinv          -> 0 
    DoublePochhammer_Trev          -> 0 
    DoublePochhammer_Trevinv       -> 0 
    DoublePochhammer_Trev11        -> 0 
    DoublePochhammer_Trevinv11     -> 0 
    DoublePochhammer_Tantidiag     -> 0 
    DoublePochhammer_Tacc          -> 0 
    DoublePochhammer_Talt          -> 0 
    DoublePochhammer_Tder          -> 0 
    DoublePochhammer_TablCol3      -> 0 
    DoublePochhammer_TablDiag3     -> 0 
    DoublePochhammer_TablLcm       -> 0 
    DoublePochhammer_TablMax       -> 0 
    DoublePochhammer_AccSum        -> 0 
    DoublePochhammer_ColMiddle     -> 0 
    DoublePochhammer_CentralE      -> 0 
    DoublePochhammer_CentralO      -> 0 
    DoublePochhammer_TransSqrs     -> 0 
    DoublePochhammer_BinConv       -> 0 
    DoublePochhammer_InvBinConv    -> 0 
    DoublePochhammer_RevToff11     -> 0 
    DoublePochhammer_RevTrev11     -> 0 
    DoublePochhammer_RevTantidiag  -> 0 
    DoublePochhammer_RevTacc       -> 0 
    DoublePochhammer_RevTalt       -> 0 
    DoublePochhammer_RevTder       -> 0 
    DoublePochhammer_RevEvenSum    -> 0 
    DoublePochhammer_RevOddSum     -> 0 
    DoublePochhammer_RevAccRevSum  -> 0 
    DoublePochhammer_RevAntiDSum   -> 0 
    DoublePochhammer_RevColMiddle  -> 0 
    DoublePochhammer_RevCentralO   -> 0 
    DoublePochhammer_RevTransNat0  -> 0 
    DoublePochhammer_RevTransNat1  -> 0 
    DoublePochhammer_RevTransSqrs  -> 0 
    DoublePochhammer_RevPolyDiag   -> 0 
    DoublePochhammer_TablCol0      -> https://oeis.org/A7
    DoublePochhammer_TablDiag0     -> https://oeis.org/A12
    DoublePochhammer_RevPolyRow1   -> https://oeis.org/A12
    DoublePochhammer_PolyRow1      -> https://oeis.org/A27
    DoublePochhammer_TablCol1      -> https://oeis.org/A165
    DoublePochhammer_PolyCol2      -> https://oeis.org/A165
    DoublePochhammer_RevPosHalf    -> https://oeis.org/A165
    DoublePochhammer_TablSum       -> https://oeis.org/A1147
    DoublePochhammer_AltSum        -> https://oeis.org/A1147
    DoublePochhammer_AbsSum        -> https://oeis.org/A1147
    DoublePochhammer_PolyCol3      -> https://oeis.org/A1147
    DoublePochhammer_OddSum        -> https://oeis.org/A1193
    DoublePochhammer_EvenSum       -> https://oeis.org/A1879
    DoublePochhammer_TablDiag1     -> https://oeis.org/A2378
    DoublePochhammer_TransNat0     -> https://oeis.org/A4041
    DoublePochhammer_RevPolyRow2   -> https://oeis.org/A5408
    DoublePochhammer_PolyRow2      -> https://oeis.org/A5563
    DoublePochhammer_PosHalf       -> https://oeis.org/A7696
    DoublePochhammer_RevPolyCol3   -> https://oeis.org/A8542
    DoublePochhammer_NegHalf       -> https://oeis.org/A8545
    DoublePochhammer_RevPolyRow3   -> https://oeis.org/A14634
    DoublePochhammer_TablDiag2     -> https://oeis.org/A36464
    DoublePochhammer_Triangle      -> https://oeis.org/A39683
    DoublePochhammer_Toff11        -> https://oeis.org/A39683
    DoublePochhammer_TablGcd       -> https://oeis.org/A65176
    DoublePochhammer_Tinv11        -> https://oeis.org/A75497
    DoublePochhammer_PolyDiag      -> https://oeis.org/A113551
    DoublePochhammer_AccRevSum     -> https://oeis.org/A114160
    DoublePochhammer_TransNat1     -> https://oeis.org/A114160
    DoublePochhammer_RevNegHalf    -> https://oeis.org/A130706
    DoublePochhammer_TablCol2      -> https://oeis.org/A203159
    DoublePochhammer_AntiDSum      -> https://oeis.org/A353255
    DoublePochhammer_PolyRow3      -> https://oeis.org/A370912

    DoublePochhammer: Distinct: 26, Hits: 33, Misses: 36
'''
