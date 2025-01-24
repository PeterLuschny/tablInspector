from functools import cache
from _tabltypes import Table

"""CentralFactorial.

[0] [1]
[1] [1, 1]
[2] [1, 4, 12]
[3] [1, 9, 72, 360]
[4] [1, 16, 240, 2880, 20160]
[5] [1, 25, 600, 12600, 201600, 1814400]
[6] [1, 36, 1260, 40320, 1088640, 21772800, 239500800]
[7] [1, 49, 2352, 105840, 4233600, 139708800, 3353011200, 43589145600]
"""

@cache
def centralfactorial(n: int) -> list[int]:
    if n == 0:
        return [1]

    row = [1]*(n + 1)
    for k in range(0, n): 
        row[k+1] = row[k]*(n*n - k*k)
    return row


CentralFactorial = Table(
    centralfactorial,    # the generating function
    "CentralFactorial",  # name of the table
    ["A370707"], # similar sequences in OEIS
    "",          # no integer inverse triangle
    r"(-1)^k \prod_{j=0}^{k-1}\, (j - n)(j + n)"  # TeX of defining formula
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(CentralFactorial)

'''
    CentralFactorial_Trev          -> 0
    CentralFactorial_Tinvrev       -> 0
    CentralFactorial_Toff11        -> 0
    CentralFactorial_Trev11        -> 0
    CentralFactorial_Tantidiag     -> 0
    CentralFactorial_Tacc          -> 0
    CentralFactorial_Tder          -> 0
    CentralFactorial_TablCol3      -> 0
    CentralFactorial_TablDiag2     -> 0
    CentralFactorial_TablDiag3     -> 0
    CentralFactorial_EvenSum       -> 0
    CentralFactorial_OddSum        -> 0
    CentralFactorial_AltSum        -> 0
    CentralFactorial_AccSum        -> 0
    CentralFactorial_AccRevSum     -> 0
    CentralFactorial_AntiDSum      -> 0
    CentralFactorial_ColMiddle     -> 0
    CentralFactorial_CentralE      -> 0
    CentralFactorial_CentralO      -> 0
    CentralFactorial_PosHalf       -> 0
    CentralFactorial_NegHalf       -> 0
    CentralFactorial_TransNat0     -> 0
    CentralFactorial_TransNat1     -> 0
    CentralFactorial_TransSqrs     -> 0
    CentralFactorial_BinConv       -> 0
    CentralFactorial_InvBinConv    -> 0
    CentralFactorial_PolyRow2      -> 0
    CentralFactorial_PolyRow3      -> 0
    CentralFactorial_PolyCol2      -> 0
    CentralFactorial_PolyCol3      -> 0
    CentralFactorial_PolyDiag      -> 0
    CentralFactorial_RevToff11     -> 0
    CentralFactorial_RevTrev11     -> 0
    CentralFactorial_RevTinv11     -> 0
    CentralFactorial_RevTantidiag  -> 0
    CentralFactorial_RevTacc       -> 0
    CentralFactorial_RevTalt       -> 0
    CentralFactorial_RevTder       -> 0
    CentralFactorial_RevEvenSum    -> 0
    CentralFactorial_RevOddSum     -> 0
    CentralFactorial_RevAccRevSum  -> 0
    CentralFactorial_RevAntiDSum   -> 0
    CentralFactorial_RevColMiddle  -> 0
    CentralFactorial_RevCentralO   -> 0
    CentralFactorial_RevNegHalf    -> 0
    CentralFactorial_RevTransNat0  -> 0
    CentralFactorial_RevTransNat1  -> 0
    CentralFactorial_RevTransSqrs  -> 0
    CentralFactorial_RevPolyRow3   -> 0
    CentralFactorial_RevPolyCol3   -> 0
    CentralFactorial_RevPolyDiag   -> 0
    CentralFactorial_TablCol0      -> 12
    CentralFactorial_PolyRow1      -> 27
    CentralFactorial_RevPolyRow1   -> 27
    CentralFactorial_TablCol1      -> 290
    CentralFactorial_TablGcd       -> 290
    CentralFactorial_TablDiag0     -> 2674
    CentralFactorial_TablLcm       -> 2674
    CentralFactorial_TablMax       -> 2674
    CentralFactorial_TablCol2      -> 47928
    CentralFactorial_RevPolyRow2   -> 189833
    CentralFactorial_TablDiag1     -> 327882
    CentralFactorial_TablSum       -> 370704
    CentralFactorial_AbsSum        -> 370704
    CentralFactorial_Triangle      -> 370707
    CentralFactorial_Talt          -> 370707

    CentralFactorial: Distinct: 9, Hits: 15, Misses: 51
'''