from rich_tabler.mixins import rt # type: ignore
from rich_tabler.modules import Table, Tree # type: ignore
from rich_tabler.custom_types import Any, DictList, StrList, Container # type: ignore
from rich_tabler.utils import content_handler, content_preview # type: ignore


class TableMaker:
    def __init__(
            self,
            names: StrList,
            container: DictList | None = None,
            title: str | None = None,
            color: str | None = None,
            **kwargs: Any
            ) -> None:
        
        kwargs = {key: value for key, value in kwargs.items() if hasattr(Table(), key)}

        self.names = names
        self.title = title

        self.container = container or []
        self.table = Table(title=self.title, **kwargs)

        content_handler(self.names, self.table, self.container, color=color) 
    
    @property
    def get_table(self) -> Table:
        return self.table
    
    @staticmethod
    def pre(names: StrList, container: Container) -> Tree:
        return content_preview(names, container)
        

    def __repr__(self) -> str:
        return f'{rt.created}:\n{"\n".join(
            [
                f"columns <name>: {self.names}",
                f"rows <count>: {len(self.container) if self.container else 'empty'}",
                f"title <name>: {self.title if self.title else 'none'}"
            ]
        )}'
    


    
   
    
