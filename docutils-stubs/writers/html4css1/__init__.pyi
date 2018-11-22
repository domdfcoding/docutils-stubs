# Stubs for docutils.writers.html4css1 (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes, writers
from docutils.writers import _html_base
from typing import Any, Dict, List, Tuple, Type

__docformat__: str

class Writer(writers._html_base.Writer):
    supported: Tuple[str, ...] = ...
    default_stylesheets: List[str] = ...
    default_stylesheet_dirs: List[str] = ...
    default_template: str = ...
    default_template_path: str = ...
    settings_spec: Tuple[str, Any, Tuple[Tuple[str, List[str], Dict[str, Any]], ...]] = ...
    config_section: str = ...
    parts: Dict[Any, Any] = ...
    translator_class: Type[HTMLTranslator] = ...
    def __init__(self) -> None: ...

class HTMLTranslator(writers._html_base.HTMLTranslator):
    doctype: str = ...
    content_type: str = ...
    content_type_mathml: str = ...
    special_characters: Dict[int, str] = ...
    attribution_formats: Dict[str, Tuple[str, str]] = ...
    def set_first_last(self, node: nodes.Node) -> None: ...
    def visit_address(self, node: nodes.address) -> None: ...
    def visit_admonition(self, node: nodes.admonition) -> None: ...
    def visit_author(self, node: nodes.author) -> None: ...
    author_in_authors: bool = ...
    def depart_author(self, node: nodes.author) -> None: ...
    def visit_authors(self, node: nodes.authors) -> None: ...
    def depart_authors(self, node: nodes.authors) -> None: ...
    def visit_colspec(self, node: nodes.colspec) -> None: ...
    def depart_colspec(self, node: nodes.colspec) -> None: ...
    def is_compactable(self, node: nodes.Node) -> bool: ...
    def visit_citation(self, node: nodes.citation) -> None: ...
    def depart_citation(self, node: nodes.citation) -> None: ...
    def visit_classifier(self, node: nodes.classifier) -> None: ...
    def visit_definition(self, node: nodes.definition) -> None: ...
    def visit_definition_list(self, node: nodes.definition_list) -> None: ...
    def visit_description(self, node: nodes.description) -> None: ...
    def depart_description(self, node: nodes.description) -> None: ...
    in_docinfo: bool = ...
    def visit_docinfo(self, node: nodes.docinfo) -> None: ...
    docinfo: List[str] = ...
    body: List[str] = ...
    def depart_docinfo(self, node: nodes.docinfo) -> None: ...
    def visit_docinfo_item(self, node: nodes.Node, name: str, meta: bool = ...) -> None: ...
    def depart_docinfo_item(self) -> None: ...
    def visit_doctest_block(self, node: nodes.doctest_block) -> None: ...
    def visit_entry(self, node: nodes.entry) -> None: ...
    compact_p: Any = ...
    compact_simple: bool = ...
    def visit_enumerated_list(self, node: nodes.enumerated_list) -> None: ...
    def depart_enumerated_list(self, node: nodes.enumerated_list) -> None: ...
    def visit_field(self, node: nodes.field) -> None: ...
    def depart_field(self, node: nodes.field) -> None: ...
    def visit_field_body(self, node: nodes.field_body) -> None: ...
    def depart_field_body(self, node: nodes.field_body) -> None: ...
    compact_field_list: bool = ...
    def visit_field_list(self, node: nodes.field_list) -> None: ...
    def depart_field_list(self, node: nodes.field_list) -> None: ...
    def visit_field_name(self, node: nodes.field_name) -> None: ...
    def depart_field_name(self, node: nodes.field_name) -> None: ...
    def visit_footnote(self, node: nodes.footnote) -> None: ...
    def footnote_backrefs(self, node: nodes.Node) -> None: ...
    def depart_footnote(self, node: nodes.footnote) -> None: ...
    def visit_footnote_reference(self, node: nodes.footnote_reference) -> None: ...
    def depart_footnote_reference(self, node: nodes.footnote_reference) -> None: ...
    def visit_generated(self, node: nodes.generated) -> None: ...
    object_image_types: Dict[str, str] = ...
    def visit_label(self, node: nodes.label) -> None: ...
    def depart_label(self, node: nodes.label) -> None: ...
    def visit_list_item(self, node: nodes.list_item) -> None: ...
    def visit_literal(self, node: nodes.literal) -> None: ...
    def visit_literal_block(self, node: nodes.literal_block) -> None: ...
    def depart_literal_block(self, node: nodes.literal_block) -> None: ...
    def visit_option_group(self, node: nodes.option_group) -> None: ...
    def depart_option_group(self, node: nodes.option_group) -> None: ...
    def visit_option_list(self, node: nodes.option_list) -> None: ...
    def depart_option_list(self, node: nodes.option_list) -> None: ...
    def visit_option_list_item(self, node: nodes.option_list_item) -> None: ...
    def depart_option_list_item(self, node: nodes.option_list_item) -> None: ...
    def should_be_compact_paragraph(self, node: nodes.Node) -> bool: ...
    def visit_paragraph(self, node: nodes.paragraph) -> None: ...
    def depart_paragraph(self, node: nodes.paragraph) -> None: ...
    in_sidebar: bool = ...
    def visit_sidebar(self, node: nodes.sidebar) -> None: ...
    def visit_subscript(self, node: nodes.subscript) -> None: ...
    def depart_subscript(self, node: nodes.subscript) -> None: ...
    in_document_title: int = ...
    def visit_subtitle(self, node: nodes.subtitle) -> None: ...
    subtitle: List[str] = ...
    def depart_subtitle(self, node: nodes.subtitle) -> None: ...
    def visit_superscript(self, node: nodes.superscript) -> None: ...
    def depart_superscript(self, node: nodes.superscript) -> None: ...
    def visit_system_message(self, node: nodes.system_message) -> None: ...
    def visit_table(self, node: nodes.table) -> None: ...
    def depart_table(self, node: nodes.table) -> None: ...
    def visit_tbody(self, node: nodes.tbody) -> None: ...
    def depart_tbody(self, node: nodes.tbody) -> None: ...
    def visit_thead(self, node: nodes.thead) -> None: ...
    def depart_thead(self, node: nodes.thead) -> None: ...

class SimpleListChecker(writers._html_base.SimpleListChecker):
    def visit_list_item(self, node: nodes.list_item) -> None: ...
    def visit_definition_list(self, node: nodes.definition_list) -> None: ...
    def visit_docinfo(self, node: nodes.docinfo) -> None: ...
    def visit_definition_list(self, node: nodes.definition_list) -> None: ...
