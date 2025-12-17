from rich_tabler.modules import * # type: ignore
from rich_tabler.mixins import rt # type: ignore
from rich_tabler.custom_types import AnyList, DictList, StrList, Content, Container # type: ignore


class ContentType(BaseModel): # type: ignore
    content: Content

class StandardType(BaseModel): # type: ignore
    any_list: AnyList

class TypeChecker(BaseModel): # type: ignore
    string_list: StrList
    dict_list: DictList


    