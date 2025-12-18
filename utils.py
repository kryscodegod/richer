from loguru import logger
from functools import wraps
from typing import Union, Callable
from rich_tabler.mixins import rt # type: ignore
from rich_tabler.modules import Tree, Table, RichHandler, ValidationError # type: ignore
from rich_tabler.custom_types import AnyList, DictList, StrList, Container # type: ignore
from rich_tabler.models import Content, ContentType, StandardType, TypeChecker # type: ignore

logger.remove()

logger.add( 
    RichHandler(rich_tracebacks=True, markup=True), # type: ignore
    format = '{message}',
    level='INFO'
    )


def checked(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
           return func(*args, **kwargs)
        except ValidationError:...

        except Exception as error_msg:
           logger.error((f'{rt.note}\n[green]exception-type: [red]{error_msg}\n'
                f'[green]in function: [yellow]{func.__name__}'))
           
    return wrapper

@checked
def check_type(strings: StrList, records: DictList) -> TypeChecker | None: # type: ignore
    return TypeChecker(string_list=strings, dict_list=records) # type: ignore
    
@checked
def check_other_types(strings: AnyList, contents: Content) -> Union[StandardType, ContentType] | None: # type: ignore
    return StandardType(any_list=strings) and ContentType(content=contents) # type: ignore
        
def add_content(
        cols: StrList, # type: ignore
        table: Table, # type: ignore
        container: Container, # type: ignore
        content_type: str = 'list_dict',
        color: str | None = None
        ) -> None: 
    
    for col in cols:
        table.add_column(col, style=color)

    if content_type == 'list_dict':
       for item in container:
           table.add_row(*[str(item[i]) for i in cols]) # type: ignore

    elif content_type == 'list_tuple':
        for item in container:
            table.add_row(*list(map(str, item)))

    logger.info(rt.success)

    
def content_handler(
        names: StrList, # type: ignore
        table: Table, # type: ignore
        container: Container, # type: ignore
        color: str | None = None,
            ) -> None:
    
    if check_type(names, container):
        add_content(names, table, container, color=color)
    
    elif check_other_types(names, container):
        add_content(names, table, container, content_type='list_tuple', color=color)

    else:
        logger.error(rt.warn) # type: ignore
        
        
def content_preview(names: StrList, container: Container) -> Tree: # type: ignore

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

