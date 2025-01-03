from functools import cache
from _tabltypes import Table


"""Jacobsthal polynomials.

  [0]   1;
  [1]   1,   1;
  [2]   1,   2,    1;
  [3]   3,   5,    3,    1;
  [4]   5,  12,   10,    4,   1;
  [5]  11,  27,   28,   16,   5,   1;
  [6]  21,  62,   75,   52,  23,   6,   1;
  [7]  43, 137,  193,  159,  85,  31,   7,  1;
  [8]  85, 304,  480,  456, 290, 128,  40,  8, 1;
  [9] 171, 663, 1170, 1254, 916, 480, 182, 50, 9, 1;
"""


@cache
def jacobsthal(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 1]
    if n == 2: return [1, 2, 1]

    Jn1 = jacobsthal(n - 1)
    Jn2 = jacobsthal(n - 2) + [0]
    row = [1] * (n + 1)
    for k in range(1, n):
        row[k] = Jn1[k-1] + Jn1[k] + 2 * Jn2[k]
    row[0] = Jn1[0] + 2 * Jn2[0]
    return row


Jacobsthal = Table(
    jacobsthal,
    "Jacobsthal",
    ["A322942"],
    "A000000",
    r"[x^k]\ ((x+1)\, \mathrm{J}(n-1, x) + 2\, \mathrm{J}(n-2, x))",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Jacobsthal)


''' OEIS
    Jacobsthal_Trev          -> 0 
    Jacobsthal_Toff11        -> 0 
    Jacobsthal_Trev11        -> 0 
    Jacobsthal_Tinv11        -> 0 
    Jacobsthal_Tantidiag     -> 0 
    Jacobsthal_Tacc          -> 0 
    Jacobsthal_Tder          -> 0 
    Jacobsthal_TablCol2      -> 0 
    Jacobsthal_TablCol3      -> 0 
    Jacobsthal_TablDiag3     -> 0 
    Jacobsthal_TablLcm       -> 0 
    Jacobsthal_TablMax       -> 0 
    Jacobsthal_AccSum        -> 0 
    Jacobsthal_ColMiddle     -> 0 
    Jacobsthal_CentralE      -> 0 
    Jacobsthal_CentralO      -> 0 
    Jacobsthal_TransSqrs     -> 0 
    Jacobsthal_BinConv       -> 0 
    Jacobsthal_InvBinConv    -> 0 
    Jacobsthal_PolyCol2      -> 0 
    Jacobsthal_PolyCol3      -> 0 
    Jacobsthal_PolyDiag      -> 0 
    Jacobsthal_RevToff11     -> 0 
    Jacobsthal_RevTrev11     -> 0 
    Jacobsthal_RevTantidiag  -> 0 
    Jacobsthal_RevTacc       -> 0 
    Jacobsthal_RevTalt       -> 0 
    Jacobsthal_RevTder       -> 0 
    Jacobsthal_RevAccRevSum  -> 0 
    Jacobsthal_RevAntiDSum   -> 0 
    Jacobsthal_RevColMiddle  -> 0 
    Jacobsthal_RevCentralO   -> 0 
    Jacobsthal_RevTransNat0  -> 0 
    Jacobsthal_RevTransNat1  -> 0 
    Jacobsthal_RevTransSqrs  -> 0 
    Jacobsthal_RevPolyRow3   -> 0 
    Jacobsthal_RevPolyCol3   -> 0 
    Jacobsthal_RevPolyDiag   -> 0 
    Jacobsthal_AltSum        -> https://oeis.org/A7
    Jacobsthal_TablDiag0     -> https://oeis.org/A12
    Jacobsthal_TablGcd       -> https://oeis.org/A12
    Jacobsthal_TablDiag1     -> https://oeis.org/A27
    Jacobsthal_PolyRow1      -> https://oeis.org/A27
    Jacobsthal_RevPolyRow1   -> https://oeis.org/A27
    Jacobsthal_PolyRow2      -> https://oeis.org/A290
    Jacobsthal_RevPolyRow2   -> https://oeis.org/A290
    Jacobsthal_TablCol0      -> https://oeis.org/A1045
    Jacobsthal_RevNegHalf    -> https://oeis.org/A1045
    Jacobsthal_EvenSum       -> https://oeis.org/A2605
    Jacobsthal_OddSum        -> https://oeis.org/A2605
    Jacobsthal_RevEvenSum    -> https://oeis.org/A2605
    Jacobsthal_RevOddSum     -> https://oeis.org/A2605
    Jacobsthal_AntiDSum      -> https://oeis.org/A6138
    Jacobsthal_NegHalf       -> https://oeis.org/A15443
    Jacobsthal_TablSum       -> https://oeis.org/A28860
    Jacobsthal_AbsSum        -> https://oeis.org/A28860
    Jacobsthal_TablDiag2     -> https://oeis.org/A52905
    Jacobsthal_PolyRow3      -> https://oeis.org/A54602
    Jacobsthal_TablCol1      -> https://oeis.org/A91596
    Jacobsthal_Triangle      -> https://oeis.org/A322942
    Jacobsthal_Talt          -> https://oeis.org/A322942
    Jacobsthal_PosHalf       -> https://oeis.org/A323232
    Jacobsthal_Tinv          -> https://oeis.org/A330794
    Jacobsthal_TransNat0     -> https://oeis.org/A331319
    Jacobsthal_AccRevSum     -> https://oeis.org/A331320
    Jacobsthal_TransNat1     -> https://oeis.org/A331320

    Jacobsthal: Distinct: 18, Hits: 28, Misses: 38
'''
