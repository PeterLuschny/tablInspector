from functools import cache
from _tabltypes import Table

"""Coefficients of Chebyshev T(n, x) polynomials.

Not integer-invertible, but the rational inverse
times 2^n is the right wing of Pascal's triangle.

[0]   1;
[1]   0,  1;
[2]  -1,  0,   2;
[3]   0, -3,   0,    4;
[4]   1,  0,  -8,    0,    8;
[5]   0,  5,   0,  -20,    0,    16;
[6]  -1,  0,  18,    0,  -48,     0,    32;
[7]   0, -7,   0,   56,    0,  -112,     0,   64;
[8]   1,  0, -32,    0,  160,     0,  -256,    0,  128;
[9]   0,  9,   0, -120,    0,   432,     0, -576,    0,  256;
"""


@cache
def chebyshevt(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    rov = chebyshevt(n - 2)
    row = [0] + chebyshevt(n - 1)
    row[n] = 2 * row[n]
    for k in range(0, n - 1):
        row[k] = 2 * row[k] - rov[k]
    return row


ChebyshevT = Table(
    chebyshevt, 
    "ChebyshevT", 
    ["A053120", "A039991", "A081265"], 
    "",  # not invertible
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(ChebyshevT)




''' OEIS
    ChebyshevT_TablCol0      -> https://oeis.org/A-999999
    ChebyshevT_TablDiag1     -> https://oeis.org/A-999999
    ChebyshevT_TablDiag3     -> https://oeis.org/A-999999
    ChebyshevT_AltSum        -> https://oeis.org/A-999999
    ChebyshevT_RevOddSum     -> https://oeis.org/A-999999
    ChebyshevT_Toff11        -> 0 
    ChebyshevT_Trev11        -> 0 
    ChebyshevT_Tantidiag     -> 0 
    ChebyshevT_Tacc          -> 0 
    ChebyshevT_TablLcm       -> 0 
    ChebyshevT_TablGcd       -> 0 
    ChebyshevT_TablMax       -> 0 
    ChebyshevT_ColMiddle     -> 0 
    ChebyshevT_CentralO      -> 0 
    ChebyshevT_BinConv       -> 0 
    ChebyshevT_InvBinConv    -> 0 
    ChebyshevT_RevToff11     -> 0 
    ChebyshevT_RevTrev11     -> 0 
    ChebyshevT_RevTantidiag  -> 0 
    ChebyshevT_RevTacc       -> 0 
    ChebyshevT_RevTder       -> 0 
    ChebyshevT_RevColMiddle  -> 0 
    ChebyshevT_RevCentralO   -> 0 
    ChebyshevT_RevTransSqrs  -> 0 
    ChebyshevT_RevPolyRow3   -> 0 
    ChebyshevT_RevPolyDiag   -> 0 
    ChebyshevT_AntiDSum      -> https://oeis.org/A7
    ChebyshevT_TablSum       -> https://oeis.org/A12
    ChebyshevT_RevEvenSum    -> https://oeis.org/A12
    ChebyshevT_RevPolyRow1   -> https://oeis.org/A12
    ChebyshevT_PolyRow1      -> https://oeis.org/A27
    ChebyshevT_EvenSum       -> https://oeis.org/A35
    ChebyshevT_OddSum        -> https://oeis.org/A35
    ChebyshevT_RevAntiDSum   -> https://oeis.org/A73
    ChebyshevT_TablDiag0     -> https://oeis.org/A79
    ChebyshevT_TransNat0     -> https://oeis.org/A290
    ChebyshevT_PolyCol2      -> https://oeis.org/A1075
    ChebyshevT_RevPosHalf    -> https://oeis.org/A1075
    ChebyshevT_RevNegHalf    -> https://oeis.org/A1075
    ChebyshevT_TablCol2      -> https://oeis.org/A1105
    ChebyshevT_AbsSum        -> https://oeis.org/A1333
    ChebyshevT_PolyCol3      -> https://oeis.org/A1541
    ChebyshevT_TablDiag2     -> https://oeis.org/A1792
    ChebyshevT_RevTransNat0  -> https://oeis.org/A2378
    ChebyshevT_TablCol3      -> https://oeis.org/A2492
    ChebyshevT_AccRevSum     -> https://oeis.org/A2522
    ChebyshevT_TransNat1     -> https://oeis.org/A2522
    ChebyshevT_RevPolyRow2   -> https://oeis.org/A8865
    ChebyshevT_TransSqrs     -> https://oeis.org/A14820
    ChebyshevT_RevPolyCol3   -> https://oeis.org/A25172
    ChebyshevT_AccSum        -> https://oeis.org/A28387
    ChebyshevT_RevAccRevSum  -> https://oeis.org/A28387
    ChebyshevT_RevTransNat1  -> https://oeis.org/A28387
    ChebyshevT_CentralE      -> https://oeis.org/A36909
    ChebyshevT_Triangle      -> https://oeis.org/A53120
    ChebyshevT_Talt          -> https://oeis.org/A53120
    ChebyshevT_PolyRow2      -> https://oeis.org/A56220
    ChebyshevT_Trev          -> https://oeis.org/A81265
    ChebyshevT_RevTalt       -> https://oeis.org/A81265
    ChebyshevT_PolyDiag      -> https://oeis.org/A115066
    ChebyshevT_Tder          -> https://oeis.org/A136160
    ChebyshevT_PosHalf       -> https://oeis.org/A138230
    ChebyshevT_NegHalf       -> https://oeis.org/A138230
    ChebyshevT_PolyRow3      -> https://oeis.org/A144129
    ChebyshevT_TablCol1      -> https://oeis.org/A193356

    ChebyshevT: Distinct: 30, Hits: 44, Misses: 21
'''
