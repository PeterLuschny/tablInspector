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
"""


@cache
def pascal(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1] + pascal(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]
    return row


Pascal = Table(
    pascal,
    "Pascal",
    [
        "A007318",
        "A074909",
        "A108086",
        "A117440",
        "A118433",
        "A130595",
        "A135278",
        "A154926",
    ],
    "A000000",
    r"\binom{n}{k}",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Pascal)






''' OEIS
    Pascal_AltSum        -> https://oeis.org/A7
    Pascal_TablCol0      -> https://oeis.org/A12
    Pascal_TablDiag0     -> https://oeis.org/A12
    Pascal_TablCol1      -> https://oeis.org/A27
    Pascal_TablDiag1     -> https://oeis.org/A27
    Pascal_PolyRow1      -> https://oeis.org/A27
    Pascal_RevPolyRow1   -> https://oeis.org/A27
    Pascal_AntiDSum      -> https://oeis.org/A45
    Pascal_RevAntiDSum   -> https://oeis.org/A45
    Pascal_TablSum       -> https://oeis.org/A79
    Pascal_EvenSum       -> https://oeis.org/A79
    Pascal_OddSum        -> https://oeis.org/A79
    Pascal_AbsSum        -> https://oeis.org/A79
    Pascal_RevEvenSum    -> https://oeis.org/A79
    Pascal_RevOddSum     -> https://oeis.org/A79
    Pascal_PolyDiag      -> https://oeis.org/A169
    Pascal_RevPolyDiag   -> https://oeis.org/A169
    Pascal_TablCol2      -> https://oeis.org/A217
    Pascal_TablDiag2     -> https://oeis.org/A217
    Pascal_PosHalf       -> https://oeis.org/A244
    Pascal_PolyCol2      -> https://oeis.org/A244
    Pascal_RevPosHalf    -> https://oeis.org/A244
    Pascal_PolyRow2      -> https://oeis.org/A290
    Pascal_RevPolyRow2   -> https://oeis.org/A290
    Pascal_TablCol3      -> https://oeis.org/A292
    Pascal_TablDiag3     -> https://oeis.org/A292
    Pascal_PolyCol3      -> https://oeis.org/A302
    Pascal_RevPolyCol3   -> https://oeis.org/A302
    Pascal_PolyRow3      -> https://oeis.org/A578
    Pascal_RevPolyRow3   -> https://oeis.org/A578
    Pascal_CentralE      -> https://oeis.org/A984
    Pascal_BinConv       -> https://oeis.org/A984
    Pascal_TablMax       -> https://oeis.org/A1405
    Pascal_ColMiddle     -> https://oeis.org/A1405
    Pascal_RevColMiddle  -> https://oeis.org/A1405
    Pascal_CentralO      -> https://oeis.org/A1700
    Pascal_RevCentralO   -> https://oeis.org/A1700
    Pascal_TransNat0     -> https://oeis.org/A1787
    Pascal_RevTransNat0  -> https://oeis.org/A1787
    Pascal_TransSqrs     -> https://oeis.org/A1788
    Pascal_RevTransSqrs  -> https://oeis.org/A1788
    Pascal_AccSum        -> https://oeis.org/A1792
    Pascal_AccRevSum     -> https://oeis.org/A1792
    Pascal_TransNat1     -> https://oeis.org/A1792
    Pascal_RevAccRevSum  -> https://oeis.org/A1792
    Pascal_RevTransNat1  -> https://oeis.org/A1792
    Pascal_TablLcm       -> https://oeis.org/A2944
    Pascal_Tder          -> https://oeis.org/A3506
    Pascal_RevTder       -> https://oeis.org/A3506
    Pascal_Triangle      -> https://oeis.org/A7318
    Pascal_Tinv          -> https://oeis.org/A7318
    Pascal_Trev          -> https://oeis.org/A7318
    Pascal_Tinvrev       -> https://oeis.org/A7318
    Pascal_Trevinv       -> https://oeis.org/A7318
    Pascal_Talt          -> https://oeis.org/A7318
    Pascal_RevTalt       -> https://oeis.org/A7318
    Pascal_Tacc          -> https://oeis.org/A8949
    Pascal_RevTacc       -> https://oeis.org/A8949
    Pascal_Tantidiag     -> https://oeis.org/A11973
    Pascal_RevTantidiag  -> https://oeis.org/A11973
    Pascal_TablGcd       -> https://oeis.org/A14963
    Pascal_NegHalf       -> https://oeis.org/A33999
    Pascal_RevNegHalf    -> https://oeis.org/A33999
    Pascal_Toff11        -> https://oeis.org/A74909
    Pascal_Trev11        -> https://oeis.org/A74909
    Pascal_Tinv11        -> https://oeis.org/A74909
    Pascal_Trevinv11     -> https://oeis.org/A74909
    Pascal_RevToff11     -> https://oeis.org/A74909
    Pascal_RevTrev11     -> https://oeis.org/A74909
    Pascal_RevTinv11     -> https://oeis.org/A74909
    Pascal_InvBinConv    -> https://oeis.org/A126869

    Pascal: Distinct: 27, Hits: 71, Misses: 0
'''
