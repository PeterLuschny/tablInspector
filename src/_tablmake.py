"""
This script generates a combined 'Tables.py' file by combining the contents of multiple source files located in the 'src' directory. 
It reads the contents of specified source files, filters out the import headers and the 'main' functions, and writes the combined content to 'Tables.py'. The script also sets the recursion limit and the maximum number of digits for integer conversion.
Thus in an application it is suffcient to import the 'Tables.py' file to access all the table functions and utility functions defined in this project.

Attributes:
    - tabl_files (list[str]): List of source file names to be combined.
    - str_tabl_fun (str): String containing the list of table functions to be included in 'Tables.py'.
    - import_header (list[str]): List of import statements to be included at the beginning of 'Tables.py'.
    
Note that reference to modules like sympy, numpy, and scipy are excluded by design.
"""

from os import getcwd
from os.path import join, isfile


tabl_files: list[str] = [
    "_tablinverse.py",
    "_tabltypes.py",
    "_tablutils.py",
    "_tabloeis.py",
    "_tabltraits.py",
    "_tabldatabase.py",
    "_tablstats.py",
    "Abel.py",
    "AbelInv.py",
    "Andre.py",
    "Baxter.py",
    "Bell.py",
    "Bessel.py",
    "BesselInv.py",
    "Bessel2.py",
    "BinaryPell.py",
    "Binomial.py",
    "BinomialInv.py",
    "BinomialBell.py",
    "BinomialCatalan.py",
    "BinomialPell.py",
    "BinomialDiffPell.py",
    "Catalan.py",
    "CatalanInv.py",
    "CatalanPaths.py",
    "CentralCycle.py",
    "CentralFactorial.py",
    "CentralSet.py",
    "CentralSetInv.py",
    "Chains.py",
    "Charlier.py",
    "ChebyshevS.py",
    "ChebyshevT.py",
    "ChebyshevU.py",
    "CompositionLP.py",
    "CompositionAcc.py",
    "CompositionDist.py",
    "CTree.py",
    "Delannoy.py",
    "DelannoyInv.py",
    "DistLattices.py",
    "Divisibility.py",
    "DoublePochhammer.py",
    "DyckPaths.py",
    "DyckPathsInv.py",
    "Entringer.py",
    "Euclid.py",
    "Euler.py",
    "Eulerian.py",
    "Eulerian2.py",
    "EulerianB.py",
    "EulerianZigZag.py",
    "EulerSec.py",
    "EulerTan.py",
    "EytzingerOrder.py",
    "EytzingerPerm.py",
    "FallingFactorial.py",
    "FiboLucas.py",
    "FiboLucasInv.py",
    "FiboLucasRev.py",
    "Fibonacci.py",
    "Fubini.py",
    "FussCatalan.py",
    "Gaussq2.py",
    "Genocchi.py",
    "Harmonic.py",
    "HermiteE.py",
    "HermiteH.py",
    "HyperHarmonic.py",
    "Jacobsthal.py",
    "LabeledGraphs.py",
    "Laguerre.py",
    "Lah.py",
    "Lehmer.py",
    "Leibniz.py",
    "LeibnizTable.py",
    "Levin.py",
    "Lozanic.py",
    "Lucas.py",
    "LucasInv.py",
    "LucasPoly.py",
    "Moebius.py",
    "Monotone.py",
    "Motzkin.py",
    "MotzkinInv.py",
    "MotzkinPoly.py",
    "Narayana.py",
    "Narayana2.py",
    "Naturals.py",
    "Nicomachus.py",
    "NimSum.py",
    "One.py",
    "Ordinals.py",
    "OrderedCycle.py",
    "Parades.py",
    "Partition.py",
    "PartitionAcc.py",
    "PartitionDist.py",
    "PartitionDistSize.py",
    "Pascal.py",
    "PolyaTreeAcc.py",
    "PolyaTree.py",
    "Polygonal.py",
    "PowLaguerre.py",
    "Powers.py",
    "Rencontres.py",
    "RencontresInv.py",
    "RisingFactorial.py",
    "RootedTree.py",
    "Schroeder.py",
    "SchroederInv.py",
    "SchroederL.py",
    "SchroederP.py",
    "Seidel.py",
    "Sierpinski.py",
    "StirlingCycle.py",
    "StirlingCycle2.py",
    "StirlingCycleB.py",
    "StirlingSet.py",
    "StirlingSet2.py",
    "StirlingSetB.py",
    "Sylvester.py",
    "TernaryTrees.py",
    "WardSet.py",
    "WardCycle.py",
    "Worpitzky.py",
    "NumBell.py",
    "NumBernoulli.py",
    "NumDivisors",
    "NumEuler.py",
    "NumEulerPhi.py",
    "NumMotzkin.py",
    "NumPartLists.py",
    "NumParts.py",
    "NumRiordan.py",
    "_tablmake.py",
    "_tablinteractive.py",
]

