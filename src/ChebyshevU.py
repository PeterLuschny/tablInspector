from functools import cache
from _tabltypes import Table

"""Coefficients of Chebyshev U(n, x) polynomials.


[0]  1;
[1]  0,  2;
[2] -1,  0,   4;
[3]  0, -4,   0,    8;
[4]  1,  0, -12,    0,  16;
[5]  0,  6,   0,  -32,   0,   32;
[6] -1,  0,  24,    0, -80,    0,   64;
[7]  0, -8,   0,   80,   0, -192,    0,   128;
[8]  1,  0, -40,    0, 240,    0, -448,     0, 256;
[9]  0, 10,   0, -160,   0,  672,    0, -1024,   0,  512;
"""


@cache
def chebyshevu(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 2]

    rov = chebyshevu(n - 2)
    row = [0] + chebyshevu(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


ChebyshevU = Table(
    chebyshevu, 
    "ChebyshevU", 
    ["A053117", "A053118", "A115322"], 
    "",  # not integer-invertible
    r"2^k \binom{(n+k)/2}{k} \text{A369736}(n, k)"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(ChebyshevU)






''' OEIS
    ChebyshevU_Toff11        -> 0 
    ChebyshevU_Trev11        -> 0 
    ChebyshevU_Tantidiag     -> 0 
    ChebyshevU_Tacc          -> 0 
    ChebyshevU_Tder          -> 0 
    ChebyshevU_TablLcm       -> 0 
    ChebyshevU_TablGcd       -> 0 
    ChebyshevU_TablMax       -> 0 
    ChebyshevU_AccSum        -> 0 
    ChebyshevU_ColMiddle     -> 0 
    ChebyshevU_CentralO      -> 0 
    ChebyshevU_TransSqrs     -> 0 
    ChebyshevU_BinConv       -> 0 
    ChebyshevU_InvBinConv    -> 0 
    ChebyshevU_RevToff11     -> 0 
    ChebyshevU_RevTrev11     -> 0 
    ChebyshevU_RevTantidiag  -> 0 
    ChebyshevU_RevTacc       -> 0 
    ChebyshevU_RevTder       -> 0 
    ChebyshevU_RevAccRevSum  -> 0 
    ChebyshevU_RevColMiddle  -> 0 
    ChebyshevU_RevCentralO   -> 0 
    ChebyshevU_RevTransNat1  -> 0 
    ChebyshevU_RevTransSqrs  -> 0 
    ChebyshevU_RevPolyRow3   -> 0 
    ChebyshevU_RevPolyDiag   -> 0 
    ChebyshevU_TablDiag1     -> https://oeis.org/A4
    ChebyshevU_TablDiag3     -> https://oeis.org/A4
    ChebyshevU_RevOddSum     -> https://oeis.org/A4
    ChebyshevU_TablSum       -> https://oeis.org/A27
    ChebyshevU_AltSum        -> https://oeis.org/A27
    ChebyshevU_RevEvenSum    -> https://oeis.org/A27
    ChebyshevU_AntiDSum      -> https://oeis.org/A35
    ChebyshevU_TablDiag0     -> https://oeis.org/A79
    ChebyshevU_AbsSum        -> https://oeis.org/A129
    ChebyshevU_PolyRow2      -> https://oeis.org/A466
    ChebyshevU_PolyCol3      -> https://oeis.org/A1109
    ChebyshevU_PolyCol2      -> https://oeis.org/A1353
    ChebyshevU_RevPosHalf    -> https://oeis.org/A1353
    ChebyshevU_RevNegHalf    -> https://oeis.org/A1353
    ChebyshevU_TablDiag2     -> https://oeis.org/A1787
    ChebyshevU_PolyRow1      -> https://oeis.org/A5843
    ChebyshevU_AccRevSum     -> https://oeis.org/A6527
    ChebyshevU_TransNat1     -> https://oeis.org/A6527
    ChebyshevU_CentralE      -> https://oeis.org/A6588
    ChebyshevU_TransNat0     -> https://oeis.org/A7290
    ChebyshevU_RevTransNat0  -> https://oeis.org/A7290
    ChebyshevU_RevAntiDSum   -> https://oeis.org/A8937
    ChebyshevU_RevPolyCol3   -> https://oeis.org/A25170
    ChebyshevU_RevPolyRow2   -> https://oeis.org/A28347
    ChebyshevU_TablCol2      -> https://oeis.org/A46092
    ChebyshevU_Trev          -> https://oeis.org/A53118
    ChebyshevU_RevTalt       -> https://oeis.org/A53118
    ChebyshevU_RevPolyRow1   -> https://oeis.org/A55642
    ChebyshevU_TablCol0      -> https://oeis.org/A56594
    ChebyshevU_PosHalf       -> https://oeis.org/A88138
    ChebyshevU_NegHalf       -> https://oeis.org/A88138
    ChebyshevU_Triangle      -> https://oeis.org/A115322
    ChebyshevU_Talt          -> https://oeis.org/A115322
    ChebyshevU_TablCol3      -> https://oeis.org/A130809
    ChebyshevU_PolyRow3      -> https://oeis.org/A144138
    ChebyshevU_EvenSum       -> https://oeis.org/A193356
    ChebyshevU_TablCol1      -> https://oeis.org/A237420
    ChebyshevU_OddSum        -> https://oeis.org/A237420
    ChebyshevU_PolyDiag      -> https://oeis.org/A323118

    ChebyshevU: Distinct: 28, Hits: 39, Misses: 26
'''
