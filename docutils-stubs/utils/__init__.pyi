# Stubs for docutils.utils (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import ApplicationError, DataError
from docutils import nodes
from docutils.frontend import Values
from docutils.io import Output
from typing import Any, Dict, Callable, Generator, IO, Iterable, List, Mapping, Optional, Pattern, Tuple, Union

__docformat__: str

class SystemMessage(ApplicationError):
    level: int = ...
    def __init__(self, system_message: nodes.system_message, level: int) -> None: ...

class SystemMessagePropagation(ApplicationError): ...

class Reporter:
    levels: List[str] = ...
    DEBUG_LEVEL: int = ...
    INFO_LEVEL: int = ...
    WARNING_LEVEL: int = ...
    ERROR_LEVEL: int = ...
    SEVERE_LEVEL: int = ...
    source: str = ...
    error_handler: str = ...
    debug_flag: bool = ...
    report_level: int = ...
    halt_level: int = ...
    stream: Optional[Union[IO, str, bool]] = ...
    encoding: str = ...
    observers: List[Callable[[nodes.system_message], None]] = ...
    max_level: int = ...
    def __init__(self, source: str, report_level: int, halt_level: int, stream: Optional[Union[IO, str, bool]] = ..., debug: bool = ..., encoding: Optional[Any] = ..., error_handler: str = ...) -> None: ...
    def set_conditions(self, category: Any, report_level: int, halt_level: int, stream: Optional[IO] = ..., debug: bool = ...) -> None: ...
    def attach_observer(self, observer: Callable[[nodes.system_message], None]) -> None: ...
    def detach_observer(self, observer: Callable[[nodes.system_message], None]) -> None: ...
    def notify_observers(self, message: nodes.system_message) -> None: ...
    def system_message(self, level: int, message: str, *children: nodes.Node, **kwargs: Any) -> nodes.system_message: ...
    def debug(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def info(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def warning(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def error(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...
    def severe(self, *args: Any, **kwargs: Any) -> nodes.system_message: ...

class ExtensionOptionError(DataError): ...
class BadOptionError(ExtensionOptionError): ...
class BadOptionDataError(ExtensionOptionError): ...
class DuplicateOptionError(ExtensionOptionError): ...

def extract_extension_options(field_list: nodes.field_list, options_spec: Dict[str, Callable[[str], Any]]) -> Dict[str, Any]: ...
def extract_options(field_list: nodes.field_list) -> List[Tuple[str, str]]: ...
def assemble_option_dict(option_list: Iterable[Tuple[str, str]], options_spec: Mapping[str, Callable[[str], Any]]) -> Dict[str, Any]: ...

class NameValueError(DataError): ...

def decode_path(path: str) -> str: ...
def extract_name_value(line: str) -> List[Tuple[str, str]]: ...
def new_reporter(source_path: str, settings: Values) -> Reporter: ...
def new_document(source_path: str, settings: Optional[Values] = ...) -> nodes.document: ...
def clean_rcs_keywords(paragraph: nodes.paragraph, keyword_substitutions: List[Tuple[Pattern, str]]) -> None: ...
def relative_path(source: str, target: str) -> str: ...
def get_stylesheet_reference(settings: Values, relative_to: Optional[str] = ...) -> str: ...
def get_stylesheet_list(settings: Values) -> List[str]: ...
def find_file_in_dirs(path: str, dirs: List[str]) -> str: ...
def get_trim_footnote_ref_space(settings: Values) -> bool: ...
def get_source_line(node: nodes.Node) -> Tuple[str, int]: ...
def escape2null(text: str) -> str: ...
def unescape(text: str, restore_backslashes: bool = ..., respect_whitespace: bool = ...) -> str: ...
def split_escaped_whitespace(text: str) -> List[str]: ...
def strip_combining_chars(text: str) -> str: ...
def find_combining_chars(text: str) -> List[int]: ...
def column_indices(text: str) -> List[int]: ...

east_asian_widths: Dict[str, int]

def column_width(text: str) -> int: ...
def uniq(L: List) -> List: ...
def unique_combinations(items: List, n: int) -> Generator[List, None, None]: ...
def normalize_language_tag(tag): ...

class DependencyList:
    def __init__(self, output_file: Optional[str] = ..., dependencies: List[str] = ...) -> None: ...
    list: List[str] = ...
    file: Output = ...
    def set_output(self, output_file: str) -> None: ...
    def add(self, *filenames: str) -> None: ...
    def close(self) -> None: ...

release_level_abbreviations: Dict[str, str]

def version_identifier(version_info: Optional[Tuple[int, int, int, str, int, bool]] = ...) -> str: ...
