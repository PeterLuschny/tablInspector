from functools import cache
from _tabltypes import Table

"""Lucas triangle.
  [0] [2]
  [1] [1, 2]
  [2] [1, 3, 2]
  [3] [1, 4, 5, 2]
  [4] [1, 5, 9, 7, 2]
  [5] [1, 6, 14, 16, 9, 2]
  [6] [1, 7, 20, 30, 25, 11, 2]
  [7] [1, 8, 27, 50, 55, 36, 13, 2]
  [8] [1, 9, 35, 77, 105, 91, 49, 15, 2]
  [9] [1, 10, 44, 112, 182, 196, 140, 64, 17, 2]
"""


@cache
def lucas(n: int) -> list[int]:
    if n == 0: return [2]
    if n == 1: return [1, 2]

    row = lucas(n - 1) + [0]
    for k in range(n, 0, -1):
        row[k] += row[k - 1]
    return row


Lucas = Table(
    lucas, 
    "Lucas", 
    ["A029635", "A029653"], 
    "", 
    r"\binom{n}{k} + \binom{n-1}{k-1}"
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Lucas)




''' OEIS
    Lucas_Tacc          -> 0 
    Lucas_Tder          -> 0 
    Lucas_TablLcm       -> 0 
    Lucas_ColMiddle     -> 0 
    Lucas_InvBinConv    -> 0 
    Lucas_RevTacc       -> 0 
    Lucas_RevTalt       -> 0 
    Lucas_TablCol0      -> https://oeis.org/A12
    Lucas_TablGcd       -> https://oeis.org/A12
    Lucas_TablCol1      -> https://oeis.org/A27
    Lucas_RevPolyRow1   -> https://oeis.org/A27
    Lucas_AntiDSum      -> https://oeis.org/A32
    Lucas_NegHalf       -> https://oeis.org/A38
    Lucas_RevAntiDSum   -> https://oeis.org/A45
    Lucas_TablCol2      -> https://oeis.org/A96
    Lucas_TablDiag2     -> https://oeis.org/A290
    Lucas_TablDiag3     -> https://oeis.org/A330
    Lucas_PolyRow2      -> https://oeis.org/A384
    Lucas_PolyCol3      -> https://oeis.org/A2042
    Lucas_RevPolyRow2   -> https://oeis.org/A2378
    Lucas_PosHalf       -> https://oeis.org/A3946
    Lucas_RevPolyCol3   -> https://oeis.org/A3947
    Lucas_PolyCol2      -> https://oeis.org/A5030
    Lucas_RevPosHalf    -> https://oeis.org/A5030
    Lucas_TablDiag1     -> https://oeis.org/A5408
    Lucas_PolyRow1      -> https://oeis.org/A5408
    Lucas_TablCol3      -> https://oeis.org/A5581
    Lucas_TablSum       -> https://oeis.org/A7283
    Lucas_EvenSum       -> https://oeis.org/A7283
    Lucas_OddSum        -> https://oeis.org/A7283
    Lucas_AbsSum        -> https://oeis.org/A7283
    Lucas_RevEvenSum    -> https://oeis.org/A7283
    Lucas_RevOddSum     -> https://oeis.org/A7283
    Lucas_RevNegHalf    -> https://oeis.org/A10701
    Lucas_RevPolyRow3   -> https://oeis.org/A11379
    Lucas_PolyRow3      -> https://oeis.org/A15237
    Lucas_Triangle      -> https://oeis.org/A29635
    Lucas_Talt          -> https://oeis.org/A29635
    Lucas_Toff11        -> https://oeis.org/A29638
    Lucas_CentralE      -> https://oeis.org/A29651
    Lucas_BinConv       -> https://oeis.org/A29651
    Lucas_Trev          -> https://oeis.org/A29653
    Lucas_Tantidiag     -> https://oeis.org/A34807
    Lucas_AltSum        -> https://oeis.org/A39964
    Lucas_TablMax       -> https://oeis.org/A50168
    Lucas_RevColMiddle  -> https://oeis.org/A50168
    Lucas_CentralO      -> https://oeis.org/A51924
    Lucas_RevCentralO   -> https://oeis.org/A51960
    Lucas_RevTransNat0  -> https://oeis.org/A53220
    Lucas_TablDiag0     -> https://oeis.org/A55642
    Lucas_TransNat0     -> https://oeis.org/A66373
    Lucas_TransSqrs     -> https://oeis.org/A89658
    Lucas_PolyDiag      -> https://oeis.org/A89945
    Lucas_RevTrev11     -> https://oeis.org/A97207
    Lucas_AccRevSum     -> https://oeis.org/A98156
    Lucas_TransNat1     -> https://oeis.org/A98156
    Lucas_RevTinv11     -> https://oeis.org/A104709
    Lucas_RevToff11     -> https://oeis.org/A110813
    Lucas_Trev11        -> https://oeis.org/A121306
    Lucas_RevTantidiag  -> https://oeis.org/A129710
    Lucas_RevTder       -> https://oeis.org/A132776
    Lucas_RevTransSqrs  -> https://oeis.org/A276289
    Lucas_AccSum        -> https://oeis.org/A339252
    Lucas_RevAccRevSum  -> https://oeis.org/A339252
    Lucas_RevTransNat1  -> https://oeis.org/A339252
    Lucas_RevPolyDiag   -> https://oeis.org/A373395

    Lucas: Distinct: 45, Hits: 59, Misses: 7
'''
