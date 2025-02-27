from functools import cache
from _tabltypes import Table

"""(Physicist's) Hermite polynomials, unsigned coefficients.

[0]     1;
[1]     0,     2;
[2]     2,     0,      4;
[3]     0,    12,      0,      8;
[4]    12,     0,     48,      0,     16;
[5]     0,   120,      0,    160,      0,    32;
[6]   120,     0,    720,      0,    480,     0,     64;
[7]     0,  1680,      0,   3360,      0,  1344,      0,   128;
[8]  1680,     0,  13440,      0,  13440,     0,   3584,     0,   256;
[9]     0, 30240,      0,  80640,      0, 48384,      0,  9216,     0,  512;
"""


@cache
def hermiteh(n: int) -> list[int]:
    row = [0] * (n + 1)
    row[n] = 2**n
    for k in range(n - 2, -1, -2):
        row[k] = (row[k + 2] * (k + 2) * (k + 1)) // (2 * (n - k))
    return row


HermiteH = Table(
    hermiteh,
    "HermiteH",
    ["A060821"],
    "",
    r"is(n - k odd)\, ? \, 0 : (-1)^{(n-k)/2} \ \frac{n!}{k!} \ \frac{2^k}{((n-k)/2)!}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(HermiteH)






''' OEIS
    HermiteH_Trev          -> 0 
    HermiteH_Toff11        -> 0 
    HermiteH_Trev11        -> 0 
    HermiteH_Tantidiag     -> 0 
    HermiteH_Tacc          -> 0 
    HermiteH_Tder          -> 0 
    HermiteH_TablCol2      -> 0 
    HermiteH_TablCol3      -> 0 
    HermiteH_TablLcm       -> 0 
    HermiteH_EvenSum       -> 0 
    HermiteH_OddSum        -> 0 
    HermiteH_AccSum        -> 0 
    HermiteH_AccRevSum     -> 0 
    HermiteH_AntiDSum      -> 0 
    HermiteH_ColMiddle     -> 0 
    HermiteH_CentralE      -> 0 
    HermiteH_CentralO      -> 0 
    HermiteH_PosHalf       -> 0 
    HermiteH_NegHalf       -> 0 
    HermiteH_TransNat0     -> 0 
    HermiteH_TransNat1     -> 0 
    HermiteH_TransSqrs     -> 0 
    HermiteH_BinConv       -> 0 
    HermiteH_InvBinConv    -> 0 
    HermiteH_PolyRow3      -> 0 
    HermiteH_PolyDiag      -> 0 
    HermiteH_RevToff11     -> 0 
    HermiteH_RevTrev11     -> 0 
    HermiteH_RevTantidiag  -> 0 
    HermiteH_RevTacc       -> 0 
    HermiteH_RevTalt       -> 0 
    HermiteH_RevTder       -> 0 
    HermiteH_RevAccRevSum  -> 0 
    HermiteH_RevAntiDSum   -> 0 
    HermiteH_RevColMiddle  -> 0 
    HermiteH_RevCentralO   -> 0 
    HermiteH_RevTransNat0  -> 0 
    HermiteH_RevTransNat1  -> 0 
    HermiteH_RevTransSqrs  -> 0 
    HermiteH_RevPolyRow3   -> 0 
    HermiteH_RevPolyCol3   -> 0 
    HermiteH_RevPolyDiag   -> 0 
    HermiteH_TablDiag1     -> https://oeis.org/A4
    HermiteH_TablDiag3     -> https://oeis.org/A4
    HermiteH_RevOddSum     -> https://oeis.org/A4
    HermiteH_TablDiag0     -> https://oeis.org/A79
    HermiteH_TablSum       -> https://oeis.org/A898
    HermiteH_AltSum        -> https://oeis.org/A898
    HermiteH_AbsSum        -> https://oeis.org/A898
    HermiteH_RevEvenSum    -> https://oeis.org/A898
    HermiteH_TablDiag2     -> https://oeis.org/A1815
    HermiteH_PolyRow1      -> https://oeis.org/A5843
    HermiteH_PolyRow2      -> https://oeis.org/A5899
    HermiteH_TablGcd       -> https://oeis.org/A16116
    HermiteH_RevPolyRow1   -> https://oeis.org/A55642
    HermiteH_Triangle      -> https://oeis.org/A60821
    HermiteH_Talt          -> https://oeis.org/A60821
    HermiteH_TablCol0      -> https://oeis.org/A67994
    HermiteH_TablCol1      -> https://oeis.org/A67994
    HermiteH_PolyCol3      -> https://oeis.org/A79949
    HermiteH_PolyCol2      -> https://oeis.org/A127394
    HermiteH_RevPosHalf    -> https://oeis.org/A127394
    HermiteH_RevNegHalf    -> https://oeis.org/A127394
    HermiteH_RevPolyRow2   -> https://oeis.org/A255843
    HermiteH_TablMax       -> https://oeis.org/A277281

    HermiteH: Distinct: 15, Hits: 23, Misses: 42
'''
