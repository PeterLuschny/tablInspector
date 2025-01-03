from functools import cache
from _tabltypes import Table

"""Pascal triangle, binomial coefficients.


[0]   1;
[1]   1,   1;
[2]   1,   2,   1;
[3]   1,   3,   3,   1;
[4]   1,   4,   6,   4,   1;
[5]   1,   5,  10,  10,   5,   1;
[6]   1,   6,  15,  20,  15,   6,   1;
[7]   1,   7,  21,  35,  35,  21,   7,   1;
[8]   1,   8,  28,  56,  70,  56,  28,   8,   1;
[9]   1,   9,  36,  84, 126, 126,  84,  36,   9,   1;


Inverse binomial triangle:

   1;
  -1,    1;
   1,   -2,    1;
  -1,    3,   -3,    1;
   1,   -4,    6,   -4,    1;
  -1,    5,  -10,   10,   -5,    1;
   1,   -6,   15,  -20,   15,   -6,    1;
  -1,    7,  -21,   35,  -35,   21,   -7,    1;
   1,   -8,   28,  -56,   70,  -56,   28,   -8,    1;
  -1,    9,  -36,   84, -126,  126,  -84,   36,   -9,    1;
  ...
"""


@cache
def binomial(n: int) -> list[int]:
    if n == 0:
        return [1]

    row: list[int] = [1] + binomial(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row


def invbinomial(n: int) -> list[int]:
    return [(-1)**(n - k) * binomial(n)[k] for k in range(n + 1)]


Binomial = Table(
    binomial,
    "Binomial",
    [
        "A007318", "A074909", "A108086", "A117440", 
        "A118433", "A130595", "A135278", "A154926",
    ],
    "A130595",
    r"n! \, / (k! \, (n - k)! )",
)

InvBinomial = Table(
    invbinomial,
    "InvBinomial",
    ["A130595"],
    "A000000",
    r"(-1)^{n-k} \, n! \, / (k! \, (n - k)! )",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Binomial)
    InspectTable(InvBinomial)


''' OEIS
    Binomial_AltSum        -> https://oeis.org/A7
    Binomial_TablCol0      -> https://oeis.org/A12
    Binomial_TablDiag0     -> https://oeis.org/A12
    Binomial_NegHalf       -> https://oeis.org/A12
    Binomial_RevNegHalf    -> https://oeis.org/A12
    Binomial_TablCol1      -> https://oeis.org/A27
    Binomial_TablDiag1     -> https://oeis.org/A27
    Binomial_PolyRow1      -> https://oeis.org/A27
    Binomial_RevPolyRow1   -> https://oeis.org/A27
    Binomial_AntiDSum      -> https://oeis.org/A45
    Binomial_RevAntiDSum   -> https://oeis.org/A45
    Binomial_TablSum       -> https://oeis.org/A79
    Binomial_EvenSum       -> https://oeis.org/A79
    Binomial_OddSum        -> https://oeis.org/A79
    Binomial_AbsSum        -> https://oeis.org/A79
    Binomial_RevEvenSum    -> https://oeis.org/A79
    Binomial_RevOddSum     -> https://oeis.org/A79
    Binomial_PolyDiag      -> https://oeis.org/A169
    Binomial_RevPolyDiag   -> https://oeis.org/A169
    Binomial_TablCol2      -> https://oeis.org/A217
    Binomial_TablDiag2     -> https://oeis.org/A217
    Binomial_PosHalf       -> https://oeis.org/A244
    Binomial_PolyCol2      -> https://oeis.org/A244
    Binomial_PolyRow2      -> https://oeis.org/A290
    Binomial_RevPolyRow2   -> https://oeis.org/A290
    Binomial_TablCol3      -> https://oeis.org/A292
    Binomial_TablDiag3     -> https://oeis.org/A292
    Binomial_PolyCol3      -> https://oeis.org/A302
    Binomial_RevPolyCol3   -> https://oeis.org/A302
    Binomial_PolyRow3      -> https://oeis.org/A578
    Binomial_RevPolyRow3   -> https://oeis.org/A578
    Binomial_CentralE      -> https://oeis.org/A984
    Binomial_BinConv       -> https://oeis.org/A984
    Binomial_TablMax       -> https://oeis.org/A1405
    Binomial_ColMiddle     -> https://oeis.org/A1405
    Binomial_RevColMiddle  -> https://oeis.org/A1405
    Binomial_CentralO      -> https://oeis.org/A1700
    Binomial_RevCentralO   -> https://oeis.org/A1700
    Binomial_TransNat0     -> https://oeis.org/A1787
    Binomial_RevTransNat0  -> https://oeis.org/A1787
    Binomial_TransSqrs     -> https://oeis.org/A1788
    Binomial_RevTransSqrs  -> https://oeis.org/A1788
    Binomial_AccSum        -> https://oeis.org/A1792
    Binomial_AccRevSum     -> https://oeis.org/A1792
    Binomial_TransNat1     -> https://oeis.org/A1792
    Binomial_RevAccRevSum  -> https://oeis.org/A1792
    Binomial_RevTransNat1  -> https://oeis.org/A1792
    Binomial_TablLcm       -> https://oeis.org/A2944
    Binomial_Tder          -> https://oeis.org/A3506
    Binomial_RevTder       -> https://oeis.org/A3506
    Binomial_Triangle      -> https://oeis.org/A7318
    Binomial_Tinv          -> https://oeis.org/A7318
    Binomial_Trev          -> https://oeis.org/A7318
    Binomial_Tinvrev       -> https://oeis.org/A7318
    Binomial_Talt          -> https://oeis.org/A7318
    Binomial_RevTalt       -> https://oeis.org/A7318
    Binomial_Tacc          -> https://oeis.org/A8949
    Binomial_RevTacc       -> https://oeis.org/A8949
    Binomial_Tantidiag     -> https://oeis.org/A11973
    Binomial_RevTantidiag  -> https://oeis.org/A11973
    Binomial_TablGcd       -> https://oeis.org/A14963
    Binomial_Toff11        -> https://oeis.org/A74909
    Binomial_Trev11        -> https://oeis.org/A74909
    Binomial_Tinv11        -> https://oeis.org/A74909
    Binomial_RevToff11     -> https://oeis.org/A74909
    Binomial_RevTrev11     -> https://oeis.org/A74909
    Binomial_RevTinv11     -> https://oeis.org/A74909
    Binomial_InvBinConv    -> https://oeis.org/A126869

    Binomial: Distinct: 26, Hits: 68, Misses: 0
'''
