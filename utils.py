from models import *

stringify = lambda _list:[str(x) for x in _list]

@checked
def check_type(strings: StrList, records: DictList) -> bool | None:
    return TypeCheсker(string_list=strings, dict_list=records)
    
@checked
def check_other_types(strings: AnyList, contents: Content) -> bool | None:
    return StandartType(any_list=strings) and ContentType(content=contents)
        
