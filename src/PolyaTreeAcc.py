from functools import cache
from _tabltypes import Table

"""Polya Trees accumulated
[0] [1]
[1] [0, 1]
[2] [0, 1,  2]
[3] [0, 1,  3,  4]
[4] [0, 1,  5,  8,   9]
[5] [0, 1,  7, 15,  19,  20]
[6] [0, 1, 11, 29,  42,  47,  48]
[7] [0, 1, 15, 53,  89, 108, 114, 115]
[8] [0, 1, 22, 98, 191, 252, 278, 285, 286]

           STATUS: EXPERIMENTAL
"""


@cache
def divisors(n: int) -> list[int]:
    return [d for d in range(n, 0, -1) if n % d == 0]


@cache
def _h(n: int, k: int) -> int:
    return sum(d * _T(d, k) for d in divisors(n))


# A244925  (which is (1, 0)-based)
#@cache
#def _H(n: int, k: int) -> int:
#    return sum(d * _T(d, k) for d in divisors(n) if k <= d)


# A113704
#@cache
#def _e(n: int, k: int) -> int:
#    return sum(d * T(d, k) for d in divisors(n) if k == d)


# Call the function _h, _H, or _e according to your use case.
@cache
def _T(n: int, k: int) -> int:
    if n == 1:
        return int(k > 0)

    return sum(_T(i, k) * _h(n - i, k - 1)
               for i in range(1, n)
            ) // (n - 1)


# _T(n, k) will add a (0,0,0...) column on the left.
# Interpretations exist for both cases, it is mainly
# a matter of terminology. The form _T(n + 1, k + 1) is
# to be prefered as it covers A113704 in the case k = d,
# which is our Divisibility triangle.
@cache
def polyatreeacc(n: int) -> list[int]:
    if n > 200:
        # raise ValueError("n is too large for this function.")
        print(f"ValueError: n = {n} is too large for function polyatreeacc.")
        return []
    return [_T(n + 1, k + 1) for k in range(n + 1)]


PolyaTreeAcc = Table(
    polyatreeacc, 
    "PolyaTreeAcc", 
    ["A375467"], 
    "", 
    r"%%"
)


if __name__ == "__main__":
    from _tabldict import InspectTable
    from _tablutils import TableGenerationTime

    InspectTable(PolyaTreeAcc)

    # EXPERIMENTAL

    for n in range(9):  # A375546
        print([_h(n, k) for k in range(n + 1)])

    #for n in range(9):  # A375467
    #    print([_H(n, k) for k in range(n + 1)])
        
    TableGenerationTime(PolyaTreeAcc, 204) 





''' OEIS
    PolyaTreeAcc_Tinvrev11     -> https://oeis.org/A-999999
    PolyaTreeAcc_Triangle      -> 0 
    PolyaTreeAcc_Trev          -> 0 
    PolyaTreeAcc_Toff11        -> 0 
    PolyaTreeAcc_Trev11        -> 0 
    PolyaTreeAcc_Tantidiag     -> 0 
    PolyaTreeAcc_Tacc          -> 0 
    PolyaTreeAcc_Talt          -> 0 
    PolyaTreeAcc_Tder          -> 0 
    PolyaTreeAcc_TablDiag1     -> 0 
    PolyaTreeAcc_TablDiag2     -> 0 
    PolyaTreeAcc_TablDiag3     -> 0 
    PolyaTreeAcc_TablLcm       -> 0 
    PolyaTreeAcc_EvenSum       -> 0 
    PolyaTreeAcc_OddSum        -> 0 
    PolyaTreeAcc_AltSum        -> 0 
    PolyaTreeAcc_AccSum        -> 0 
    PolyaTreeAcc_AccRevSum     -> 0 
    PolyaTreeAcc_AntiDSum      -> 0 
    PolyaTreeAcc_ColMiddle     -> 0 
    PolyaTreeAcc_CentralE      -> 0 
    PolyaTreeAcc_CentralO      -> 0 
    PolyaTreeAcc_PosHalf       -> 0 
    PolyaTreeAcc_NegHalf       -> 0 
    PolyaTreeAcc_TransNat0     -> 0 
    PolyaTreeAcc_TransNat1     -> 0 
    PolyaTreeAcc_TransSqrs     -> 0 
    PolyaTreeAcc_BinConv       -> 0 
    PolyaTreeAcc_InvBinConv    -> 0 
    PolyaTreeAcc_PolyRow3      -> 0 
    PolyaTreeAcc_PolyCol2      -> 0 
    PolyaTreeAcc_PolyCol3      -> 0 
    PolyaTreeAcc_PolyDiag      -> 0 
    PolyaTreeAcc_RevToff11     -> 0 
    PolyaTreeAcc_RevTrev11     -> 0 
    PolyaTreeAcc_RevTantidiag  -> 0 
    PolyaTreeAcc_RevTacc       -> 0 
    PolyaTreeAcc_RevTalt       -> 0 
    PolyaTreeAcc_RevTder       -> 0 
    PolyaTreeAcc_RevEvenSum    -> 0 
    PolyaTreeAcc_RevOddSum     -> 0 
    PolyaTreeAcc_RevAccRevSum  -> 0 
    PolyaTreeAcc_RevAntiDSum   -> 0 
    PolyaTreeAcc_RevColMiddle  -> 0 
    PolyaTreeAcc_RevCentralO   -> 0 
    PolyaTreeAcc_RevPosHalf    -> 0 
    PolyaTreeAcc_RevNegHalf    -> 0 
    PolyaTreeAcc_RevTransNat0  -> 0 
    PolyaTreeAcc_RevTransNat1  -> 0 
    PolyaTreeAcc_RevTransSqrs  -> 0 
    PolyaTreeAcc_RevPolyCol3   -> 0 
    PolyaTreeAcc_RevPolyDiag   -> 0 
    PolyaTreeAcc_TablCol0      -> https://oeis.org/A7
    PolyaTreeAcc_TablCol1      -> https://oeis.org/A12
    PolyaTreeAcc_TablGcd       -> https://oeis.org/A12
    PolyaTreeAcc_RevPolyRow1   -> https://oeis.org/A12
    PolyaTreeAcc_PolyRow1      -> https://oeis.org/A27
    PolyaTreeAcc_RevPolyRow2   -> https://oeis.org/A27
    PolyaTreeAcc_TablCol2      -> https://oeis.org/A41
    PolyaTreeAcc_TablDiag0     -> https://oeis.org/A81
    PolyaTreeAcc_TablMax       -> https://oeis.org/A81
    PolyaTreeAcc_TablCol3      -> https://oeis.org/A1383
    PolyaTreeAcc_PolyRow2      -> https://oeis.org/A14105
    PolyaTreeAcc_RevPolyRow3   -> https://oeis.org/A14206
    PolyaTreeAcc_TablSum       -> https://oeis.org/A375468
    PolyaTreeAcc_AbsSum        -> https://oeis.org/A375468

    PolyaTreeAcc: Distinct: 11, Hits: 15, Misses: 51
'''
