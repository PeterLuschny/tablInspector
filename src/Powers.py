from functools import cache
from _tabltypes import Table

"""Powers.

[0]  [1]
[1]  [0, 1]
[2]  [0, 1,   1]
[3]  [0, 1,   2,   1]
[4]  [0, 1,   4,   3,    1]
[5]  [0, 1,   8,   9,    4,   1]
[6]  [0, 1,  16,  27,   16,   5,   1]
[7]  [0, 1,  32,  81,   64,  25,   6,  1]
[8]  [0, 1,  64, 243,  256, 125,  36,  7, 1]
[9]  [0, 1, 128, 729, 1024, 625, 216, 49, 8, 1]

"""

@cache
def powers(n: int) -> list[int]:
    if n == 0:
        return [1]

    lrow = powers(n - 1)
    return [k * lrow[k] for k in range(n)] + [1]


Powers = Table(
    powers,        # the generating function
    "Powers",      # name of the table
    ["A004248", "A009998", "A051129"], # similar sequences in OEIS
    "A000000",    # inverse triangle exists, but not in OEIS
    r"k^{n - k}"  # TeX of defining formula
)


if __name__ == "__main__":
    from _tabldatabase import InspectTable

    InspectTable(Powers)






''' OEIS
    Powers_Tinv          -> 0 
    Powers_Trevinv       -> 0 
    Powers_Tinv11        -> 0 
    Powers_Tinvrev11     -> 0 
    Powers_Trevinv11     -> 0 
    Powers_Tantidiag     -> 0 
    Powers_Tacc          -> 0 
    Powers_TablLcm       -> 0 
    Powers_EvenSum       -> 0 
    Powers_OddSum        -> 0 
    Powers_AccRevSum     -> 0 
    Powers_NegHalf       -> 0 
    Powers_TransNat1     -> 0 
    Powers_RevTrev11     -> 0 
    Powers_RevTantidiag  -> 0 
    Powers_RevTacc       -> 0 
    Powers_RevTder       -> 0 
    Powers_RevOddSum     -> 0 
    Powers_RevNegHalf    -> 0 
    Powers_RevTransSqrs  -> 0 
    Powers_RevPolyCol3   -> 0 
    Powers_TablCol0      -> https://oeis.org/A7
    Powers_TablCol1      -> https://oeis.org/A12
    Powers_TablDiag0     -> https://oeis.org/A12
    Powers_RevPolyRow1   -> https://oeis.org/A12
    Powers_TablDiag1     -> https://oeis.org/A27
    Powers_PolyRow1      -> https://oeis.org/A27
    Powers_RevPolyRow2   -> https://oeis.org/A27
    Powers_TablCol2      -> https://oeis.org/A79
    Powers_RevCentralO   -> https://oeis.org/A169
    Powers_TablCol3      -> https://oeis.org/A244
    Powers_BinConv       -> https://oeis.org/A248
    Powers_TablDiag2     -> https://oeis.org/A290
    Powers_RevPolyRow3   -> https://oeis.org/A290
    Powers_CentralE      -> https://oeis.org/A312
    Powers_TablDiag3     -> https://oeis.org/A578
    Powers_PolyRow2      -> https://oeis.org/A2378
    Powers_TransNat0     -> https://oeis.org/A3101
    Powers_TablMax       -> https://oeis.org/A3320
    Powers_InvBinConv    -> https://oeis.org/A3725
    Powers_Trev          -> https://oeis.org/A3992
    Powers_RevTalt       -> https://oeis.org/A3992
    Powers_Triangle      -> https://oeis.org/A4248
    Powers_Talt          -> https://oeis.org/A4248
    Powers_CentralO      -> https://oeis.org/A7778
    Powers_Toff11        -> https://oeis.org/A9998
    Powers_Trev11        -> https://oeis.org/A9999
    Powers_TablSum       -> https://oeis.org/A26898
    Powers_AbsSum        -> https://oeis.org/A26898
    Powers_AltSum        -> https://oeis.org/A38125
    Powers_PolyRow3      -> https://oeis.org/A45991
    Powers_Tder          -> https://oeis.org/A51129
    Powers_RevTransNat0  -> https://oeis.org/A62807
    Powers_TransSqrs     -> https://oeis.org/A62809
    Powers_RevToff11     -> https://oeis.org/A95884
    Powers_AccSum        -> https://oeis.org/A101495
    Powers_RevAccRevSum  -> https://oeis.org/A101495
    Powers_RevTransNat1  -> https://oeis.org/A101495
    Powers_AntiDSum      -> https://oeis.org/A104872
    Powers_ColMiddle     -> https://oeis.org/A110132
    Powers_RevColMiddle  -> https://oeis.org/A110138
    Powers_TablGcd       -> https://oeis.org/A174965
    Powers_RevPolyDiag   -> https://oeis.org/A349969
    Powers_PosHalf       -> https://oeis.org/A349970
    Powers_PolyCol2      -> https://oeis.org/A351279
    Powers_RevPosHalf    -> https://oeis.org/A351279
    Powers_PolyCol3      -> https://oeis.org/A351282
    Powers_PolyDiag      -> https://oeis.org/A351340
    Powers_RevAntiDSum   -> https://oeis.org/A352944
    Powers_RevEvenSum    -> https://oeis.org/A353016

    Powers: Distinct: 39, Hits: 49, Misses: 21
'''
