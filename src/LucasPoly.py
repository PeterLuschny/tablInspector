from functools import cache
from _tabltypes import Table

"""Lucas polynomials (unsigned coefficients).
  [ 0]  1;
  [ 1]  1,  0;
  [ 2]  1,  1,  1;
  [ 3]  1,  2,  1,  0;
  [ 4]  1,  3,  1,  1,  1;
  [ 5]  1,  4,  1,  3,  2,  0;
  [ 6]  1,  5,  1,  6,  3,  1,  1;
  [ 7]  1,  6,  1, 10,  4,  4,  3,  0;
  [ 8]  1,  7,  1, 15,  5, 10,  6,  1,  1;
  [ 9]  1,  8,  1, 21,  6, 20, 10,  5,  4,  0;
  [10]  1,  9,  1, 28,  7, 35, 15, 15, 10,  1, 1;
"""


@cache
def lucaspoly(n: int) -> list[int]:
    if n == 0: return [1]
    if n == 1: return [1, 0]
    if n == 2: return [1, 1, 1]

    rowA = lucaspoly(n - 2)
    row  = lucaspoly(n - 1) + [(n + 1) % 2]
    row[1] += 1

    for k in range(3, n):
        row[k] += rowA[k - 2]

    return row


LucasPoly = Table(
    lucaspoly, 
    "LucasPoly", 
    ["A374440"], 
    "", 
    r"T_{n - 1, k} + T_{n - 2, k - 2}"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(LucasPoly)




''' OEIS
    LucasPoly_Trev          -> 0 
    LucasPoly_Tinvrev       -> 0 
    LucasPoly_Toff11        -> 0 
    LucasPoly_Trev11        -> 0 
    LucasPoly_Tantidiag     -> 0 
    LucasPoly_Tacc          -> 0 
    LucasPoly_Tder          -> 0 
    LucasPoly_TablDiag2     -> 0 
    LucasPoly_TablDiag3     -> 0 
    LucasPoly_AccSum        -> 0 
    LucasPoly_AccRevSum     -> 0 
    LucasPoly_AntiDSum      -> 0 
    LucasPoly_ColMiddle     -> 0 
    LucasPoly_CentralE      -> 0 
    LucasPoly_CentralO      -> 0 
    LucasPoly_PosHalf       -> 0 
    LucasPoly_NegHalf       -> 0 
    LucasPoly_TransNat0     -> 0 
    LucasPoly_TransNat1     -> 0 
    LucasPoly_TransSqrs     -> 0 
    LucasPoly_BinConv       -> 0 
    LucasPoly_InvBinConv    -> 0 
    LucasPoly_PolyCol2      -> 0 
    LucasPoly_PolyCol3      -> 0 
    LucasPoly_PolyDiag      -> 0 
    LucasPoly_RevToff11     -> 0 
    LucasPoly_RevTrev11     -> 0 
    LucasPoly_RevTinv11     -> 0 
    LucasPoly_RevTantidiag  -> 0 
    LucasPoly_RevTacc       -> 0 
    LucasPoly_RevTalt       -> 0 
    LucasPoly_RevTder       -> 0 
    LucasPoly_RevEvenSum    -> 0 
    LucasPoly_RevOddSum     -> 0 
    LucasPoly_RevAccRevSum  -> 0 
    LucasPoly_RevColMiddle  -> 0 
    LucasPoly_RevCentralO   -> 0 
    LucasPoly_RevPosHalf    -> 0 
    LucasPoly_RevNegHalf    -> 0 
    LucasPoly_RevTransNat0  -> 0 
    LucasPoly_RevTransNat1  -> 0 
    LucasPoly_RevTransSqrs  -> 0 
    LucasPoly_RevPolyCol3   -> 0 
    LucasPoly_RevPolyDiag   -> 0 
    LucasPoly_TablCol0      -> https://oeis.org/A12
    LucasPoly_TablCol2      -> https://oeis.org/A12
    LucasPoly_PolyRow1      -> https://oeis.org/A12
    LucasPoly_TablCol1      -> https://oeis.org/A27
    LucasPoly_RevPolyRow1   -> https://oeis.org/A27
    LucasPoly_TablSum       -> https://oeis.org/A32
    LucasPoly_AbsSum        -> https://oeis.org/A32
    LucasPoly_TablDiag0     -> https://oeis.org/A35
    LucasPoly_OddSum        -> https://oeis.org/A71
    LucasPoly_TablCol3      -> https://oeis.org/A217
    LucasPoly_PolyRow3      -> https://oeis.org/A290
    LucasPoly_EvenSum       -> https://oeis.org/A1611
    LucasPoly_AltSum        -> https://oeis.org/A1911
    LucasPoly_PolyRow2      -> https://oeis.org/A2061
    LucasPoly_RevPolyRow2   -> https://oeis.org/A2061
    LucasPoly_TablLcm       -> https://oeis.org/A25560
    LucasPoly_RevPolyRow3   -> https://oeis.org/A45991
    LucasPoly_TablDiag1     -> https://oeis.org/A57979
    LucasPoly_TablMax       -> https://oeis.org/A73028
    LucasPoly_RevAntiDSum   -> https://oeis.org/A86341
    LucasPoly_TablGcd       -> https://oeis.org/A257696
    LucasPoly_Triangle      -> https://oeis.org/A374440
    LucasPoly_Talt          -> https://oeis.org/A374440

    LucasPoly: Distinct: 18, Hits: 23, Misses: 44
'''
