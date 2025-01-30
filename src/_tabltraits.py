"""
This module provides various functions to analyze and transform integer triangles (Table objects).
It includes functions to compute different traits of tables, such as dot products, polynomials, table columns, diagonals, rows, and various transformations and convolutions of tables. Additionally, it provides functions to compute LCM, GCD, sums, and other properties of table rows and columns.
"""

from Binomial import Binomial, InvBinomial
from _tabltypes import Table, RevTable, rowgen, trait
from _tablutils import SeqToString
from typing import Tuple, TypeAlias
from itertools import accumulate
from more_itertools import flatten
from functools import reduce
from math import lcm, gcd
import operator


# #@

# use the defaults for size: 7 rows for tables or 28 terms


def dotproduct(vec: list[int], tor: list[int]) -> int:
    """
    Calculate the dot product of two vectors.

    Args:
        vec (list[int]): The first vector.
        tor (list[int]): The second vector.

    Returns:
        int: The dot product of the two vectors.

    Raises:
        ValueError: If the input vectors are not of the same length.

    Example:
        >>> dotproduct([1, 2, 3], [4, 5, 6])
        32
    """
    """Returns the dot product of the two vectors."""
    return sum(map(operator.mul, vec, tor))


def Triangle(T: Table, size: int = 7) -> list[int]:
    """
    Generates a list of integers representing a triangle pattern from the given table.

    Args:
        T (Table): The table from which to generate the triangle pattern.
        size (int, optional): The size of the triangle. Defaults to 7.

    Returns:
        list[int]: A list of integers representing the triangle pattern.
    """
    return T.flat(size)


def Trev(T: Table, size: int = 7) -> list[int]:
    """
    Generate a list of reversed elements from a Table object.

    Args:
        T (Table): The Table object containing elements to be reversed.
        size (int, optional): The number of elements to reverse. Defaults to 7.

    Returns:
        list[int]: A flattened list of reversed elements from the Table.
    """
    return list(flatten([T.rev(n) for n in range(size)]))


def Tinv(T: Table, size: int = 7) -> list[int]:
    """
    Inverts the given table and flattens the result.

    Args:
        T (Table): The table to be inverted.
        size (int, optional): The size parameter for the inversion. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers representing the inverted table.
    """
    return list(flatten(T.inv(size)))


def Tinvrev(T: Table, size: int = 7) -> list[int]:
    """
    Inverts and reverses the given table and returns the result as a flattened list.

    Args:
        T (Table): The table to be inverted and reversed.
        size (int, optional): The size parameter for the inversion and reversal. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers after inverting and reversing the table.
    """
    return list(flatten(T.invrev(size)))


def Toff11(T: Table, size: int = 7) -> list[int]:
    """
    Creates a new Table object offset by 1 row and 1 column from the original table,
    and returns a flattened list of the new table's elements.

    Args:
        T (Table): The original table object.
        size (int, optional): The size parameter for the flat method. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers from the new table.
    """
    T11 = Table(T.off(1, 1), T.id + "off11")
    return T11.flat(size)


def Trev11(T: Table, size: int = 7) -> list[int]:
    """
    Generate a flattened list of reversed elements from a Table object.

    Args:
        T (Table): The Table object containing the data.
        size (int, optional): The number of elements to reverse. Defaults to 7.

    Returns:
        list[int]: A flattened list of reversed elements from the Table.
    """
    return list(flatten([T.rev11(n) for n in range(size)]))


def Tinv11(T: Table, size: int = 7) -> list[int]:
    """
    Compute the inverse of the table T using the inv11 method and flatten the result.

    Args:
        T (Table): The table object which has the inv11 method.
        size (int, optional): The size parameter to be passed to the inv11 method. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers representing the inverse of the table.
    """
    InvT11 = T.inv11(size)
    return list(flatten(InvT11))


def Tinvrev11(T: Table, size: int = 7) -> list[int]:
    """
    Generate a flattened list from the inverse revision of a table.

    Args:
        T (Table): The table object that contains the `invrev11` method.
        size (int, optional): The size parameter to be passed to the `invrev11` method. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers resulting from the inverse revision of the table.
    """
    InvrevT11 = T.invrev11(size)
    return list(flatten(InvrevT11))


def Talt(T: Table, size: int = 7) -> list[int]:
    """
    Generate a list of alternative values from a Table object.

    This function calls the `alt` method of the provided Table object `T` for
    each integer in the range from 0 to `size - 1`, flattens the resulting lists,
    and returns the flattened list.

    Args:
        T (Table): The Table object from which to generate alternative values.
        size (int, optional): The number of alternative values to generate. Defaults to 7.

    Returns:
        list[int]: A flattened list of alternative values from the Table object.
    """
    return list(flatten([T.alt(n) for n in range(size)]))


def Tacc(T: Table, size: int = 7) -> list[int]:
    """
    Accumulate values from a Table object.

    This function flattens the accumulated values from the Table object `T`
    for a given range specified by `size`.

    Args:
        T (Table): The Table object from which to accumulate values.
        size (int, optional): The range of values to accumulate. Defaults to 7.

    Returns:
        list[int]: A flattened list of accumulated values.
    """
    return list(flatten([T.acc(n) for n in range(size)]))


