from functools import cache
from _tabltypes import Table
from Binomial import binomial

"""Lozanic numbers.


[0]  1;
[1]  1,  1;
[2]  1,  1,  1;
[3]  1,  2,  2,  1;
[4]  1,  2,  4,  2,  1;
[5]  1,  3,  6,  6,  3,  1;
[6]  1,  3,  9, 10,  9,  3,  1;
[7]  1,  4, 12, 19, 19, 12,  4,  1;
[8]  1,  4, 16, 28, 38, 28, 16,  4,  1;
[9]  1,  5, 20, 44, 66, 66, 44, 20,  5,  1;
"""


@cache
def lozanic(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1] + lozanic(n - 1)
    for k in range(1, n):
        row[k] += row[k + 1]

    if n % 2 != 0:
        return row

    b = binomial(n // 2 - 1)
    for k in range(1, n, 2):
        row[k] -= b[(k - 1) // 2]

    return row


Lozanic = Table(
    lozanic,
    "Lozanic",
    ["A034851"],
    "A000000",
    r"\frac{1}{2} \left(\binom{n}{k}+\binom{n \text{ mod } 2}{k \text{ mod } 2} \binom{n \text{ div } 2}{k \text{ div } 2} \right)",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Lozanic)




''' OEIS
    Lozanic_NegHalf       -> https://oeis.org/A-999999
    Lozanic_RevNegHalf    -> https://oeis.org/A-999999
    Lozanic_Trevinv       -> 0 
    Lozanic_Toff11        -> 0 
    Lozanic_Trev11        -> 0 
    Lozanic_Tinv11        -> 0 
    Lozanic_Trevinv11     -> 0 
    Lozanic_Tacc          -> 0 
    Lozanic_Tder          -> 0 
    Lozanic_TablLcm       -> 0 
    Lozanic_TablGcd       -> 0 
    Lozanic_AccSum        -> 0 
    Lozanic_AccRevSum     -> 0 
    Lozanic_PosHalf       -> 0 
    Lozanic_TransNat0     -> 0 
    Lozanic_TransNat1     -> 0 
    Lozanic_TransSqrs     -> 0 
    Lozanic_BinConv       -> 0 
    Lozanic_InvBinConv    -> 0 
    Lozanic_PolyCol2      -> 0 
    Lozanic_PolyCol3      -> 0 
    Lozanic_PolyDiag      -> 0 
    Lozanic_RevToff11     -> 0 
    Lozanic_RevTrev11     -> 0 
    Lozanic_RevTinv11     -> 0 
    Lozanic_RevTacc       -> 0 
    Lozanic_RevTder       -> 0 
    Lozanic_RevAccRevSum  -> 0 
    Lozanic_RevPosHalf    -> 0 
    Lozanic_RevTransNat0  -> 0 
    Lozanic_RevTransNat1  -> 0 
    Lozanic_RevTransSqrs  -> 0 
    Lozanic_RevPolyCol3   -> 0 
    Lozanic_RevPolyDiag   -> 0 
    Lozanic_TablCol0      -> https://oeis.org/A12
    Lozanic_TablDiag0     -> https://oeis.org/A12
    Lozanic_PolyRow1      -> https://oeis.org/A27
    Lozanic_RevPolyRow1   -> https://oeis.org/A27
    Lozanic_AntiDSum      -> https://oeis.org/A1224
    Lozanic_RevAntiDSum   -> https://oeis.org/A1224
    Lozanic_PolyRow2      -> https://oeis.org/A2061
    Lozanic_RevPolyRow2   -> https://oeis.org/A2061
    Lozanic_TablCol2      -> https://oeis.org/A2620
    Lozanic_TablDiag2     -> https://oeis.org/A2620
    Lozanic_TablCol1      -> https://oeis.org/A4526
    Lozanic_TablDiag1     -> https://oeis.org/A4526
    Lozanic_TablSum       -> https://oeis.org/A5418
    Lozanic_EvenSum       -> https://oeis.org/A5418
    Lozanic_AbsSum        -> https://oeis.org/A5418
    Lozanic_RevEvenSum    -> https://oeis.org/A5418
    Lozanic_CentralO      -> https://oeis.org/A5654
    Lozanic_RevCentralO   -> https://oeis.org/A5654
    Lozanic_TablCol3      -> https://oeis.org/A5993
    Lozanic_TablDiag3     -> https://oeis.org/A5993
    Lozanic_CentralE      -> https://oeis.org/A32123
    Lozanic_Triangle      -> https://oeis.org/A34851
    Lozanic_Trev          -> https://oeis.org/A34851
    Lozanic_Talt          -> https://oeis.org/A34851
    Lozanic_RevTalt       -> https://oeis.org/A34851
    Lozanic_TablMax       -> https://oeis.org/A34872
    Lozanic_ColMiddle     -> https://oeis.org/A34872
    Lozanic_RevColMiddle  -> https://oeis.org/A34872
    Lozanic_OddSum        -> https://oeis.org/A51437
    Lozanic_RevOddSum     -> https://oeis.org/A51437
    Lozanic_Tinv          -> https://oeis.org/A55138
    Lozanic_Tinvrev       -> https://oeis.org/A55138
    Lozanic_PolyRow3      -> https://oeis.org/A69778
    Lozanic_RevPolyRow3   -> https://oeis.org/A69778
    Lozanic_AltSum        -> https://oeis.org/A77957
    Lozanic_Tantidiag     -> https://oeis.org/A102541
    Lozanic_RevTantidiag  -> https://oeis.org/A102541

    Lozanic: Distinct: 19, Hits: 39, Misses: 32
'''
