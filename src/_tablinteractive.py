'''
This module provides interactive tools for looking up sequences in the OEIS database based on table traits.

Functions:
    ILookUp(t: str, tr: str, info: bool = True) -> int:
        Look up the A-number in the OEIS database based on a trait of a table.
        Same as LookUp in Tables.py, but with input from selectors.
    GetTablSelector() -> Dropdown:
        Returns a dropdown widget for selecting a table.
    GetTraitSelector() -> Dropdown:
        Returns a dropdown widget for selecting a trait.
Modules:
    ipywidgets: Provides interactive HTML widgets for Jupyter notebooks and the IPython kernel.
    Tables: Contains the TraitsDict, TablesDict, and LookUp functions for table and trait management.
'''

from _tabltypes import Table
from _tabldatabase import TraitsDict
from _tabloeis import LookUp
from _tablutils import is_sage_running, NumToAnum, TidToStdFormat
from Tables import TablesDict
from ipywidgets import Dropdown


# #@

    
def ILookUp(t: str, tr: str, info: bool = True) -> int:
    """
    Look up the A-number in the OEIS database based on a trait of a table.

    Args:
        t (str): The name of the table to be analyzed.
        tr (str): The name of a trait that extracts information from the table.
        info (bool, optional): If True, information about the matching will be displayed. Defaults to True.

    Returns:
        int: The A-number of the sequence if found, otherwise 0.
    
    Raises:
        Exception: If the OEIS server cannot be reached after multiple attempts.
        Currently, the function will return -999999 if the OEIS server cannot be reached.
    
    Example:
        >>> LookUp(Fubini, PolyDiag)
        connecting: [0]
        You searched: 1,1,10,219,8676,...
        OEIS-data is: 1,1,10,219,8676,...
        *** Found: A094420 Generalized ordered Bell numbers Bo(n,n).
        Returns the int 94420.
    """
    try:
        T = TablesDict[t]
        TR = TraitsDict[tr][0]
    except KeyError as e: 
        print("KeyError:", e)
        return 0

    if info:
        print('Selected triangle: ' + t) # + "  " + T.tex)
        print('Selected trait:    ' + tr) # + "  " + TraitsDict[tr][2])
        T.show(7)

    num = LookUp(T, TR, info) # type: ignore

    if not info:
        print(f"{TidToStdFormat(T.id)} {T.oeis[0]} -> {NumToAnum(num)}")

    return num

def GetTablSelector():
    return Dropdown(options=[k for k in TablesDict.keys()])

def GetTraitSelector():
    return Dropdown(options=sorted([k for k in TraitsDict.keys()]))


def TablPlot(t: Table | str, size: int, scaled: bool=True) -> None:
    """Plots the first size row polynomials of a table.
    This function can only be used in a SageMath environment.
    If 'scaled'=True, the polynomials are scaled by the factorial of the row index.
    """
    if size <= 0 or size > 10:
        print(f"Size must be in the range 1-10, but was {size}.")
        return

    if not is_sage_running():
        print("This function can only be used in a SageMath environment.")
        return

    from sage.all import var, plot, show, factorial

    try:
        T = TablesDict[t] if isinstance(t, str) else t 
    except KeyError as e: 
        print("KeyError:", e)
        return

    # RGB = [(102, 163, 202), (93, 158, 199), (235, 98, 53), (143, 176, 50), (135, 120, 179), (225, 156, 36), (94, 129, 181), (197, 110, 26), (255, 192, 3), (166, 97, 158)]
    
    C = ['green', 'blue', 'violet', 'sienna', 'plum', 'springgreen', 'chocolate', 'crimson', 'red', 'black']
    sv = var('sv') 

    if scaled:
        pol = [T.poly(n, sv)/factorial(n) for n in range(1, size + 1)]  # type: ignore
        s = '(scaled)'
    else:
        pol = [T.poly(n, sv) for n in range(1, size + 1)]  # type: ignore
        s = ''

    a = plot([], figsize=(5, 5), title=f"{T.id} Polynomials {s}")
    for c, p in enumerate(pol):  # type: ignore
        a += plot(p, sv, (-1, 1), color=C[c], legend_label=f"p{c+1}")
    show(a)


if __name__ == "__main__":

    #ILookUp("SchroederInv", "TablSum")
    TablPlot("Hans", 8)
