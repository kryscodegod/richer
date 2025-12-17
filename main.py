from rich_tabler.custom_types import Any, AnyList, DictList, StrList, Container # type: ignore
from rich_tabler.mixins import rt # type: ignore
from rich_tabler.modules import Table, Tree, console # type: ignore
from rich_tabler.utils import check_type, check_other_types, content_handler, get_valid_attrs # type: ignore


class TableMaker:
    def __init__(
            self,
            names: StrList,
            container: DictList | None = None,
            title: str | None = None,
            color: str | None = None,
            **kwargs: Any
            ) -> None:
        self.names = names
        self.title = title
        self.container = container or []
        self.table = Table(title=self.title, **get_valid_attrs(kwargs))
        
        content_handler(
            self.names,
            self.table,
            self.container,
            color=color
            ) 
    
    @property
    def get_table(self) -> Table:
        return self.table
    
    @staticmethod
    def content_data_preview(
        names: StrList, 
        container: Container,
        ) -> Tree:

        tree = Tree('[magenta]data-preview')
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

    def __repr__(self) -> str:
        return f'{rt.created}:\n{"\n".join(
            [
                f"columns <name>: {self.names}",
                f"rows <count>: {len(self.container) if self.container else 'empty'}",
                f"title <name>: {self.title if self.title else 'none'}"
            ]
        )}'
    


    
   
    
