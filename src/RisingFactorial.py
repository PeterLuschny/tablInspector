from functools import cache
from _tabltypes import Table

"""Rising factorial.

[0]  1;
[1]  1, 1;
[2]  1, 2,   6;
[3]  1, 3,  12,  60;
[4]  1, 4,  20, 120,  840;
[5]  1, 5,  30, 210, 1680, 15120;
[6]  1, 6,  42, 336, 3024, 30240, 332640;
[7]  1, 7,  56, 504, 5040, 55440, 665280, 8648640;
"""


@cache
def risingfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1 for _ in range(n + 1)]
    row[1] = n
    for k in range(1, n):
        row[k + 1] = row[k] * (n + k)
    return row


RisingFactorial = Table(
    risingfactorial, 
    "RisingFactorial", 
    ["A124320"], 
    "", 
    r"k! \binom{n+k-1}{k}",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(RisingFactorial)


''' OEIS
    RisingFactorial_Trev          -> 0 
    RisingFactorial_Tinvrev       -> 0 
    RisingFactorial_Toff11        -> 0 
    RisingFactorial_Trev11        -> 0 
    RisingFactorial_Tantidiag     -> 0 
    RisingFactorial_Tacc          -> 0 
    RisingFactorial_Tder          -> 0 
    RisingFactorial_EvenSum       -> 0 
    RisingFactorial_OddSum        -> 0 
    RisingFactorial_AltSum        -> 0 
    RisingFactorial_AccSum        -> 0 
    RisingFactorial_AccRevSum     -> 0 
    RisingFactorial_AntiDSum      -> 0 
    RisingFactorial_ColMiddle     -> 0 
    RisingFactorial_PosHalf       -> 0 
    RisingFactorial_NegHalf       -> 0 
    RisingFactorial_TransNat0     -> 0 
    RisingFactorial_TransNat1     -> 0 
    RisingFactorial_TransSqrs     -> 0 
    RisingFactorial_PolyRow3      -> 0 
    RisingFactorial_PolyCol2      -> 0 
    RisingFactorial_PolyCol3      -> 0 
    RisingFactorial_PolyDiag      -> 0 
    RisingFactorial_RevToff11     -> 0 
    RisingFactorial_RevTrev11     -> 0 
    RisingFactorial_RevTinv11     -> 0 
    RisingFactorial_RevTantidiag  -> 0 
    RisingFactorial_RevTacc       -> 0 
    RisingFactorial_RevTalt       -> 0 
    RisingFactorial_RevTder       -> 0 
    RisingFactorial_RevEvenSum    -> 0 
    RisingFactorial_RevOddSum     -> 0 
    RisingFactorial_RevAccRevSum  -> 0 
    RisingFactorial_RevAntiDSum   -> 0 
    RisingFactorial_RevColMiddle  -> 0 
    RisingFactorial_RevCentralO   -> 0 
    RisingFactorial_RevNegHalf    -> 0 
    RisingFactorial_RevTransNat0  -> 0 
    RisingFactorial_RevTransNat1  -> 0 
    RisingFactorial_RevTransSqrs  -> 0 
    RisingFactorial_RevPolyRow3   -> 0 
    RisingFactorial_RevPolyCol3   -> 0 
    RisingFactorial_RevPolyDiag   -> 0 
    RisingFactorial_TablCol0      -> https://oeis.org/A12
    RisingFactorial_TablCol1      -> https://oeis.org/A27
    RisingFactorial_TablGcd       -> https://oeis.org/A27
    RisingFactorial_PolyRow1      -> https://oeis.org/A27
    RisingFactorial_RevPolyRow1   -> https://oeis.org/A27
    RisingFactorial_TablDiag0     -> https://oeis.org/A407
    RisingFactorial_TablLcm       -> https://oeis.org/A407
    RisingFactorial_TablMax       -> https://oeis.org/A407
    RisingFactorial_TablDiag3     -> https://oeis.org/A1761
    RisingFactorial_TablDiag1     -> https://oeis.org/A1813
    RisingFactorial_TablCol2      -> https://oeis.org/A2378
    RisingFactorial_TablDiag2     -> https://oeis.org/A6963
    RisingFactorial_TablCol3      -> https://oeis.org/A7531
    RisingFactorial_CentralO      -> https://oeis.org/A64352
    RisingFactorial_RevPolyRow2   -> https://oeis.org/A117951
    RisingFactorial_TablSum       -> https://oeis.org/A123680
    RisingFactorial_AbsSum        -> https://oeis.org/A123680
    RisingFactorial_Triangle      -> https://oeis.org/A124320
    RisingFactorial_Talt          -> https://oeis.org/A124320
    RisingFactorial_PolyRow2      -> https://oeis.org/A136392
    RisingFactorial_InvBinConv    -> https://oeis.org/A278069
    RisingFactorial_BinConv       -> https://oeis.org/A278070
    RisingFactorial_CentralE      -> https://oeis.org/A352601

    RisingFactorial: Distinct: 17, Hits: 23, Misses: 43
'''
