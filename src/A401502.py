from functools import cache
from _tabltypes import Table

"""T(n, k) is the number of partitions of the set {1, 2, ..., n+k} into k
   nonempty lists, such that the smallest element of each list is not in 
   the initial position. The lists themselves are unordered.

   T(n, k) = (n + k)! * [x^k] Laguerre(n + k, -x-1, -x).


  [0]  1;
  [1]  0,     1;
  [2]  0,     4,      3;
  [3]  0,    18,     40,      15;
  [4]  0,    96,    430,     420,     105;
  [5]  0,   600,   4536,    8260,    5040,     945;
  [6]  0,  4320,  49644,  144928,  157500,   69300,   10395;
  [7]  0, 35280, 574848, 2460780, 4145680, 3153150, 1081080, 135135;
"""

@cache
def a401502(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = [0]*(n + 1)
    prev2 = a401502(n-2)
    prev1 = a401502(n-1)
    row[n] = (2*n - 1) * prev1[n - 1] 
    row[n-1] = (2*n - 2) * (prev1[n - 2] + 2*prev1[n - 1])
    for k in range(1, n-1):
        row[k] = (n+k-1) * (prev1[k-1] + 2*prev1[k] - (n+k-2)*prev2[k])

    return row


A401502 = Table(
    a401502,      # the generating function
    "A401502",    # name of the table
    ["A401502"],  # similar sequences in OEIS
    "",           # id of inverse sequence if it exists
    r"T(n,k) = (n + k)!  [x^k] Laguerre(n + k, -x-1, -x)."  # TeX form 
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(A401502)



''' OEIS
    A401502_Toff11 -> 0 
    A401502_Trev11 -> 0 
    A401502_Tantidiag -> 0 
    A401502_Tacc -> 0 
    A401502_Tder -> 0 
    A401502_TablCol2 -> 0 
    A401502_TablCol3 -> 0 
    A401502_TablDiag1 -> 0 
    A401502_TablDiag2 -> 0 
    A401502_TablDiag3 -> 0 
    A401502_TablLcm -> 0 
    A401502_TablMax -> 0 
    A401502_EvenSum -> 0 
    A401502_OddSum -> 0 
    A401502_AccSum -> 0 
    A401502_AccRevSum -> 0 
    A401502_ColMiddle -> 0 
    A401502_CentralE -> 0 
    A401502_CentralO -> 0 
    A401502_PosHalf -> 0 
    A401502_NegHalf -> 0 
    A401502_TransNat0 -> 0 
    A401502_TransNat1 -> 0 
    A401502_TransSqrs -> 0 
    A401502_BinConv -> 0 
    A401502_InvBinConv -> 0 
    A401502_PolyRow3 -> 0 
    A401502_PolyCol2 -> 0 
    A401502_PolyCol3 -> 0 
    A401502_PolyDiag -> 0 
    A401502_RevToff11 -> 0 
    A401502_RevTrev11 -> 0 
    A401502_RevTantidiag -> 0 
    A401502_RevTacc -> 0 
    A401502_RevTder -> 0 
    A401502_RevEvenSum -> 0 
    A401502_RevOddSum -> 0 
    A401502_RevAccRevSum -> 0 
    A401502_RevAntiDSum -> 0 
    A401502_RevColMiddle -> 0 
    A401502_RevCentralO -> 0 
    A401502_RevPosHalf -> 0 
    A401502_RevNegHalf -> 0 
    A401502_RevTransNat0 -> 0 
    A401502_RevTransNat1 -> 0 
    A401502_RevTransSqrs -> 0 
    A401502_RevPolyRow3 -> 0 
    A401502_RevPolyCol3 -> 0 
    A401502_RevPolyDiag -> 0 
    A401502_TablCol0     -> https://oeis.org/A7
    A401502_TablGcd      -> https://oeis.org/A12
    A401502_RevPolyRow1  -> https://oeis.org/A12
    A401502_PolyRow1     -> https://oeis.org/A27
    A401502_TablDiag0    -> https://oeis.org/A1147
    A401502_TablCol1     -> https://oeis.org/A1563
    A401502_RevPolyRow2  -> https://oeis.org/A4767
    A401502_TablSum      -> https://oeis.org/A48174
    A401502_AbsSum       -> https://oeis.org/A48174
    A401502_AntiDSum     -> https://oeis.org/A52852
    A401502_PolyRow2     -> https://oeis.org/A140676
    A401502_AltSum       -> https://oeis.org/A331404
    A401502_Trev         -> https://oeis.org/A401501
    A401502_RevTalt      -> https://oeis.org/A401501
    A401502_Triangle     -> https://oeis.org/A401502
    A401502_Talt         -> https://oeis.org/A401502

    A401502: Distinct: 13, Hits: 16, Misses: 49
'''
