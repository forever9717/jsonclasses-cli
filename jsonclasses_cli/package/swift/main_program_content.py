from jsonclasses.cgraph import CGraph
from .import_lines import import_lines
from .string_query import string_query
from .int_query import int_query
from .float_query import float_query
from .bool_query import bool_query
from .sort_order import sort_order
from .data_enum import data_enum
from .data_class import data_class
from .session_items import session_items
from .session import session
from .response import response_struct
from .user_default import user_default
from .session_manager import session_manager
from .sign_out import sign_out
from .request_manager import request_manager
from ...utils.join_lines import join_lines

def main_program_content(cgraph: CGraph) -> str:
    session_classes = session_items(cgraph)
    use_session = len(session_classes) > 0
    return join_lines([
        import_lines(),
        string_query(),
        int_query(),
        float_query(),
        bool_query(),
        # other type queries
        sort_order(),
        *map(lambda e: data_enum(e), cgraph._enum_map.values()),
        *map(lambda c: data_class(c), cgraph._map.values()),
        session(session_classes) if use_session else '',
        response_struct(),
        user_default(),
        session_manager() if use_session else '',
        sign_out(),
        request_manager('http://127.0.0.1:5000', use_session),
    ], 2)
