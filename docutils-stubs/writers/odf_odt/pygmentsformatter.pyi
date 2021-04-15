# Stubs for docutils.writers.odf_odt.pygmentsformatter (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import pygments.formatter  # type: ignore
from pygments.token import _TokenType  # type: ignore
from typing import Any, Sequence, Tuple, TextIO

class OdtPygmentsFormatter(pygments.formatter.Formatter):
    rststyle_function: Any = ...
    escape_function: Any = ...
    def __init__(self, rststyle_function: Any, escape_function: Any) -> None: ...
    def rststyle(self, name: Any, parameters: Any = ...) -> Any: ...

class OdtPygmentsProgFormatter(OdtPygmentsFormatter):
    def format(self, tokensource: Sequence[Tuple[_TokenType, str]], outfile: TextIO) -> None: ...

class OdtPygmentsLaTeXFormatter(OdtPygmentsFormatter):
    def format(self, tokensource: Sequence[Tuple[_TokenType, str]], outfile: TextIO) -> None: ...
