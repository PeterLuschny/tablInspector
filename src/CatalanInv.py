from functools import cache
from _tabltypes import Table

"""Inverse Catalan triangle. Unsigned version.

   0:   1
   1:   0    1
   2:   0    2    1
   3:   0    3    4    1
   4:   0    4   10    6    1
   5:   0    5   20   21    8    1
   6:   0    6   35   56   36   10    1
   7:   0    7   56  126  120   55   12    1
   8:   0    8   84  252  330  220   78   14    1
   9:   0    9  120  462  792  715  364  105   16    1
  10:   0   10  165  792 1716 2002 1365  560  136   18    1
"""

@cache
def catalaninv(n: int) -> list[int]:
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]

    row = [0]*(n+1)
    c0 = catalaninv(n-2) + [0, 0]
    c1 = catalaninv(n-1) + [0]
    for k in range(1, n+1):
        row[k] = c1[k-1] + 2*c1[k] - c0[k]
    return row


CatalanInv = Table(
    catalaninv,    # the generating function
    "CatalanInv",  # name of the table
    ["A128908", "A053122", "A285072"],   # similar sequences in OEIS
    "A128899",     # id of inverse sequence
    r"T(n,k)=0"    # TeX of defining formula
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CatalanInv)


''' OEIS
    CatalanInv_Trev          -> 0 
    CatalanInv_Tantidiag     -> 0 
    CatalanInv_Tacc          -> 0 
    CatalanInv_Tder          -> 0 
    CatalanInv_TablMax       -> 0 
    CatalanInv_ColMiddle     -> 0 
    CatalanInv_CentralO      -> 0 
    CatalanInv_TransSqrs     -> 0 
    CatalanInv_PolyDiag      -> 0 
    CatalanInv_RevToff11     -> 0 
    CatalanInv_RevTrev11     -> 0 
    CatalanInv_RevTantidiag  -> 0 
    CatalanInv_RevTacc       -> 0 
    CatalanInv_RevTalt       -> 0 
    CatalanInv_RevTder       -> 0 
    CatalanInv_RevOddSum     -> 0 
    CatalanInv_RevColMiddle  -> 0 
    CatalanInv_RevTransSqrs  -> 0 
    CatalanInv_RevPolyDiag   -> 0 
    CatalanInv_TablCol0      -> https://oeis.org/A7
    CatalanInv_TablDiag0     -> https://oeis.org/A12
    CatalanInv_RevPolyRow1   -> https://oeis.org/A12
    CatalanInv_TablCol1      -> https://oeis.org/A27
    CatalanInv_PolyRow1      -> https://oeis.org/A27
    CatalanInv_AntiDSum      -> https://oeis.org/A79
    CatalanInv_TablCol2      -> https://oeis.org/A292
    CatalanInv_TablCol3      -> https://oeis.org/A389
    CatalanInv_RevPolyRow3   -> https://oeis.org/A567
    CatalanInv_TablSum       -> https://oeis.org/A1906
    CatalanInv_AbsSum        -> https://oeis.org/A1906
    CatalanInv_PosHalf       -> https://oeis.org/A2450
    CatalanInv_TablDiag3     -> https://oeis.org/A2492
    CatalanInv_RevPolyRow2   -> https://oeis.org/A5408
    CatalanInv_PolyRow2      -> https://oeis.org/A5563
    CatalanInv_TablDiag1     -> https://oeis.org/A5843
    CatalanInv_RevNegHalf    -> https://oeis.org/A10673
    CatalanInv_AltSum        -> https://oeis.org/A11655
    CatalanInv_TablDiag2     -> https://oeis.org/A14105
    CatalanInv_TransNat0     -> https://oeis.org/A30267
    CatalanInv_Tinv11        -> https://oeis.org/A39598
    CatalanInv_RevCentralO   -> https://oeis.org/A45721
    CatalanInv_NegHalf       -> https://oeis.org/A49072
    CatalanInv_PolyCol2      -> https://oeis.org/A52530
    CatalanInv_Toff11        -> https://oeis.org/A78812
    CatalanInv_RevPolyCol3   -> https://oeis.org/A99459
    CatalanInv_TablLcm       -> https://oeis.org/A99996
    CatalanInv_OddSum        -> https://oeis.org/A113066
    CatalanInv_Tinv          -> https://oeis.org/A128899
    CatalanInv_Triangle      -> https://oeis.org/A128908
    CatalanInv_Talt          -> https://oeis.org/A128908
    CatalanInv_RevAntiDSum   -> https://oeis.org/A158943
    CatalanInv_CentralE      -> https://oeis.org/A165817
    CatalanInv_Trev11        -> https://oeis.org/A172431
    CatalanInv_BinConv       -> https://oeis.org/A262440
    CatalanInv_RevTransNat0  -> https://oeis.org/A281199
    CatalanInv_EvenSum       -> https://oeis.org/A290890
    CatalanInv_PolyCol3      -> https://oeis.org/A290902
    CatalanInv_AccRevSum     -> https://oeis.org/A290917
    CatalanInv_TransNat1     -> https://oeis.org/A290917
    CatalanInv_PolyRow3      -> https://oeis.org/A317637
    CatalanInv_TablGcd       -> https://oeis.org/A318829
    CatalanInv_InvBinConv    -> https://oeis.org/A350290
    CatalanInv_RevEvenSum    -> https://oeis.org/A376716
    CatalanInv_AccSum        -> https://oeis.org/A377866
    CatalanInv_RevAccRevSum  -> https://oeis.org/A377866
    CatalanInv_RevTransNat1  -> https://oeis.org/A377866

    CatalanInv: Distinct: 41, Hits: 47, Misses: 19
'''
