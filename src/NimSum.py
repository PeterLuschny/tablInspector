from functools import cache
from _tabltypes import Table


"""n XOR k (or Nim-sum of n and k).

[0] 0;
[1] 1,  1;
[2] 2,  0,  2;
[3] 3,  3,  3,  3;
[4] 4,  2,  0,  2,  4;
[5] 5,  5,  1,  1,  5,  5;
[6] 6,  4,  6,  0,  6,  4,  6;
[7] 7,  7,  7,  7,  7,  7,  7,  7;
[8] 8,  6,  4,  6,  0,  6,  4,  6,  8;
[9] 9,  9,  5,  5,  1,  1,  5,  5,  9,  9;
"""


@cache
def nimsum(n: int) -> list[int]:
    return [k ^ (n - k) for k in range(n + 1)]


NimSum = Table(
    nimsum, 
    "NimSum", 
    ["A003987"], 
    "",
    r"k \ \text{XOR} \ (n - k)"
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(NimSum)






''' OEIS
    NimSum_Toff11        -> 0 
    NimSum_Trev11        -> 0 
    NimSum_Tantidiag     -> 0 
    NimSum_Tacc          -> 0 
    NimSum_Tder          -> 0 
    NimSum_TablLcm       -> 0 
    NimSum_TablGcd       -> 0 
    NimSum_EvenSum       -> 0 
    NimSum_OddSum        -> 0 
    NimSum_AltSum        -> 0 
    NimSum_AccSum        -> 0 
    NimSum_AccRevSum     -> 0 
    NimSum_AntiDSum      -> 0 
    NimSum_PosHalf       -> 0 
    NimSum_NegHalf       -> 0 
    NimSum_TransNat0     -> 0 
    NimSum_TransNat1     -> 0 
    NimSum_TransSqrs     -> 0 
    NimSum_BinConv       -> 0 
    NimSum_InvBinConv    -> 0 
    NimSum_PolyRow3      -> 0 
    NimSum_PolyCol2      -> 0 
    NimSum_PolyCol3      -> 0 
    NimSum_PolyDiag      -> 0 
    NimSum_RevToff11     -> 0 
    NimSum_RevTrev11     -> 0 
    NimSum_RevTantidiag  -> 0 
    NimSum_RevTacc       -> 0 
    NimSum_RevTder       -> 0 
    NimSum_RevEvenSum    -> 0 
    NimSum_RevOddSum     -> 0 
    NimSum_RevAccRevSum  -> 0 
    NimSum_RevAntiDSum   -> 0 
    NimSum_RevPosHalf    -> 0 
    NimSum_RevNegHalf    -> 0 
    NimSum_RevTransNat0  -> 0 
    NimSum_RevTransNat1  -> 0 
    NimSum_RevTransSqrs  -> 0 
    NimSum_RevPolyRow3   -> 0 
    NimSum_RevPolyCol3   -> 0 
    NimSum_RevPolyDiag   -> 0 
    NimSum_CentralE      -> https://oeis.org/A4
    NimSum_TablCol0      -> https://oeis.org/A27
    NimSum_TablDiag0     -> https://oeis.org/A27
    NimSum_TablMax       -> https://oeis.org/A27
    NimSum_PolyRow1      -> https://oeis.org/A27
    NimSum_RevPolyRow1   -> https://oeis.org/A27
    NimSum_Triangle      -> https://oeis.org/A3987
    NimSum_Trev          -> https://oeis.org/A3987
    NimSum_Talt          -> https://oeis.org/A3987
    NimSum_RevTalt       -> https://oeis.org/A3987
    NimSum_TablCol1      -> https://oeis.org/A4442
    NimSum_TablDiag1     -> https://oeis.org/A4442
    NimSum_TablCol2      -> https://oeis.org/A4443
    NimSum_TablDiag2     -> https://oeis.org/A4443
    NimSum_TablCol3      -> https://oeis.org/A4444
    NimSum_TablDiag3     -> https://oeis.org/A4444
    NimSum_PolyRow2      -> https://oeis.org/A5893
    NimSum_RevPolyRow2   -> https://oeis.org/A5893
    NimSum_CentralO      -> https://oeis.org/A38712
    NimSum_RevCentralO   -> https://oeis.org/A38712
    NimSum_ColMiddle     -> https://oeis.org/A135481
    NimSum_RevColMiddle  -> https://oeis.org/A135481
    NimSum_TablSum       -> https://oeis.org/A375551
    NimSum_AbsSum        -> https://oeis.org/A375551

    NimSum: Distinct: 11, Hits: 24, Misses: 41
'''
