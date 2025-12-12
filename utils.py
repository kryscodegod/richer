from models import *
from loguru import logger
from functools import wraps
from typing import Union, Callable

logger.remove()

logger.add( 
    RichHandler(rich_tracebacks=True, markup=True),
    format = '{message}',
    level='INFO'
    )


stringify = lambda _list: list(map(str, _list))

def checked(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
           logger.info({'run': True, 'file': __name__, 'extensions': None})
           console.print(Panel(f'[blue] execute-function: [red]{func.__name__}'))
           
           return func(*args, **kwargs)
        
        except ValidationError as error_message:
           logger.error(f'[red]WARNING! [green]{error_message}')
    return wrapper

@checked
def check_type(strings: StrList, records: DictList) -> TypeCheсker | None:
    return TypeCheсker(string_list=strings, dict_list=records)
    
@checked
def check_other_types(strings: AnyList, contents: Content) -> Union[StandardType, ContentType] | None:
    return StandardType(any_list=strings) and ContentType(content=contents)
        

def content_handler(
        condition: bool,
        names: StrList,
        table: Table,
        container: DictList,
        color: str | None = None,
            ) -> None | Table:
    
    if condition and check_type(names, container):
         # type: ignore
        for name in names:
            table.add_column(name, style=color)

        for item in container:
            table.add_row(*[str(item[i]) for i in names])

    elif condition and check_other_types(names, container):
         # type: ignore
        for name in names:
            table.add_column(name, style=color)
            
        for item in container:
            table.add_row(*stringify(item))

        return table # type: ignore
    
    else:
        console.print(rt.warn)


