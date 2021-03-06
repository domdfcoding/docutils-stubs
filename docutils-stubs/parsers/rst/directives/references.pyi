# Stubs for docutils.parsers.rst.directives.references (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils.nodes import Node
from docutils.parsers.rst import Directive
from typing import Any, Callable, Dict, List

__docformat__: str

class TargetNotes(Directive):
    option_spec: Dict[str, Callable[[str], Any]] = ...
    def run(self) -> List[Node]: ...
