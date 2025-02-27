from functools import cache
from _tabltypes import Table

"""
T(n,k) = binomial(n, k) * Catalan(n - k).
       = CatalanNumber(k) * Pochhammer(-n, k) / k!

[0] 1;
[1] 1, 1;
[2] 1, 2,  2;
[3] 1, 3,  6,   5;
[4] 1, 4, 12,  20,  14;
[5] 1, 5, 20,  50,  70,  42;
[6] 1, 6, 30, 100, 210, 252, 132;
[7] 1, 7, 42, 175, 490, 882, 924, 429;
"""


@cache
def binomialcatalan(n: int) -> list[int]:
    if n == 0:
        return [1]

    a = binomialcatalan(n - 1) + [0]
    row = [0] * (n + 1)
    row[0] = 1
    row[1] = n
    for k in range(2, n + 1):
        row[k] = (a[k] * (n + k + 1) + a[k - 1] * (4 * k - 2)) // (n + 1)

    return row


BinomialCatalan = Table(
    binomialcatalan,
    "BinomialCatalan",
    ["A124644", "A098474"],
    "",  # not invertible
    r"\binom{n}{k} \text{Catalan}(n - k)",
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(BinomialCatalan)






''' OEIS
    BinomialCatalan_Tinvrev       -> 0 
    BinomialCatalan_Toff11        -> 0 
    BinomialCatalan_Trev11        -> 0 
    BinomialCatalan_Tantidiag     -> 0 
    BinomialCatalan_Tacc          -> 0 
    BinomialCatalan_Tder          -> 0 
    BinomialCatalan_TablDiag3     -> 0 
    BinomialCatalan_TablLcm       -> 0 
    BinomialCatalan_TablMax       -> 0 
    BinomialCatalan_OddSum        -> 0 
    BinomialCatalan_AccSum        -> 0 
    BinomialCatalan_ColMiddle     -> 0 
    BinomialCatalan_TransSqrs     -> 0 
    BinomialCatalan_InvBinConv    -> 0 
    BinomialCatalan_PolyRow3      -> 0 
    BinomialCatalan_RevToff11     -> 0 
    BinomialCatalan_RevTrev11     -> 0 
    BinomialCatalan_RevTinv11     -> 0 
    BinomialCatalan_RevTantidiag  -> 0 
    BinomialCatalan_RevTacc       -> 0 
    BinomialCatalan_RevTder       -> 0 
    BinomialCatalan_RevOddSum     -> 0 
    BinomialCatalan_RevAccRevSum  -> 0 
    BinomialCatalan_RevColMiddle  -> 0 
    BinomialCatalan_RevTransNat0  -> 0 
    BinomialCatalan_RevTransNat1  -> 0 
    BinomialCatalan_RevTransSqrs  -> 0 
    BinomialCatalan_TablCol0      -> https://oeis.org/A12
    BinomialCatalan_TablCol1      -> https://oeis.org/A27
    BinomialCatalan_PolyRow1      -> https://oeis.org/A27
    BinomialCatalan_RevPolyRow1   -> https://oeis.org/A27
    BinomialCatalan_TablGcd       -> https://oeis.org/A34
    BinomialCatalan_TablDiag0     -> https://oeis.org/A108
    BinomialCatalan_CentralE      -> https://oeis.org/A888
    BinomialCatalan_CentralO      -> https://oeis.org/A891
    BinomialCatalan_TablDiag1     -> https://oeis.org/A984
    BinomialCatalan_NegHalf       -> https://oeis.org/A1405
    BinomialCatalan_PolyRow2      -> https://oeis.org/A1844
    BinomialCatalan_TablCol2      -> https://oeis.org/A2378
    BinomialCatalan_RevPolyRow2   -> https://oeis.org/A2522
    BinomialCatalan_AltSum        -> https://oeis.org/A5043
    BinomialCatalan_RevPolyRow3   -> https://oeis.org/A5491
    BinomialCatalan_TablSum       -> https://oeis.org/A7317
    BinomialCatalan_AbsSum        -> https://oeis.org/A7317
    BinomialCatalan_AccRevSum     -> https://oeis.org/A26375
    BinomialCatalan_TransNat1     -> https://oeis.org/A26375
    BinomialCatalan_TransNat0     -> https://oeis.org/A26376
    BinomialCatalan_PosHalf       -> https://oeis.org/A64613
    BinomialCatalan_BinConv       -> https://oeis.org/A86618
    BinomialCatalan_AntiDSum      -> https://oeis.org/A90344
    BinomialCatalan_TablDiag2     -> https://oeis.org/A92443
    BinomialCatalan_EvenSum       -> https://oeis.org/A98465
    BinomialCatalan_Triangle      -> https://oeis.org/A98474
    BinomialCatalan_Talt          -> https://oeis.org/A98474
    BinomialCatalan_RevEvenSum    -> https://oeis.org/A102318
    BinomialCatalan_RevPolyCol3   -> https://oeis.org/A104455
    BinomialCatalan_RevAntiDSum   -> https://oeis.org/A105864
    BinomialCatalan_Trev          -> https://oeis.org/A124644
    BinomialCatalan_RevTalt       -> https://oeis.org/A124644
    BinomialCatalan_RevCentralO   -> https://oeis.org/A125558
    BinomialCatalan_TablCol3      -> https://oeis.org/A134481
    BinomialCatalan_PolyCol2      -> https://oeis.org/A162326
    BinomialCatalan_RevPosHalf    -> https://oeis.org/A162326
    BinomialCatalan_RevPolyDiag   -> https://oeis.org/A292632
    BinomialCatalan_PolyCol3      -> https://oeis.org/A337167
    BinomialCatalan_RevNegHalf    -> https://oeis.org/A337168
    BinomialCatalan_PolyDiag      -> https://oeis.org/A338979

    BinomialCatalan: Distinct: 34, Hits: 40, Misses: 27
'''
