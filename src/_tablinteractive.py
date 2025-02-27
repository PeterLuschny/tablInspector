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

from Tables import TraitsDict, TablesDict, LookUp
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
    T = TablesDict[t]
    TR = TraitsDict[tr][0]
    print('Selected triangle: ' + t) # + "  " + T.tex)
    T.show(7)
    print('Selected trait:    ' + tr) # + "  " + TraitsDict[tr][2])
    return LookUp(T, TR, info)

def GetTablSelector():
    return Dropdown(options=[k for k in TablesDict.keys()])

def GetTraitSelector():
    return Dropdown(options=sorted([k for k in TraitsDict.keys()]))
