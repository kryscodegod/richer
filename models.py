from modules import *
from mixins import rt
from custom_types import AnyList, DictList, StrList, Content, Union, Callable


class ContentType(BaseModel):
    content: Content

class StandardType(BaseModel):
    any_list: AnyList

class TypeCheсker(BaseModel):
    string_list: StrList
    dict_list: DictList

def checked(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError:
           console.print(rt.warn)
    return wrapper
    