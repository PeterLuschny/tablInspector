from functools import cache
from _tabltypes import Table

"""To call this triangle 'LucasInv' is a (slight) misnomer. 
This is an integer version of the matrix inverse of the Lucas
triangle. T(n, k) = -LucasInv(n, k)*(-2)^(n-k+1). 

  [0]  1;
  [1]  1,   1;
  [2]  1,   3,    1;
  [3]  1,   7,    5,    1;
  [4]  1,  15,   17,    7,    1;
  [5]  1,  31,   49,   31,    9,    1;
  [6]  1,  63,  129,  111,   49,   11,   1;
  [7]  1, 127,  321,  351,  209,   71,  13,   1;
  [8]  1, 255,  769, 1023,  769,  351,  97,  15,   1;
  [9]  1, 511, 1793, 2815, 2561, 1471, 545, 127,  17,  1;
"""


@cache
def lucasinv(n: int) -> list[int]:
    if n == 0: return [1]

    r = [1] + lucasinv(n - 1) 
    for k in range(1, n): 
        r[k] += 2*r[k + 1]
    return  r


LucasInv = Table(
    lucasinv, 
    "LucasInv", 
    ["A112857"], 
    "A029635", 
    r"\sum_{j=k^n} \binom{n}{j} \binom{j-1}{k-1}"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(LucasInv)


''' OEIS
    LucasInv_Tinvrev       -> 0 
    LucasInv_Tinv11        -> 0 
    LucasInv_Tacc          -> 0 
    LucasInv_Tder          -> 0 
    LucasInv_TablLcm       -> 0 
    LucasInv_TablMax       -> 0 
    LucasInv_AccSum        -> 0 
    LucasInv_AccRevSum     -> 0 
    LucasInv_ColMiddle     -> 0 
    LucasInv_TransNat0     -> 0 
    LucasInv_TransNat1     -> 0 
    LucasInv_InvBinConv    -> 0 
    LucasInv_RevTinv11     -> 0 
    LucasInv_RevTantidiag  -> 0 
    LucasInv_RevTacc       -> 0 
    LucasInv_RevTder       -> 0 
    LucasInv_RevEvenSum    -> 0 
    LucasInv_RevOddSum     -> 0 
    LucasInv_RevAccRevSum  -> 0 
    LucasInv_RevAntiDSum   -> 0 
    LucasInv_RevColMiddle  -> 0 
    LucasInv_RevTransNat0  -> 0 
    LucasInv_RevTransNat1  -> 0 
    LucasInv_RevTransSqrs  -> 0 
    LucasInv_RevPolyRow3   -> 0 
    LucasInv_RevPolyCol3   -> 0 
    LucasInv_RevPolyDiag   -> 0 
    LucasInv_TablCol0      -> https://oeis.org/A12
    LucasInv_TablDiag0     -> https://oeis.org/A12
    LucasInv_TablGcd       -> https://oeis.org/A12
    LucasInv_RevNegHalf    -> https://oeis.org/A12
    LucasInv_AltSum        -> https://oeis.org/A27
    LucasInv_PolyRow1      -> https://oeis.org/A27
    LucasInv_RevPolyRow1   -> https://oeis.org/A27
    LucasInv_TablCol1      -> https://oeis.org/A225
    LucasInv_TablCol2      -> https://oeis.org/A337
    LucasInv_BinConv       -> https://oeis.org/A2003
    LucasInv_NegHalf       -> https://oeis.org/A3063
    LucasInv_TablDiag1     -> https://oeis.org/A5408
    LucasInv_TablSum       -> https://oeis.org/A7051
    LucasInv_AbsSum        -> https://oeis.org/A7051
    LucasInv_PolyCol2      -> https://oeis.org/A7583
    LucasInv_AntiDSum      -> https://oeis.org/A24537
    LucasInv_PolyRow2      -> https://oeis.org/A28387
    LucasInv_RevPolyRow2   -> https://oeis.org/A28387
    LucasInv_OddSum        -> https://oeis.org/A47926
    LucasInv_TablCol3      -> https://oeis.org/A55580
    LucasInv_TablDiag2     -> https://oeis.org/A56220
    LucasInv_TransSqrs     -> https://oeis.org/A80420
    LucasInv_PolyCol3      -> https://oeis.org/A83065
    LucasInv_PolyDiag      -> https://oeis.org/A83069
    LucasInv_PolyRow3      -> https://oeis.org/A83074
    LucasInv_EvenSum       -> https://oeis.org/A111277
    LucasInv_Triangle      -> https://oeis.org/A112857
    LucasInv_Talt          -> https://oeis.org/A112857
    LucasInv_Trev          -> https://oeis.org/A119258
    LucasInv_RevTalt       -> https://oeis.org/A119258
    LucasInv_CentralE      -> https://oeis.org/A119259
    LucasInv_RevCentralO   -> https://oeis.org/A178792
    LucasInv_Trev11        -> https://oeis.org/A193844
    LucasInv_RevToff11     -> https://oeis.org/A193844
    LucasInv_Toff11        -> https://oeis.org/A193845
    LucasInv_RevTrev11     -> https://oeis.org/A193845
    LucasInv_TablDiag3     -> https://oeis.org/A199899
    LucasInv_Tinv          -> https://oeis.org/A200139
    LucasInv_CentralO      -> https://oeis.org/A240721
    LucasInv_PosHalf       -> https://oeis.org/A247313
    LucasInv_Tantidiag     -> https://oeis.org/A257597

    LucasInv: Distinct: 31, Hits: 41, Misses: 27
'''
