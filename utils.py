from rich_tabler.models import * # type: ignore
from loguru import logger
from functools import wraps
from typing import Union, Callable

logger.remove()

logger.add( 
    RichHandler(rich_tracebacks=True, markup=True), # type: ignore
    format = '{message}',
    level='INFO'
    )


stringify = lambda _list: list(map(str, _list))


get_valid_attrs = lambda kwr: {key: value for key, value in kwr.items() if hasattr(Table(), key)} # type: ignore


def checked(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
           
           return func(*args, **kwargs)
        
        except ValidationError: # type: ignore
           logger.debug(f'[red] validation-error in func: [yellow]{func.__name__}')

        except Exception as error_message:
           logger.error(f'[red]WARNING! [green]{error_message}')

    return wrapper

@checked
def check_type(strings: StrList, records: DictList) -> TypeChecker | None: # type: ignore
    return TypeChecker(string_list=strings, dict_list=records) # type: ignore
    
@checked
def check_other_types(strings: AnyList, contents: Content) -> Union[StandardType, ContentType] | None: # type: ignore
    return StandardType(any_list=strings) and ContentType(content=contents) # type: ignore
        
def add_columns(
        cols: StrList, # type: ignore
        table: Table, # type: ignore
        color: str | None = None
        ): # type: ignore
    for cl in cols:
        table.add_column(cl, style=color)
    
def content_handler(
        names: StrList, # type: ignore
        table: Table, # type: ignore
        container: Container, # type: ignore
        color: str | None = None,
            ) -> None:
    
    if check_type(names, container):
        add_columns(names, table, color)

        for item in container:
            table.add_row(*[str(item[i]) for i in names]) # type: ignore

    elif check_other_types(names, container):
        add_columns(names, table, color)
            
        for item in container:
            table.add_row(*stringify(item))

    else:
        console.print(rt.warn) # type: ignore

def content_preview(names: StrList, container: Container,) -> Tree: # type: ignore

        tree = Tree('[magenta]data-preview') # type: ignore

        ls = tree.add('[green]cols-data')

        ls.add(f'[blue]is_list[/]: [red] {isinstance(names, list)}')
        ls.add(f'[blue]is_empty[/]: [red]{False if len(names) else True}')

        cont = tree.add('[green]row_content-data')

        cont.add(('[blue]is_dict-list[/]: [red]'
                  f'{True if check_type(names, container) else False}'))
        cont.add(('[blue]is_list-of-tuple[/]: [red]'
                  f'{True if check_other_types(names, container) else False}'))
        
        end = tree.add('[magenta]result-data')
        
        end.add((f'[cyan]signature: [black]< {" | ".join(names)} >[/]'
                 ' -- [cyan]final-size: [red]'
                 f'{len(container) if isinstance(container, list) else None}'))

        return tree

