from functools import cache
from Binomial import binomial
from _tabltypes import Table

"""Parades triangle.
  [0] 1;
  [1] 0, 0;
  [2] 0, 1,  0;
  [3] 0, 1,  1,   0;
  [4] 0, 1,  5,   1,   0;
  [5] 0, 1, 13,  13,   1,  0;
  [6] 0, 1, 29,  73,  29,  1, 0;
  [7] 0, 1, 61, 301, 301, 61, 1, 0;
"""

@cache
def A(n: int, k: int) -> int:
    if n == 0:
        return int(k == 0)
    if k > n:
        n, k = k, n

    b = binomial(k + 1)
    return k * A(n - 1, k) + sum(b[j + 1] * A(n - 1, k - j)
                             for j in range(1, k + 1))


@cache
def parades(n: int) -> list[int]:
    return [A(n - k, k) for k in range(n + 1)]


Parades = Table(
    parades,
    "Parades",
    ["A371761", "A272644"],
    "",
    r"\sum_{j=0}^{k} \, {n - k \brace j} \, {k \brace j} \, (j!)^2"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Parades)






''' OEIS
    Parades_Toff11        -> 0 
    Parades_Trev11        -> 0 
    Parades_Tantidiag     -> 0 
    Parades_Tacc          -> 0 
    Parades_Tder          -> 0 
    Parades_TablLcm       -> 0 
    Parades_TablGcd       -> 0 
    Parades_EvenSum       -> 0 
    Parades_OddSum        -> 0 
    Parades_AccSum        -> 0 
    Parades_AccRevSum     -> 0 
    Parades_AntiDSum      -> 0 
    Parades_CentralO      -> 0 
    Parades_PosHalf       -> 0 
    Parades_NegHalf       -> 0 
    Parades_TransNat0     -> 0 
    Parades_TransNat1     -> 0 
    Parades_TransSqrs     -> 0 
    Parades_PolyCol2      -> 0 
    Parades_PolyCol3      -> 0 
    Parades_PolyDiag      -> 0 
    Parades_RevToff11     -> 0 
    Parades_RevTrev11     -> 0 
    Parades_RevTantidiag  -> 0 
    Parades_RevTacc       -> 0 
    Parades_RevTder       -> 0 
    Parades_RevEvenSum    -> 0 
    Parades_RevOddSum     -> 0 
    Parades_RevAccRevSum  -> 0 
    Parades_RevAntiDSum   -> 0 
    Parades_RevCentralO   -> 0 
    Parades_RevPosHalf    -> 0 
    Parades_RevNegHalf    -> 0 
    Parades_RevTransNat0  -> 0 
    Parades_RevTransNat1  -> 0 
    Parades_RevTransSqrs  -> 0 
    Parades_RevPolyCol3   -> 0 
    Parades_RevPolyDiag   -> 0 
    Parades_PolyRow1      -> https://oeis.org/A4
    Parades_RevPolyRow1   -> https://oeis.org/A4
    Parades_TablCol0      -> https://oeis.org/A7
    Parades_TablDiag0     -> https://oeis.org/A7
    Parades_TablCol1      -> https://oeis.org/A12
    Parades_TablDiag1     -> https://oeis.org/A12
    Parades_PolyRow2      -> https://oeis.org/A27
    Parades_RevPolyRow2   -> https://oeis.org/A27
    Parades_PolyRow3      -> https://oeis.org/A2378
    Parades_RevPolyRow3   -> https://oeis.org/A2378
    Parades_TablCol3      -> https://oeis.org/A6230
    Parades_TablDiag3     -> https://oeis.org/A6230
    Parades_TablCol2      -> https://oeis.org/A36563
    Parades_TablDiag2     -> https://oeis.org/A36563
    Parades_AltSum        -> https://oeis.org/A36968
    Parades_CentralE      -> https://oeis.org/A48144
    Parades_BinConv       -> https://oeis.org/A52841
    Parades_InvBinConv    -> https://oeis.org/A210657
    Parades_TablMax       -> https://oeis.org/A272645
    Parades_ColMiddle     -> https://oeis.org/A272645
    Parades_RevColMiddle  -> https://oeis.org/A272645
    Parades_TablSum       -> https://oeis.org/A297195
    Parades_AbsSum        -> https://oeis.org/A297195
    Parades_Triangle      -> https://oeis.org/A371761
    Parades_Trev          -> https://oeis.org/A371761
    Parades_Talt          -> https://oeis.org/A371761
    Parades_RevTalt       -> https://oeis.org/A371761

    Parades: Distinct: 15, Hits: 27, Misses: 38
'''