def Tder(T: Table, size: int = 7) -> list[int]:
    """
    Generate a list of derivatives from a Table object.

    Args:
        T (Table): The Table object from which to derive values.
        size (int, optional): The number of derivatives to compute. Defaults to 7.

    Returns:
        list[int]: A flattened list of derivatives.
    """
    return list(flatten([T.der(n) for n in range(size)]))


# Needs 9 rows
def Tantidiag(T: Table, size: int = 9) -> list[int]:
    """
    Generate a list of elements from the antidiagonals of a table.

    Args:
        T (Table): The table from which to extract antidiagonals.
        size (int, optional): The number of antidiagonals to extract. Defaults to 9.

    Returns:
        list[int]: A flattened list of elements from the antidiagonals of the table.
    """
    return list(flatten([T.antidiag(n) for n in range(size)]))


def TablCol(T: Table, col: int, size: int = 28) -> list[int]:
    """
    Extracts a column from a table and returns it as a list of integers.

    Args:
        T (Table): The table from which to extract the column.
        col (int): The index of the column to extract.
        size (int, optional): The number of elements to extract from the column. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the extracted column.
    """
    return [T(col + n, col) for n in range(size)]


def TablCol0(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Retrieve the first column of a table.

    Args:
        T (Table): The table from which to retrieve the column.
        size (int, optional): The number of elements to retrieve. Defaults to 28.
        rev (bool, optional): If True, retrieve the diagonal instead of the column. Defaults to False.

    Returns:
        list[int]: A list of integers representing the first column or the diagonal of the table.
    """
    if rev:
        return TablDiag0(T, size)
    else:
        return [T(n, 0) for n in range(size)]


def TablCol1(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generate a list of integers representing a column in a table.

    Args:
        T (Table): The table object from which to extract the column.
        size (int, optional): The number of elements in the column. Defaults to 28.
        rev (bool, optional): If True, return the diagonal elements instead of the column. Defaults to False.

    Returns:
        list[int]: A list of integers representing the column or diagonal elements.
    """
    if rev:
        return TablDiag1(T, size)
    else:
        return [T(1 + n, 1) for n in range(size)]


def TablCol2(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generates a list of integers based on the provided Table object.

    Args:
        T (Table): The Table object to generate the list from.
        size (int, optional): The size of the list to generate. Defaults to 28.
        rev (bool, optional): If True, generates the list using the TablDiag2 function. Defaults to False.

    Returns:
        list[int]: A list of integers generated from the Table object.
    """
    if rev:
        return TablDiag2(T, size)
    else:
        return [T(2 + n, 2) for n in range(size)]


def TablCol3(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generate a list of integers based on the given Table object.

    Args:
        T (Table): The Table object to generate the list from.
        size (int, optional): The number of elements to generate. Defaults to 28.
        rev (bool, optional): If True, use the TablDiag3 function to generate the list. Defaults to False.

    Returns:
        list[int]: A list of integers generated from the Table object.
    """
    if rev:
        return TablDiag3(T, size)
    else:
        return [T(3 + n, 3) for n in range(size)]


def TablDiag(T: Table, diag: int, size: int = 28) -> list[int]:
    """
    Extracts a diagonal from a table.

    Args:
        T (Table): The table from which to extract the diagonal.
        diag (int): The starting index of the diagonal.
        size (int, optional): The number of elements to extract from the diagonal. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the diagonal elements.
    """
    return [T(diag + k, k) for k in range(size)]


def TablDiag0(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generate a list of diagonal elements from a table.

    Args:
        T (Table): The table from which to extract diagonal elements.
        size (int, optional): The number of elements to extract. Defaults to 28.
        rev (bool, optional): If True, extract elements from the first column instead of the diagonal. Defaults to False.

    Returns:
        list[int]: A list of integers representing the diagonal elements or the first column elements.
    """
    if rev:
        return TablCol0(T, size)
    else:
        return [T(k, k) for k in range(size)]


def TablDiag1(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generates a list of integers based on the provided table function `T`.

    If `rev` is True, the function returns the result of `TablCol1(T, size)`.
    Otherwise, it returns a list of integers generated by calling `T(1 + k, k)` 
    for each `k` in the range from 0 to `size - 1`.

    Args:
        T (Table): A table function that takes two integer arguments.
        size (int, optional): The size of the list to generate. Defaults to 28.
        rev (bool, optional): A flag to determine which list generation method to use. Defaults to False.

    Returns:
        list[int]: A list of integers generated based on the provided table function `T`.
    """
    if rev:
        return TablCol1(T, size)
    else:
        return [T(1 + k, k) for k in range(size)]


def TablDiag2(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generate a list of integers based on the provided Table function.

    If `rev` is True, the function returns the result of `TablCol2(T, size)`.
    Otherwise, it returns a list of integers generated by calling the Table
    function `T` with parameters (2 + k, k) for k in the range of `size`.

    Args:
        T (Table): A function that takes two integers and returns an integer.
        size (int, optional): The number of elements to generate. Defaults to 28.
        rev (bool, optional): A flag to determine which list generation method to use. Defaults to False.

    Returns:
        list[int]: A list of integers generated based on the provided Table function.
    """
    if rev:
        return TablCol2(T, size)
    else:
        return [T(2 + k, k) for k in range(size)]


def TablDiag3(T: Table, size: int = 28, rev: bool = False) -> list[int]:
    """
    Generate a list of integers based on the provided Table function.

    If `rev` is True, the function returns the result of `TablCol3(T, size)`.
    Otherwise, it returns a list of integers generated by calling the Table function `T`
    with parameters (3 + k, k) for k in the range of `size`.

    Args:
        T (Table): A function that takes two integer arguments and returns an integer.
        size (int, optional): The number of elements to generate. Defaults to 28.
        rev (bool, optional): A flag to determine which list to return. Defaults to False.

    Returns:
        list[int]: A list of integers generated based on the provided Table function.
    """
    if rev:
        return TablCol3(T, size)
    else:
        return [T(3 + k, k) for k in range(size)]


def PolyRow(T: Table, row: int, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values for a given row in a table.

    Args:
        T (Table): The table object containing polynomial data.
        row (int): The row index for which to generate polynomial values.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for the specified row.
    """
    return [T.poly(row, x) for x in range(size)]


def PolyRow1(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values for the first row of a table.

    Args:
        T (Table): An instance of the Table class.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for the first row.
    """
    return [T.poly(1, x) for x in range(size)]


def PolyRow2(T: Table, size: int = 28) -> list[int]:
    """
    Generates a list of polynomial values of degree 2 for a given table.

    Args:
        T (Table): The table object that has a method `poly` to compute polynomial values.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 2.
    """
    return [T.poly(2, x) for x in range(size)]


def PolyRow3(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 for a given table.

    Args:
        T (Table): The table object that provides the polynomial function.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 3.
    """
    return [T.poly(3, x) for x in range(size)]


def PolyCol(T: Table, col: int, size: int = 28) -> list[int]:
    """
    Generates a list of polynomial values for a specified column in a table.

    Args:
        T (Table): The table object containing the data.
        col (int): The column index for which polynomial values are to be generated.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values for the specified column.
    """
    return [T.poly(x, col) for x in range(size)]


def PolyCol1(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 1 for a given table.

    Args:
        T (Table): The table object that contains the polynomial method.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 1.
    """
    return [T.poly(x, 1) for x in range(size)]


def PolyCol2(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 2 for a given table.

    Args:
        T (Table): An instance of the Table class with a method `poly` that computes polynomial values.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 2.
    """
    return [T.poly(x, 2) for x in range(size)]


def PolyCol3(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 for a given table.

    Args:
        T (Table): The table object that contains the method `poly`.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 3.
    """
    return [T.poly(x, 3) for x in range(size)]


def PolyDiag(T: Table, size: int = 28) -> list[int]:
    """
    Generates a list of polynomial diagonal values from a given Table object.

    Args:
        T (Table): The Table object containing the polynomial data.
        size (int, optional): The number of diagonal values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial diagonal values.
    """
    return [T.poly(n, n) for n in range(size)]


def RowLcmGcd(g: rowgen, row: int, lg: bool) -> int:
    """
    Calculate the least common multiple (LCM) or greatest common divisor (GCD) of 
    non-trivial elements in a row generated by a given row generator function.
    Note our convention to exclude 0 and 1.

    Args:
        g (rowgen): A row generator function that takes an integer row index and 
                    returns an iterable of integers.
        row (int): The index of the row to process.
        lg (bool): If True, calculate the LCM of the elements; if False, calculate the GCD.

    Returns:
        int: The LCM or GCD of the non-trivial elements in the row. If the row contains 
             only trivial elements (-1, 0, 1), returns 1.
    """
    Z = [v for v in g(row) if v not in [-1, 0, 1]]
    if Z == []:
        return 1
    return lcm(*Z) if lg else gcd(*Z)


def TablLcm(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the least common multiple (LCM) for each row in a table.

    Args:
        T (Table): The table containing rows for which the LCM is to be calculated.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of LCM values for each row in the table.
    """
    return [RowLcmGcd(T.row, n, True) for n in range(size)]


def TablGcd(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the greatest common divisor (GCD) for each row in a table.

    Args:
        T (Table): The table containing rows to process.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of GCD values for each row in the table.
    """
    return [RowLcmGcd(T.row, n, False) for n in range(size)]


def TablMax(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the maximum absolute value in each row of a table.
    Note our convention to use the abs value.

    Args:
        T (Table): The table from which to calculate the maximum values.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of maximum absolute values for each row.
    """
    return [reduce(max, (abs(t) for t in T.row(n))) for n in range(size)]


def TablSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of elements in a table for a given range.

    Args:
        T (Table): The table object containing the data.
        size (int, optional): The number of elements to sum. Defaults to 28.

    Returns:
        list[int]: A list of sums for each element in the specified range.
    """
    return [T.sum(n) for n in range(size)]


def EvenSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of even-indexed elements in each row of a table.

    Args:
        T (Table): The table object containing rows of data.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of sums of even-indexed elements for each row.
    """
    return [sum(T.row(n)[::2]) for n in range(size)]


def OddSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of elements at odd indices for each row in a table.

    Args:
        T (Table): The table object containing rows of data.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of sums of elements at odd indices for each row.
    """
    return [sum(T.row(n)[1::2]) for n in range(size)]


def AltSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the alternating sum of elements in each row of a table.

    This function computes the alternating sum of elements in each row of the given table `T`.
    The alternating sum is defined as the sum of elements at even indices minus the sum of elements at odd indices.

    Args:
        T (Table): The table from which rows are taken.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of alternating sums for each row.
    """
    return [sum(T.row(n)[::2]) - sum(T.row(n)[1::2]) for n in range(size)]


def AbsSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the absolute sum of each row in a table.

    Args:
        T (Table): The table from which to calculate the absolute sums.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of absolute sums for each row.
    """
    return [sum(abs(t) for t in T.row(n)) for n in range(size)]


def AccSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the accumulated sum for each index up to a given size.

    Args:
        T (Table): An instance of the Table class with an 'acc' method.
        size (int, optional): The number of indices to calculate the accumulated sum for. Defaults to 28.

    Returns:
        list[int]: A list of accumulated sums for each index from 0 to size-1.
    """
    return [sum(T.acc(n)) for n in range(size)]


def AccRevSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the accumulated revenue sums for a given table.

    Args:
        T (Table): The table object containing revenue data.
        size (int, optional): The number of periods to calculate the accumulated sums for. Defaults to 28.

    Returns:
        list[int]: A list of accumulated revenue sums for each period.
    """
    return [sum(accumulate(T.rev(n))) for n in range(size)]


def AntiDSum(T: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of the antidiagonals of a table.

    Args:
        T (Table): The table from which to calculate the antidiagonal sums.
        size (int, optional): The number of antidiagonals to sum. Defaults to 28.

    Returns:
        list[int]: A list of sums of the antidiagonals.
    """
    return [sum(T.antidiag(n)) for n in range(size)]


def ColMiddle(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of values from the Table object.

    This function creates a list of values by calling the Table object `T` with 
    two arguments: the current index `n` and half of the current index `n // 2`. 
    The list is generated for indices ranging from 0 to `size - 1`.

    Args:
        T (Table): A callable object that takes two integer arguments and returns an integer.
        size (int, optional): The number of elements to generate in the list. Defaults to 28.

    Returns:
        list[int]: A list of integers generated by the Table object `T`.
    """
    return [T(n, n // 2) for n in range(size)]


def CentralE(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of integers using a given table function.

    This function takes a table function `T` and an optional size parameter `size`.
    It returns a list of integers generated by applying the table function `T` to
    pairs of integers (2 * n, n) for n in the range from 0 to `size` - 1.

    Args:
        T (Table): A table function that takes two integers and returns an integer.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of integers generated by the table function `T`.
    """
    return [T(2 * n, n) for n in range(size)]


def CentralO(T: Table, size: int = 28) -> list[int]:
    """
    Generates a list of integers by applying the function T to pairs of values.

    Args:
        T (Table): A function or callable that takes two integer arguments and returns an integer.
        size (int, optional): The number of elements to generate in the list. Defaults to 28.

    Returns:
        list[int]: A list of integers generated by applying T to pairs of values (2*n + 1, n) for n in range(size).
    """
    return [T(2 * n + 1, n) for n in range(size)]


def ColLeft(T: Table, size: int = 28) -> list[int]:
    """
    Extracts the leftmost column from a table.

    Args:
        T (Table): The table from which to extract the column.
        size (int, optional): The number of rows to extract. Defaults to 28.

    Returns:
        list[int]: A list containing the values from the leftmost column of the table.
    """
    return [T(n, 0) for n in range(size)]


def ColRight(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of integers by applying the function T to each integer in the range from 0 to size-1.

    Args:
        T (Table): A function that takes two integer arguments and returns an integer.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of integers generated by applying T to each integer in the specified range.
    """
    return [T(n, n) for n in range(size)]


def PolyFrac(row: list[int], x: int) -> int:
    """
    Evaluate a polynomial at a given point x.

    This function takes a list of coefficients representing a polynomial
    and evaluates the polynomial at the given value of x. The coefficients
    are assumed to be in descending order of powers.

    Args:
        row (list[int]): A list of integers representing the coefficients of the polynomial.
        x (int): The value at which to evaluate the polynomial.

    Returns:
        int: The result of the polynomial evaluation at x.
    """
    n = len(row) - 1
    return sum(c * x**(n - k) for (k, c) in enumerate(row))


def PosHalf(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions for the first half of the rows in the table.

    Args:
        T (Table): The table from which rows are taken.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions for the specified rows.
    """
    return [PolyFrac(T.row(n), 2) for n in range(size)]


def NegHalf(T: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions with a negative half exponent.

    Args:
        T (Table): The table from which rows are taken.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions with a -2 exponent.
    """
    return [PolyFrac(T.row(n), -2) for n in range(size)]


def TransNat0(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the given table using a natural transformation.

    Args:
        T (Table): The table to be transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    """
    return T.trans(lambda k: k, size)


def TransNat1(T: Table, size: int = 28) -> list[int]:
    """
    Transforms the given table by incrementing each element by 1.

    Args:
        T (Table): The table to be transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    """
    return T.trans(lambda k: k + 1, size)


def TransSqrs(T: Table, size: int = 28) -> list[int]:
    """
    Transforms each element in the table by squaring it.

    Args:
        T (Table): The table containing elements to be transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of squared elements from the table.
    """
    return T.trans(lambda k: k * k, size)


def BinConv(T: Table, size: int = 28) -> list[int]:
    """
    Converts each row of the given table to a binomial representation and computes the dot product.

    Args:
        T (Table): The input table with rows to be converted.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the dot product of each row with its binomial representation.
    """
    return [dotproduct(Binomial.row(n), T.row(n)) for n in range(size)]


def InvBinConv(T: Table, size: int = 28) -> list[int]:
    """
    Computes the inverse binomial convolution of the rows of a given table.

    Args:
        T (Table): The input table whose rows will be used in the convolution.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of integers representing the result of the inverse binomial convolution for each row.
    """
    return [dotproduct(InvBinomial.row(n), T.row(n)) for n in range(size)]

#------

def Rev_Toff11(t: Table, size: int = 7) -> list[int]:
    """
    Generates a list of integers by reversing the given table, offsetting it by (1, 1), 
    and flattening the result to the specified size.

    Args:
        t (Table): The input table to be reversed and processed.
        size (int, optional): The size of the flattened list to be returned. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers from the processed table.
    """
    T = RevTable(t)
    T11 = Table(T.off(1, 1), T.id + "off11")
    return T11.flat(size)


def Rev_Trev11(t: Table, size: int = 7) -> list[int]:
    """
    Generates a list of integers by applying the rev11 method of the RevTable class to a given Table object.

    Args:
        t (Table): The Table object to be processed.
        size (int, optional): The number of times to apply the rev11 method. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers resulting from the rev11 method applied to the Table object.
    """
    T = RevTable(t)
    return list(flatten([T.rev11(n) for n in range(size)]))


def Rev_Tinv11(t: Table, size: int = 7) -> list[int]:
    """
    Computes the inverse of the table `t` and flattens the result.

    Args:
        t (Table): The table to be inverted.
        size (int, optional): The size parameter for the inversion. Defaults to 7.

    Returns:
        list[int]: A flattened list of the inverted table.
    """
    T = RevTable(t)
    InvT11 = T.inv11(size)
    return list(flatten(InvT11))


def Rev_Talt(t: Table, size: int = 7) -> list[int]:
    """
    Generate a list of integers by reversing the table and flattening the alternates.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of alternates to consider. Defaults to 7.

    Returns:
        list[int]: A flattened list of integers from the alternates of the reversed table.
    """
    T = RevTable(t)
    return list(flatten([T.alt(n) for n in range(size)]))


def Rev_Tacc(t: Table, size: int = 7) -> list[int]:
    """
    Generate a list of accumulated values from a reversed table.

    Args:
        t (Table): The table to be reversed and processed.
        size (int, optional): The number of accumulations to perform. Defaults to 7.

    Returns:
        list[int]: A flattened list of accumulated values from the reversed table.
    """
    T = RevTable(t)
    return list(flatten([T.acc(n) for n in range(size)]))


def Rev_Tder(t: Table, size: int = 7) -> list[int]:
    """
    Generate a list of derivatives from a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of derivatives to compute. Defaults to 7.

    Returns:
        list[int]: A flattened list of derivatives from the reversed table.
    """
    T = RevTable(t)
    return list(flatten([T.der(n) for n in range(size)]))


# Needs 9 rows
def Rev_Tantidiag(t: Table, size: int = 9) -> list[int]:
    """
    Generates a list of integers from the reversed table's antidiagonals.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of antidiagonals to consider. Defaults to 9.

    Returns:
        list[int]: A flattened list of integers from the reversed table's antidiagonals.
    """
    T = RevTable(t)
    return list(flatten([T.antidiag(n) for n in range(size)]))


def Rev_PolyRow1(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values from a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 1 from the reversed table.
    """
    T = RevTable(t)
    return [T.poly(1, x) for x in range(size)]


def Rev_PolyRow2(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 2 from a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 2.
    """
    T = RevTable(t)
    return [T.poly(2, x) for x in range(size)]


def Rev_PolyRow3(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 for a given table.

    This function takes a table `t` and generates a list of polynomial values
    of degree 3 for each element in the range of `size`. The table is first
    reversed using the `RevTable` function, and then the polynomial values
    are computed.

    Args:
        t (Table): The input table to be reversed and processed.
        size (int, optional): The number of polynomial values to generate. 
                              Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 3.
    """
    T = RevTable(t)
    return [T.poly(3, x) for x in range(size)]


def Rev_PolyCol3(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial values of degree 3 from a reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of polynomial values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial values of degree 3.
    """
    T = RevTable(t)
    return [T.poly(x, 3) for x in range(size)]


def Rev_PolyDiag(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial diagonal values from a reversed table.

    Args:
        t (Table): The input table.
        size (int, optional): The number of diagonal values to generate. Defaults to 28.

    Returns:
        list[int]: A list of polynomial diagonal values.
    """
    T = RevTable(t)
    return [T.poly(n, n) for n in range(size)]


def Rev_EvenSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of even-indexed elements in each row of a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list of sums of even-indexed elements for each row.
    """
    T = RevTable(t)
    return [sum(T.row(n)[::2]) for n in range(size)]


def Rev_OddSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of odd-indexed elements in each row of a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of rows to process. Defaults to 28.

    Returns:
        list[int]: A list containing the sum of odd-indexed elements for each row.
    """
    T = RevTable(t)
    return [sum(T.row(n)[1::2]) for n in range(size)]


def Rev_AccRevSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the accumulated sum of reversed table values.

    Args:
        t (Table): The input table.
        size (int, optional): The number of elements to process. Defaults to 28.

    Returns:
        list[int]: A list of accumulated sums for each element in the reversed table.
    """
    T = RevTable(t)
    return [sum(accumulate(T.rev(n))) for n in range(size)]


def Rev_AntiDSum(t: Table, size: int = 28) -> list[int]:
    """
    Calculate the sum of the antidiagonals of a reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of antidiagonals to sum. Defaults to 28.

    Returns:
        list[int]: A list of sums of the antidiagonals.
    """
    T = RevTable(t)
    return [sum(T.antidiag(n)) for n in range(size)]


def Rev_ColMiddle(t: Table, size: int = 28) -> list[int]:
    """
    Generates a list of integers by reversing the table and selecting the middle column.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of elements to generate. Defaults to 28.

    Returns:
        list[int]: A list of integers from the middle column of the reversed table.
    """
    T = RevTable(t)
    return [T(n, n // 2) for n in range(size)]


def Rev_CentralO(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of integers based on the reversed table.

    This function takes a table `t` and an optional size parameter `size`. It reverses the table
    and then generates a list of integers by applying a specific formula to the reversed table.

    Args:
        t (Table): The input table to be reversed.
        size (int, optional): The number of elements to generate in the list. Defaults to 28.

    Returns:
        list[int]: A list of integers generated from the reversed table.
    """
    T = RevTable(t)
    return [T(2 * n + 1, n) for n in range(size)]


def Rev_PosHalf(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions for reversed elements of a table.

    Args:
        t (Table): The table object containing elements to be reversed.
        size (int, optional): The number of elements to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions for the reversed elements.
    """
    return [PolyFrac(t.rev(n),  2) for n in range(size)]


def Rev_NegHalf(t: Table, size: int = 28) -> list[int]:
    """
    Generate a list of polynomial fractions with a negative half exponent.

    This function takes a Table object and generates a list of polynomial fractions
    with an exponent of -2 for each element in the table, reversed up to the specified size.

    Args:
        t (Table): The table object containing the elements to be processed.
        size (int, optional): The number of elements to process. Defaults to 28.

    Returns:
        list[int]: A list of polynomial fractions with a negative half exponent.
    """
    return [PolyFrac(t.rev(n), -2) for n in range(size)]


def Rev_TransNat0(t: Table, size: int = 28) -> list[int]:
    """
    Reverse the given table and transform its elements.

    This function takes a table `t`, reverses it using the `RevTable` function,
    and then applies a transformation to its elements using the `trans` method.
    The transformation applied is the identity function (i.e., each element is
    mapped to itself).

    Args:
        t (Table): The table to be reversed and transformed.
        size (int, optional): The size parameter to be passed to the `trans` method. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    """
    T = RevTable(t)
    return T.trans(lambda k: k, size)


def Rev_TransNat1(t: Table, size: int = 28) -> list[int]:
    """
    Reverse the given table and transform its elements by adding 1.

    Args:
        t (Table): The table to be reversed and transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    """
    T = RevTable(t)
    return T.trans(lambda k: k + 1, size)


def Rev_TransSqrs(t: Table, size: int = 28) -> list[int]:
    """
    Applies a transformation to the given table by reversing it and then squaring each element.

    Args:
        t (Table): The input table to be transformed.
        size (int, optional): The size parameter for the transformation. Defaults to 28.

    Returns:
        list[int]: A list of integers resulting from the transformation.
    """
    T = RevTable(t)
    return T.trans(lambda k: k * k, size)


# sum((-1)**(n-k)*Binomial(n,k)*Trev(n, k) for k in range(n+1)) for n in range(size)])


"""The basic construction is a map
    (Table:Class, Trait:Function) -> (Anum:Url, TreatInfo:TeXString)
"""

# Useful for the LaTeX titels: https://latexeditor.lagrida.com/

TraitInfo: TypeAlias = Tuple[trait, int, str]

'''The dictionary of all traits with their respective functions and TeX strings.
   The size of the table is set to 7, 9 or 28 rows for the default case.
   It is mandatory that this dictionary starts with the key 'Triangle'!
'''
AllTraits: dict[str, TraitInfo] = {
    "Triangle     ": (Triangle,  7, r"\(T_{n,k}\)"),
    "Tinv         ": (Tinv,      7, r"\(T^{-1}_{n,k}\)"),
    "Trev         ": (Trev,      7, r"\(T_{n,n-k}\)"),
    "Tinvrev      ": (Tinvrev,   7, r"\((T_{n,n-k})^{-1}\)"),
    "Toff11       ": (Toff11,    7, r"\(T_{n+1,k+1} \)"),
    "Trev11       ": (Trev11,    7, r"\(T_{n+1,n-k+1} \)"),
    "Tinv11       ": (Tinv11,    7, r"\(T^{-1}_{n+1,k+1}\)"),
    "Tinvrev11    ": (Tinvrev11, 7, r"\((T_{n+1,n-k+1})^{-1}\)"),
    "Tantidiag    ": (Tantidiag, 9, r"\(T_{n-k,k}\ \ (k \le n/2)\)"),
    "Tacc         ": (Tacc,      7, r"\(\sum_{j=0}^{k} T_{n,j}\)"),
    "Talt         ": (Talt,      7, r"\(T_{n,k}\ (-1)^{k}\)"),
    "Tder         ": (Tder,      7, r"\(T_{n+1,k+1}\ (k+1) \)"),
    "TablCol0     ": (TablCol0,  28, r"\(T_{n  ,0}\)"),
    "TablCol1     ": (TablCol1,  28, r"\(T_{n+1,1}\)"),
    "TablCol2     ": (TablCol2,  28, r"\(T_{n+2,2}\)"),
    "TablCol3     ": (TablCol3,  28, r"\(T_{n+3,3}\)"),
    "TablDiag0    ": (TablDiag0, 28, r"\(T_{n  ,n}\)"),
    "TablDiag1    ": (TablDiag1, 28, r"\(T_{n+1,n}\)"),
    "TablDiag2    ": (TablDiag2, 28, r"\(T_{n+2,n}\)"),
    "TablDiag3    ": (TablDiag3, 28, r"\(T_{n+3,n}\)"),
    "TablLcm      ": (TablLcm,   28, r"\(\text{lcm}_{k=0}^{n}\ |T_{n,k}|\ (T_{n,k}>1)\)"),
    "TablGcd      ": (TablGcd,   28, r"\(\text{gcd}_{k=0}^{n}\ |T_{n,k}|\ (T_{n,k}>1)\)"),
    "TablMax      ": (TablMax,   28, r"\(\text{max}_{k=0}^{n}\ |T_{n,k}|\)"),
    "TablSum      ": (TablSum,   28, r"\(\sum_{k=0}^{n} T_{n,k}\)"),
    "EvenSum      ": (EvenSum,   28, r"\(\sum_{k=0}^{n} T_{n,k}\ [2|k]\)"),
    "OddSum       ": (OddSum,    28, r"\(\sum_{k=0}^{n} T_{n,k}\ (1-[2|k])\)"),
    "AltSum       ": (AltSum,    28, r"\(\sum_{k=0}^{n} T_{n,k}\ (-1)^{k}\)"),
    "AbsSum       ": (AbsSum,    28, r"\(\sum_{k=0}^{n} | T_{n,k} |\)"),
    "AccSum       ": (AccSum,    28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k} T_{n,j}\)"),
    "AccRevSum    ": (AccRevSum, 28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k} T_{n,n-j}\)"),
    "AntiDSum     ": (AntiDSum,  28, r"\(\sum_{k=0}^{n/2} T_{n-k, k}\)"),
    "ColMiddle    ": (ColMiddle, 28, r"\(T_{n, n / 2}\)"),
    "CentralE     ": (CentralE,  28, r"\(T_{2 n, n}\)"),
    "CentralO     ": (CentralO,  28, r"\(T_{2 n + 1, n}\)"),
    "PosHalf      ": (PosHalf,   28, r"\(\sum_{k=0}^{n}T_{n,k}\ 2^{n-k} \)"),
    "NegHalf      ": (NegHalf,   28, r"\(\sum_{k=0}^{n}T_{n,k}\ (-2)^{n-k} \)"),
    "TransNat0    ": (TransNat0, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ k\)"),
    "TransNat1    ": (TransNat1, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ (k+1)\)"),
    "TransSqrs    ": (TransSqrs, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ k^{2}\)"),
    "BinConv      ": (BinConv,   28, r"\(\sum_{k=0}^{n}T_{n,k}\ \binom{n}{k} \)"),
    "InvBinConv   ": (InvBinConv, 28, r"\(\sum_{k=0}^{n}T_{n,k}\ (-1)^{n-k}\ \binom{n}{k}\)"),
    "PolyRow1     ": (PolyRow1,  28, r"\(\sum_{k=0}^{1}T_{1,k}\ n^k\)"),
    "PolyRow2     ": (PolyRow2,  28, r"\(\sum_{k=0}^{2}T_{2,k}\ n^k\)"),
    "PolyRow3     ": (PolyRow3,  28, r"\(\sum_{k=0}^{3}T_{3,k}\ n^k\)"),
    "PolyCol2     ": (PolyCol2,  28, r"\(\sum_{k=0}^{n}T_{n,k}\ 2^k\)"),
    "PolyCol3     ": (PolyCol3,  28, r"\(\sum_{k=0}^{n}T_{n,k}\ 3^k\)"),
    "PolyDiag     ": (PolyDiag,  28, r"\(\sum_{k=0}^{n}T_{n,k}\ n^k\)"),
    "RevToff11    ": (Rev_Toff11,    7, r"\(T_{n+1,n-k} \)"),
    "RevTrev11    ": (Rev_Trev11,    7, r"\(T_{n+1,n-k} \)"),
    "RevTinv11    ": (Rev_Tinv11,    7, r"\(T^{-1}_{n+1,n-k}\)"),
    "RevTantidiag ": (Rev_Tantidiag, 9, r"\(T_{n-k,n-2k}\ \ (k \le n/2)\)"),
    "RevTacc      ": (Rev_Tacc,      7, r"\(\sum_{j=0}^{n-k}T_{n,n-j}\)"),
    "RevTalt      ": (Rev_Talt,      7, r"\(T_{n,n-k}\ (-1)^{n-k}\)"),
    "RevTder      ": (Rev_Tder,      7, r"\(T_{n+1,n-k}\ (n-k+1) \)"),
    "RevEvenSum   ": (Rev_EvenSum,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ [2|k]\)"),
    "RevOddSum    ": (Rev_OddSum,    28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (1-[2|k])\)"),
    "RevAccRevSum ": (Rev_AccRevSum, 28, r"\(\sum_{k=0}^{n} \sum_{j=0}^{k}T_{n,n-j}\)"),
    "RevAntiDSum  ": (Rev_AntiDSum,  28, r"\(\sum_{k=0}^{n/2}T_{n-k,n-k}\)"),
    "RevColMiddle ": (Rev_ColMiddle, 28, r"\(T_{n,n/2}\)"),
    "RevCentralO  ": (Rev_CentralO,  28, r"\(T_{2n+1,n}\)"),
    "RevPosHalf   ": (Rev_PosHalf,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ 2^{n-k} \)"),
    "RevNegHalf   ": (Rev_NegHalf,   28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (-2)^{n-k} \)"),
    "RevTransNat0 ": (Rev_TransNat0, 28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ k\)"),
    "RevTransNat1 ": (Rev_TransNat1, 28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ (k + 1)\)"),
    "RevTransSqrs ": (Rev_TransSqrs, 28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ k^{2}\)"),
    "RevPolyRow1  ": (Rev_PolyRow1,  28, r"\(\sum_{k=0}^{1}T_{1,n-k}\ n^k\)"),
    "RevPolyRow2  ": (Rev_PolyRow2,  28, r"\(\sum_{k=0}^{2}T_{2,n-k}\ n^k\)"),
    "RevPolyRow3  ": (Rev_PolyRow3,  28, r"\(\sum_{k=0}^{3}T_{3,n-k}\ n^k\)"),
    "RevPolyCol3  ": (Rev_PolyCol3,  28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ 3^k\)"),
    "RevPolyDiag  ": (Rev_PolyDiag,  28, r"\(\sum_{k=0}^{n}T_{n,n-k}\ n^k\)"),
}


def TableTraits(T: Table) -> None:
    """
    Processes and prints traits of a given table.

    Args:
        T (Table): The table object whose traits are to be processed.

    Iterates over all traits in the AllTraits dictionary, constructs a name
    for each trait by combining the table's ID and the trait ID, and prints
    the name and the corresponding trait's TeXed formula. Additionally, converts the
    trait's sequence to a string and prints it.

    The name can be used as a key into the dictionary of T.
    The sequence is converted to a string with a maximum line length of 60 and
    a maximum of 20 terms.

    Returns:
        None
    """
    for trait_id, tr in AllTraits.items():
        name = (T.id + '_' + trait_id).ljust(9 + len(T.id), " ")
        tex = tr[2]
        seq = tr[0](T, tr[1])
        print(name, tex)
        # print(FNVhash(SeqToString(seq, 180, 50, ",", 3, True)))
        print(SeqToString(seq, 60, 20))


if __name__ == "__main__":

    from Abel import Abel                # type: ignore
    from AbelInv import AbelInv          # type: ignore
    from LahInv import LahInv            # type: ignore

    def test(T: Table, LEN: int) -> None:
        print("TablCol")
        for n in range(4):
            print(TablCol(T, n, LEN))
        print("TablDiag")
        for n in range(4):
            print(TablDiag(T, n, LEN))
        print("PolyRow")
        for n in range(4):
            print(PolyRow(T, n, LEN))
        print("PolyCol")
        for n in range(4):
            print(PolyCol(T, n, LEN))
        print()
    
    #test(Abel, 10)
    TableTraits(Abel)
