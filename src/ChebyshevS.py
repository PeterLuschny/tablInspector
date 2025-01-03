from functools import cache
from _tabltypes import Table

"""Coefficients of Chebyshev S(n, x) = U(n, x/2) polynomials.

[0]  1;
[1]  0,  1;
[2] -1,  0,   1;
[3]  0, -2,   0,   1;
[4]  1,  0,  -3,   0,  1;
[5]  0,  3,   0,  -4,  0,  1;
[6] -1,  0,   6,   0, -5,  0,  1;
[7]  0, -4,   0,  10,  0, -6,  0,   1;
[8]  1,  0, -10,   0, 15,  0, -7,   0, 1;
[9]  0,  5,   0, -20,  0,  21,  0, -8, 0, 1;
"""


@cache
def chebyshevs(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    rov = chebyshevs(n - 2)
    row = [0] + chebyshevs(n - 1)
    for k in range(0, n - 1):
        row[k] -= rov[k]
    return row


ChebyshevS = Table(
    chebyshevs,
    "ChebyshevS",
    ["A049310", "A053119", "A112552", "A168561"],
    "A053121",  # this is the Catalan Paths triangle
    r"\binom{(n+k)/2}{k} text{A369736}(n, k)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(ChebyshevS)


''' OEIS
    ChebyshevS_Trev11        -> 0 
    ChebyshevS_Tantidiag     -> 0 
    ChebyshevS_Tacc          -> 0 
    ChebyshevS_TablGcd       -> 0 
    ChebyshevS_AccSum        -> 0 
    ChebyshevS_AccRevSum     -> 0 
    ChebyshevS_ColMiddle     -> 0 
    ChebyshevS_TransNat1     -> 0 
    ChebyshevS_TransSqrs     -> 0 
    ChebyshevS_RevToff11     -> 0 
    ChebyshevS_RevTrev11     -> 0 
    ChebyshevS_RevTacc       -> 0 
    ChebyshevS_RevTder       -> 0 
    ChebyshevS_RevAccRevSum  -> 0 
    ChebyshevS_RevColMiddle  -> 0 
    ChebyshevS_RevTransNat0  -> 0 
    ChebyshevS_RevTransNat1  -> 0 
    ChebyshevS_RevTransSqrs  -> 0 
    ChebyshevS_RevPolyDiag   -> 0 
    ChebyshevS_TablDiag1     -> https://oeis.org/A7
    ChebyshevS_TablDiag3     -> https://oeis.org/A7
    ChebyshevS_AntiDSum      -> https://oeis.org/A7
    ChebyshevS_RevOddSum     -> https://oeis.org/A7
    ChebyshevS_TablDiag0     -> https://oeis.org/A12
    ChebyshevS_RevPolyRow1   -> https://oeis.org/A12
    ChebyshevS_TablDiag2     -> https://oeis.org/A27
    ChebyshevS_PolyRow1      -> https://oeis.org/A27
    ChebyshevS_PolyCol2      -> https://oeis.org/A27
    ChebyshevS_RevNegHalf    -> https://oeis.org/A27
    ChebyshevS_TablCol0      -> https://oeis.org/A35
    ChebyshevS_AbsSum        -> https://oeis.org/A45
    ChebyshevS_TablCol2      -> https://oeis.org/A217
    ChebyshevS_TablCol3      -> https://oeis.org/A292
    ChebyshevS_PolyCol3      -> https://oeis.org/A1906
    ChebyshevS_PolyRow2      -> https://oeis.org/A5563
    ChebyshevS_RevPolyRow2   -> https://oeis.org/A5563
    ChebyshevS_CentralE      -> https://oeis.org/A5809
    ChebyshevS_TablSum       -> https://oeis.org/A11655
    ChebyshevS_AltSum        -> https://oeis.org/A11655
    ChebyshevS_RevEvenSum    -> https://oeis.org/A11655
    ChebyshevS_TablLcm       -> https://oeis.org/A25560
    ChebyshevS_RevCentralO   -> https://oeis.org/A45721
    ChebyshevS_Tinv          -> https://oeis.org/A53121
    ChebyshevS_RevPolyRow3   -> https://oeis.org/A56220
    ChebyshevS_TablMax       -> https://oeis.org/A73028
    ChebyshevS_PolyDiag      -> https://oeis.org/A97690
    ChebyshevS_RevAntiDSum   -> https://oeis.org/A99530
    ChebyshevS_PosHalf       -> https://oeis.org/A106853
    ChebyshevS_NegHalf       -> https://oeis.org/A106853
    ChebyshevS_Toff11        -> https://oeis.org/A112552
    ChebyshevS_Tinv11        -> https://oeis.org/A112554
    ChebyshevS_TablCol1      -> https://oeis.org/A142150
    ChebyshevS_RevPolyCol3   -> https://oeis.org/A146078
    ChebyshevS_Trev          -> https://oeis.org/A162515
    ChebyshevS_RevTalt       -> https://oeis.org/A162515
    ChebyshevS_CentralO      -> https://oeis.org/A165817
    ChebyshevS_Triangle      -> https://oeis.org/A168561
    ChebyshevS_Talt          -> https://oeis.org/A168561
    ChebyshevS_RevTantidiag  -> https://oeis.org/A180184
    ChebyshevS_TransNat0     -> https://oeis.org/A186731
    ChebyshevS_PolyRow3      -> https://oeis.org/A242135
    ChebyshevS_EvenSum       -> https://oeis.org/A257000
    ChebyshevS_OddSum        -> https://oeis.org/A257000
    ChebyshevS_BinConv       -> https://oeis.org/A278415
    ChebyshevS_InvBinConv    -> https://oeis.org/A278415
    ChebyshevS_Tder          -> https://oeis.org/A294519

    ChebyshevS: Distinct: 33, Hits: 47, Misses: 19
'''
