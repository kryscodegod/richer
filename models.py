from custom_types import *
from mixins import *

from pydantic import BaseModel, ValidationError

class ContentType(BaseModel):
    content: Content

class StandartType(BaseModel):
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
    