tabl_dict: str = """\
TablesDict: dict[str, Table] = {
    'Abel': Abel,
    'AbelInv': AbelInv,
    'Andre': Andre,
    'Baxter': Baxter,
    'Bell': Bell,
    'Bessel': Bessel,
    'BesselInv': BesselInv,
    'Bessel2': Bessel2,
    'BinaryPell': BinaryPell,
    'Binomial': Binomial,
    'BinomialInv': BinomialInv,
    'BinomialBell': BinomialBell,
    'BinomialCatalan': BinomialCatalan,
    'BinomialPell': BinomialPell,
    'BinomialDiffPell': BinomialDiffPell,
    'Catalan': Catalan,
    'CatalanInv': CatalanInv,
    'CatalanPaths': CatalanPaths,
    'CentralCycle': CentralCycle,
    'CentralFactorial': CentralFactorial,
    'CentralSet': CentralSet,
    'CentralSetInv': CentralSetInv,
    'Chains': Chains,
    'Charlier': Charlier,
    'ChebyshevS': ChebyshevS,
    'ChebyshevT': ChebyshevT,
    'ChebyshevU': ChebyshevU,
    'CompositionLP': CompositionLP,
    'CompositionAcc': CompositionAcc,
    'CompositionDist': CompositionDist,
    'CTree': CTree,
    'Delannoy': Delannoy,
    'DelannoyInv': DelannoyInv,
    'DistLattices': DistLattices,
    'Divisibility': Divisibility,
    'DoublePochhammer': DoublePochhammer,
    'DyckPaths': DyckPaths,
    'DyckPathsInv': DyckPathsInv,
    'Entringer': Entringer,
    'Euclid': Euclid,
    'Euler': Euler,
    'Eulerian': Eulerian,
    'Eulerian2': Eulerian2,
    'EulerianB': EulerianB,
    'EulerianZigZag': EulerianZigZag,
    'EulerSec': EulerSec,
    'EulerTan': EulerTan,
    'EytzingerOrder': EytzingerOrder,
    'EytzingerPerm': EytzingerPerm,
    'FallingFactorial': FallingFactorial,
    'FiboLucas': FiboLucas,
    'FiboLucasInv': FiboLucasInv,
    'FiboLucasRev': FiboLucasRev,
    'Fibonacci': Fibonacci,
    'Fubini': Fubini,
    'FussCatalan': FussCatalan,
    'Gaussq2': Gaussq2,
    'Genocchi': Genocchi,
    'Harmonic': Harmonic,
    'HermiteE': HermiteE,
    'HermiteH': HermiteH,
    'HyperHarmonic': HyperHarmonic,
    'Jacobsthal': Jacobsthal,
    'LabeledGraphs': LabeledGraphs,
    'Laguerre': Laguerre,
    'Lah': Lah,
    'Lehmer': Lehmer,
    'Leibniz': Leibniz,
    'LeibnizTable': LeibnizTable,
    'Levin': Levin,
    'Lozanic': Lozanic,
    'Lucas': Lucas,
    'LucasInv': LucasInv,
    'LucasPoly': LucasPoly,
    'Moebius': Moebius,
    'Monotone': Monotone,
    'Motzkin': Motzkin,
    'MotzkinInv': MotzkinInv,
    'MotzkinPoly': MotzkinPoly,
    'Narayana': Narayana,
    'Narayana2': Narayana2,
    'Naturals': Naturals,
    'Nicomachus': Nicomachus,
    'NimSum': NimSum,
    'One': One,
    'Ordinals': Ordinals,
    'OrderedCycle': OrderedCycle,
    'Parades': Parades,
    'Partition': Partition,
    'PartitionAcc': PartitionAcc,
    'PartitionDist': PartitionDist,
    'PartitionDistSize': PartitionDistSize,
    'Pascal': Pascal,
    'PolyaTreeAcc': PolyaTreeAcc,
    'PolyaTree': PolyaTree,
    'Polygonal': Polygonal,
    'PowLaguerre': PowLaguerre,
    'Powers': Powers,
    'Rencontres': Rencontres,
    'RencontresInv': RencontresInv,
    'RisingFactorial': RisingFactorial,
    'RootedTree': RootedTree,
    'Schroeder': Schroeder,
    'SchroederInv': SchroederInv,
    'SchroederL': SchroederL,
    'SchroederP': SchroederP,
    'Seidel': Seidel,
    'Sierpinski': Sierpinski,
    'StirlingCycle': StirlingCycle,
    'StirlingCycle2': StirlingCycle2,
    'StirlingCycleB': StirlingCycleB,
    'StirlingSet': StirlingSet,
    'StirlingSet2': StirlingSet2,
    'StirlingSetB': StirlingSetB,
    'Sylvester': Sylvester,
    'TernaryTrees': TernaryTrees,
    'WardSet': WardSet,
    'WardCycle': WardCycle,
    'Worpitzky': Worpitzky,
}\n"""

