from functools import cache
from _tabltypes import Table

"""Template.  This is a demonstration file producing a valid "Table" class.
   The including file should be named "Template.py". the class "Template"
   and the generating function "template" (that should be decorated with "@cache").

   After you have defined the class and the generating function, add the
   name of the file and the name of the class to the lists in the file
   "_tablmake.py". Then run the program "_tablmake.py" to create the file
   "Tables.py" which will contain the new class and function definitions.


[0] [0]
[1] [0, 0]
[2] [0, 0, 0]
[3] [0, 0, 0, 0]
[4] [0, 0, 0, 0, 0]
[5] [0, 0, 0, 0, 0, 0]
[6] [0, 0, 0, 0, 0, 0, 0]
[7] [0, 0, 0, 0, 0, 0, 0, 0]
[8] [0, 0, 0, 0, 0, 0, 0, 0, 0]
[9] [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""

@cache
def template(n: int) -> list[int]:
    if n == 0:
        return [0]

    row = [0]*(n + 1)
    return row


Template = Table(
    template,    # the generating function
    "Template",  # name of the table
    ["A000004"], # similar sequences in OEIS
    "",          # id of inverse sequence if it exists
    r"T(n,k)=0"  # TeX of the defining formula
)


if __name__ == "__main__":
    from _tabldict import InspectTable

    InspectTable(Template)
