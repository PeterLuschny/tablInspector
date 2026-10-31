from functools import cache
from _tabltypes import Table

"""  A397333

  0:        1;
  1:        2,         1;
  2:        9,         7,         1;
  3:       64,        61,        15,       1;
  4:      625,       671,       217,      26,       1;
  5:     7776,      9031,      3465,     565,      40,     1;
  6:   117649,    144495,     62401,   12410,    1220,    57,    1;
  7:  2097152,   2685817,   1265607,  289821,   35350,  2324,   77,    1;
  8: 43046721,  56953279,  28702801, 7309722, 1041831, 85974, 4046,  100,  1;
"""

@cache
def a397333row(n: int) -> list[int]:
    if n == 0: return [1]
    row = [0]*(n + 1)
    row[n] = 1
    prev = a397333row(n - 1) + [0]
    for k in range(n - 1, -1, -1):
        row[k] = prev[k - 1] + (n + 2 * k + 1) * prev[k] + (n + k + 1) * (k + 1) * prev[k + 1] 
    return row


A397333 = Table(
    a397333row,     # the generating function
    "A397333",   # name of the table
    ["A397333"], # similar sequences in OEIS
    "?",         # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX form of the defining formula T(n, k)
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A397333)

''' OEIS
    A397333_Tinv -> 0
    A397333_Trev -> 0
    A397333_Trevinv -> 0
    A397333_Toff11 -> 0
    A397333_Trev11 -> 0
    A397333_Tinv11 -> 0
    A397333_Trevinv11 -> 0
    A397333_Tantidiag -> 0
    A397333_Tacc -> 0
    A397333_Tder -> 0
    A397333_TablCol2 -> 0
    A397333_TablCol3 -> 0
    A397333_TablDiag2 -> 0
    A397333_TablDiag3 -> 0
    A397333_TablLcm -> 0
    A397333_TablMax -> 0
    A397333_EvenSum -> 0
    A397333_OddSum -> 0
    A397333_AltSum -> 0
    A397333_AccSum -> 0
    A397333_AntiDSum -> 0
    A397333_ColMiddle -> 0
    A397333_CentralE -> 0
    A397333_CentralO -> 0
    A397333_PosHalf -> 0
    A397333_NegHalf -> 0
    A397333_TransNat0 -> 0
    A397333_TransSqrs -> 0
    A397333_BinConv -> 0
    A397333_InvBinConv -> 0
    A397333_PolyRow3 -> 0
    A397333_PolyCol2 -> 0
    A397333_PolyCol3 -> 0
    A397333_PolyDiag -> 0
    A397333_RevToff11 -> 0
    A397333_RevTrev11 -> 0
    A397333_RevTantidiag -> 0
    A397333_RevTacc -> 0
    A397333_RevTalt -> 0
    A397333_RevTder -> 0
    A397333_RevEvenSum -> 0
    A397333_RevOddSum -> 0
    A397333_RevAccRevSum -> 0
    A397333_RevAntiDSum -> 0
    A397333_RevColMiddle -> 0
    A397333_RevCentralO -> 0
    A397333_RevPosHalf -> 0
    A397333_RevNegHalf -> 0
    A397333_RevTransNat0 -> 0
    A397333_RevTransNat1 -> 0
    A397333_RevTransSqrs -> 0
    A397333_RevPolyRow3 -> 0
    A397333_RevPolyCol3 -> 0
    A397333_RevPolyDiag -> 0
    A397333_TablDiag0 -> 12
    A397333_TablGcd -> 12
    A397333_PolyRow1 -> 27
    A397333_TablCol0 -> 169
    A397333_RevPolyRow1 -> 5408
    A397333_TablDiag1 -> 5449
    A397333_PolyRow2 -> 14209
    A397333_AccRevSum -> 124824
    A397333_TransNat1 -> 124824
    A397333_TablCol1 -> 213326
    A397333_RevPolyRow2 -> 214660
    A397333_TablSum -> 397332
    A397333_AbsSum -> 397332
    A397333_Triangle -> 397333
    A397333_Talt -> 397333

    Dict length: 69
'''
