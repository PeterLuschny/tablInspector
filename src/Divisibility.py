from functools import cache
from _tabltypes import Table

"""
The divisibility matrix, the indicator function for divisibility. The Matrix inverse of the Moebius Matrix.

[ 0]  1
[ 1]  0  1
[ 2]  0  1  1
[ 3]  0  1  0  1
[ 4]  0  1  1  0  1
[ 5]  0  1  0  0  0  1
[ 6]  0  1  1  1  0  0  1
[ 7]  0  1  0  0  0  0  0  1
[ 8]  0  1  1  0  1  0  0  0  1
[ 9]  0  1  0  1  0  0  0  0  0  1
[10]  0  1  1  0  0  1  0  0  0  0  1
"""


@cache
def divisibility(n: int) -> list[int]:
    if n == 0:
        return [1]
    L = [0 for _ in range(n + 1)]
    L[1] = L[n] = 1
    i = 1
    div = n

    while i < div:
        div, mod = divmod(n, i)
        if mod == 0:
            L[i] = L[div] = 1
        i += 1
    return L


Divisibility = Table(
    divisibility,
    "Divisibility",
    ["A113704", "A051731"],
    "A000000",
    r"[n=0 \text{ or } k \text{ divides } n]",
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Divisibility)




''' OEIS
    Divisibility_Trev          -> 0 
    Divisibility_Tantidiag     -> 0 
    Divisibility_Tacc          -> 0 
    Divisibility_NegHalf       -> 0 
    Divisibility_InvBinConv    -> 0 
    Divisibility_RevToff11     -> 0 
    Divisibility_RevTantidiag  -> 0 
    Divisibility_RevTacc       -> 0 
    Divisibility_RevTalt       -> 0 
    Divisibility_RevTder       -> 0 
    Divisibility_RevNegHalf    -> 0 
    Divisibility_RevPolyDiag   -> 0 
    Divisibility_TablSum       -> https://oeis.org/A5
    Divisibility_AbsSum        -> https://oeis.org/A5
    Divisibility_TablCol0      -> https://oeis.org/A7
    Divisibility_TablDiag3     -> https://oeis.org/A7
    Divisibility_RevCentralO   -> https://oeis.org/A7
    Divisibility_Trevinv       -> https://oeis.org/A12
    Divisibility_Tinvrev11     -> https://oeis.org/A12
    Divisibility_Trevinv11     -> https://oeis.org/A12
    Divisibility_TablCol1      -> https://oeis.org/A12
    Divisibility_TablDiag0     -> https://oeis.org/A12
    Divisibility_TablLcm       -> https://oeis.org/A12
    Divisibility_TablGcd       -> https://oeis.org/A12
    Divisibility_TablMax       -> https://oeis.org/A12
    Divisibility_CentralE      -> https://oeis.org/A12
    Divisibility_RevPolyRow1   -> https://oeis.org/A12
    Divisibility_PolyRow1      -> https://oeis.org/A27
    Divisibility_RevPolyRow2   -> https://oeis.org/A27
    Divisibility_TablCol2      -> https://oeis.org/A35
    Divisibility_RevColMiddle  -> https://oeis.org/A35
    Divisibility_TransNat0     -> https://oeis.org/A203
    Divisibility_TransSqrs     -> https://oeis.org/A1157
    Divisibility_OddSum        -> https://oeis.org/A1227
    Divisibility_RevOddSum     -> https://oeis.org/A1227
    Divisibility_RevAntiDSum   -> https://oeis.org/A1227
    Divisibility_PolyRow2      -> https://oeis.org/A2378
    Divisibility_RevPolyRow3   -> https://oeis.org/A2522
    Divisibility_AccRevSum     -> https://oeis.org/A7503
    Divisibility_TransNat1     -> https://oeis.org/A7503
    Divisibility_AntiDSum      -> https://oeis.org/A32741
    Divisibility_PolyRow3      -> https://oeis.org/A34262
    Divisibility_Toff11        -> https://oeis.org/A51731
    Divisibility_PolyCol2      -> https://oeis.org/A55895
    Divisibility_RevPosHalf    -> https://oeis.org/A55895
    Divisibility_BinConv       -> https://oeis.org/A56045
    Divisibility_PolyDiag      -> https://oeis.org/A66108
    Divisibility_PosHalf       -> https://oeis.org/A74854
    Divisibility_TablCol3      -> https://oeis.org/A79978
    Divisibility_AccSum        -> https://oeis.org/A81307
    Divisibility_RevAccRevSum  -> https://oeis.org/A81307
    Divisibility_RevTransNat1  -> https://oeis.org/A81307
    Divisibility_RevTransNat0  -> https://oeis.org/A94471
    Divisibility_AltSum        -> https://oeis.org/A112329
    Divisibility_Triangle      -> https://oeis.org/A113704
    Divisibility_Talt          -> https://oeis.org/A113704
    Divisibility_Trev11        -> https://oeis.org/A113998
    Divisibility_Tder          -> https://oeis.org/A127093
    Divisibility_ColMiddle     -> https://oeis.org/A128174
    Divisibility_Tinv11        -> https://oeis.org/A174852
    Divisibility_RevTrev11     -> https://oeis.org/A175992
    Divisibility_EvenSum       -> https://oeis.org/A183063
    Divisibility_TablDiag1     -> https://oeis.org/A209229
    Divisibility_CentralO      -> https://oeis.org/A209229
    Divisibility_TablDiag2     -> https://oeis.org/A279329
    Divisibility_RevEvenSum    -> https://oeis.org/A320111
    Divisibility_RevPolyCol3   -> https://oeis.org/A357051
    Divisibility_PolyCol3      -> https://oeis.org/A363913
    Divisibility_Tinv          -> https://oeis.org/A363914
    Divisibility_RevTransSqrs  -> https://oeis.org/A367326

    Divisibility: Distinct: 37, Hits: 58, Misses: 12
'''
