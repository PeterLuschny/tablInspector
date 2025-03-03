from functools import cache
from Binomial import Binomial
from _tabltypes import Table

"""Sidi

  [0] [1]
  [1] [0, 1]
  [2] [0, -2, 4]
  [3] [0, 3, -24, 27]
  [4] [0, -4, 96, -324, 256]
  [5] [0, 5, -320, 2430, -5120, 3125]
  [6] [0, -6, 960, -14580, 61440, -93750, 46656]
  [7] [0, 7, -2688, 76545, -573440, 1640625, -1959552, 823543]      

"""

@cache
def sidi(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [(-1)**(n-k)*Binomial(n, k)*k**n for k in range(n+1)]
    return row


Sidi = Table(
    sidi,        # the generating function
    "Sidi",      # name of the table
    ["A258773"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"(-1)^(n-k) \binom{n}{k} k^n"  # TeX of the defining formula
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Sidi)

''' OEIS
    Sidi_Trev -> 0
    Sidi_Toff11 -> 0
    Sidi_Trev11 -> 0
    Sidi_Tantidiag -> 0
    Sidi_Tacc -> 0
    Sidi_Tder -> 0
    Sidi_TablCol3 -> 0
    Sidi_TablDiag2 -> 0
    Sidi_TablDiag3 -> 0
    Sidi_TablLcm -> 0
    Sidi_TablMax -> 0
    Sidi_EvenSum -> 0
    Sidi_OddSum -> 0
    Sidi_AccSum -> 0
    Sidi_AntiDSum -> 0
    Sidi_ColMiddle -> 0
    Sidi_CentralE -> 0
    Sidi_CentralO -> 0
    Sidi_BinConv -> 0
    Sidi_PolyRow3 -> 0
    Sidi_PolyCol3 -> 0
    Sidi_PolyDiag -> 0
    Sidi_RevToff11 -> 0
    Sidi_RevTrev11 -> 0
    Sidi_RevTantidiag -> 0
    Sidi_RevTacc -> 0
    Sidi_RevTalt -> 0
    Sidi_RevTder -> 0
    Sidi_RevOddSum -> 0
    Sidi_RevAccRevSum -> 0
    Sidi_RevAntiDSum -> 0
    Sidi_RevColMiddle -> 0
    Sidi_RevCentralO -> 0
    Sidi_RevTransNat1 -> 0
    Sidi_RevTransSqrs -> 0
    Sidi_RevPolyRow3 -> 0
    Sidi_RevPolyCol3 -> 0
    Sidi_RevPolyDiag -> 0
    Sidi_TablCol0 -> 7
    Sidi_RevPolyRow1 -> 12
    Sidi_TablCol1 -> 27
    Sidi_TablGcd -> 27
    Sidi_PolyRow1 -> 27
    Sidi_TablSum -> 142
    Sidi_TablDiag0 -> 312
    Sidi_TransNat0 -> 1286
    Sidi_RevTransNat0 -> 1804
    Sidi_PolyRow2 -> 2939
    Sidi_RevPolyRow2 -> 5843
    Sidi_TransSqrs -> 37960
    Sidi_AltSum -> 72034
    Sidi_AbsSum -> 72034
    Sidi_TablCol2 -> 100381
    Sidi_AccRevSum -> 121635
    Sidi_TransNat1 -> 121635
    Sidi_TablDiag1 -> 209290
    Sidi_RevEvenSum -> 218296
    Sidi_Triangle -> 258773
    Sidi_Talt -> 258773
    Sidi_InvBinConv -> 336828
    Sidi_PosHalf -> 344053
    Sidi_PolyCol2 -> 375540
    Sidi_RevPosHalf -> 375540
    Sidi_RevNegHalf -> 375541
    Sidi_NegHalf -> 375542
    '''