""" Importet modules:
    os: Provides functions for interacting with the operating system.
    os.path: Provides functions for manipulating file paths.
    functools: Provides higher-order functions for functional programming.
    itertools: Provides functions for creating iterators for efficient looping.
    more_itertools: Provides additional iterator building blocks.
    math: Provides mathematical functions.
    fractions: Provides support for rational number arithmetic.
    operator: Provides functions for standard operators.
    time: Provides time-related functions.
    pathlib: Provides an object-oriented interface for filesystem paths.
    requests: Provides functions for making HTTP requests.
    json: Provides functions for parsing JSON.
    sys: Provides access to system-specific parameters and functions.
    typing: Provides support for type hints.
"""
import_header: list[str] = [
    "from functools import cache\n",
    "from itertools import accumulate, islice\n",
    "from more_itertools import difference, flatten\n",
    "from functools import reduce\n",
    "from math import factorial, sqrt, lcm, gcd\n",
    "from fractions import Fraction\n",
    "import operator\n",
    "from operator import itemgetter\n",
    "import time\n",
    "from pathlib import Path\n",
    "import requests\n",
    "import json\n",
    "from ipywidgets import Dropdown\n",
    "from requests import get\n",
    "from sys import setrecursionlimit, set_int_max_str_digits\n",
    "from typing import Callable, TypeAlias, Iterator, Dict, Tuple, NamedTuple\n",
] 


def MakeTabl() -> None:
    """
    This function generates the 'Tables.py' file by combining the contents
    of multiple source files. It reads the source files from the 'src'
    directory and writes the combined content to 'Tables.py'. The function
    also sets the recursion limit and the maximum number of digits for integer
    conversion.

    Parameters:
    None

    Returns:
    None
    """
    dir = join(getcwd(), "src")
    dest = open(join(dir, "Tables.py"), "w+", encoding="utf-8")

    dest.writelines(import_header)
    dest.write("setrecursionlimit(3000)\n")
    dest.write("set_int_max_str_digits(5000)\n")

    for src in tabl_files:
        if src == "_tablmake.py":
            dest.write(tabl_dict)
            dest.write("TablesList = list(TablesDict.values())\n")
            continue
        print(src)
        file_path: str = join(dir, src)
        if isfile(file_path):
            start: bool = False
            src_file = open(file_path, "r", encoding="utf-8")

            for line in src_file:
                if line.startswith("from"):
                    continue
                if not start:
                    start = line.startswith("@") or line.startswith("# #@")
                    if line.startswith("@"):
                        dest.write(line)
                    continue
                else:
                    start = True
                if line.startswith("#"):
                    continue
                if line.startswith("if __name__"):
                    break
                if line != "\n":
                    dest.write(line)
            src_file.close()
    dest.write("# TablesListPreview()\n")
    dest.close()


if __name__ == "__main__":
    MakeTabl()
