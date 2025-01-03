"""
This module provides utility functions and classes for working with tables and measuring generating time.
Functions:
    SeqToString(seq: list[int], maxchars: int, maxterms: int, sep: str = ' ', offset: int = 0, absval: bool = False) -> str:
        Converts a sequence of integers into a string representation.
    TableGenerationTime(tabl: Table, size: int = 100) -> None:
        Measures and prints the time taken to generate the table of the given triangle.
    TimeIncrease(T: Callable[[int, int], int], offset: int = 4, size: int = 5) -> list[float]:
        Computes the relative increase of time generating a triangle when the number of rows doubles.
    SimilarsList() -> list[str]:
        Collects and returns a sorted list of the A-numbers included in the list of 'similars' for all tables in TablesList.
    IsSimilarTriangleInLib(anum: str) -> bool:
        Checks if a triangle similar to the A-number referenced is in the library.
    QuickTablesDisplay(prompt: bool = False) -> None:
        Iterates through the TablesList and displays a quick view of the tables.
    fnv(data: bytes) -> int:
        Calculates the FNV-1a hash value for the given data.
    FNVhash(seq: str) -> str:
        Returns the fnv-hash of a string (representing an integer sequence).
Classes:
    StopWatch
"""

from _tabltypes import Table
from typing import Callable
import time

# #@


def fnv(data: bytes) -> int:
    """
    This function calculates the FNV-1a hash value for the given data.

    Args:
        data (bytes): The input data to be hashed.

    Returns:
        int: The calculated hash value.
   """
    assert isinstance(data, bytes)

    hval = 0xCBF29CE484222325
    for byte in data:
        hval ^= byte
        hval *= 0x100000001B3
        hval &= 0xFFFFFFFFFFFFFFFF
    return hval


def FNVhash(seq: str) -> str:
    """Returns the fnv-hash of a string (representing an integer sequence).

    Args:
        seq (list[int]):

    Returns:
        str: The hex value of the hash without the '0x'-head.
    """
    return hex(fnv(bytes(seq, encoding="ascii")))[2:]


def SeqToString(
        seq: list[int],
        maxchars: int,
        maxterms: int,
        sep: str = ' ',
        offset: int = 0,
        absval: bool = False,
    ) -> str:
    """
    Converts a sequence of integers into a string representation.

    Args:
        seq: The sequence of integers to be converted.
        maxchars: The maximum length of the resulting string.
        maxterms: The maximum number of terms included.
        sep: String seperator. Default is ' '.
        offset: The starting index of the sequence. Defaults to 0.
        absval: Use the absolute value of the terms. Defaults to False.

    Returns:
        str: The string representation of the sequence.
    """
    seqstr = ""
    maxt = maxl = 0
    for trm in seq[offset:]:
        maxt += 1
        if maxt > maxterms:
            break
        if absval:
            s = str(abs(trm)) + sep
        else:
            s = str(trm) + sep
        maxl += len(s)
        if maxl > maxchars:
            break
        seqstr += s

    return seqstr

class StopWatch:
    """
    A simple stopwatch utility class to measure elapsed time.
    Attributes:
        start_time (float or None): The start time of the stopwatch.
        text (str): The comment text to display with the elapsed time.
    Methods:
        start() -> None:
            Start the stopwatch. Raises a RuntimeError if the stopwatch 
            is already running.
        stop() -> float:
            Stop the stopwatch and report the elapsed time. 
            Raises a RuntimeError if the stopwatch is not running.
    """
    def __init__(
        self,
        comment: str = "Elapsed time: "
    ) -> None:

        self.start_time = None
        self.text = comment

    def start(self) -> None:
        """Start a new StopWatch"""
        if self.start_time is not None:
            raise RuntimeError("Watch is running. First stop it.")
        self.start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the StopWatch, and report the elapsed time."""
        if self.start_time is None:
            raise RuntimeError("Watch is not running.")

        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None

        print(self.text.rjust(17), "{:0.4f}".format(elapsed_time), "sec")

        return elapsed_time


def TableGenerationTime(tabl: Table, size: int = 100) -> None:
    """
    Measures and prints the time taken to generate the table of the given triangle.

    Args:
        tabl (Table): The triangle whose generating will be timed.
        size (int, optional): The size of the table (number of rows). Defaults to 100.

    Returns:
        None
    """
    t = StopWatch(tabl.id)
    t.start()
    tabl.tab(size)
    t.stop()


def TimeIncrease(
    T: Callable[[int, int], int],
    offset: int = 4,
    size: int = 5
) -> list[float]:
    """Computes the relative increase of time generating a triangle when the number of rows doubles.

    Args:
        T(n, k): function defined for n >= 0 and 0 <= k <= n.
        offset > 0: the power of two where the test starts. Defaults to 4.
        size: the length of test run. Defaults to 5.

    Returns:
        List of quotients of elapsed time when the number of rows of the triangle doubles.

    Example:
        TimeIncrease(lambda n, k: n**k)
    """
    B: list[float] = []
    for s in [2 << n for n in range(offset - 1, offset + size)]:
        t = StopWatch(str(s))
        t.start()
        [[T(n, k) for k in range(n + 1)] for n in range(s)]
        B.append(t.stop())
    return [B[i + 1] / B[i] for i in range(size)]


def SimilarsList() -> list[str]:
    """
    Collects and returns a sorted list of the A-numbers included in the list
    of 'similars' for all tables in TablesList. The collected A-numbers are 
    then sorted and returned as a list (of strings).

    Returns:
        list[str]: A sorted list of A-numbers.
    """
    bag: list[str] = []
    for tab in TablesList:
        for anum in tab.sim:
            bag.append(anum)
    return sorted(bag)


def IsSimilarTriangleInLib(anum: str) -> bool:
    """Is a triangle similar to the A-number referenced in this library?

    Args:
        A-number as string.
    Returns:
        If 'True' a similar triangle is probably implemented.
    """
    return anum in SimilarsList()


def TablesListPreview(prompt: bool = False) -> None:
    """
    Displays a short view of the tables in the TablesList.

    Args:
        prompt (bool): If True, prompts the user to hit Return/Enter 
        after displaying each table. Default is False.
    """
    for T in TablesList:
        print(T.id, T.sim)
        T.show(6)
        if prompt:
            input("Hit Return/Enter > ")


if __name__ == "__main__":
    from Tables import TablesList
    #from Abel import Abel

    def QuickBench() -> None:
        for tabl in TablesList:
            TableGenerationTime(tabl)  # type: ignore

    def OrderBench() -> None:
        for tabl in TablesList:
            print(TimeIncrease(tabl))  # type: ignore

    QuickBench()

    # print(IsSimilarTriangleInLib('A021009'))
    # print(f"\n{len(Tables)} tables tested!\n")
    # print(AnumInListQ("A002426"))
    # print(AnumList())
    #TimeIncrease(lambda n, k: n**k)