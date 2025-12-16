from custom_types import *
from modules import console
from mixins import rt
from modules import Table
from utils import check_other_types, content_handler


class TableMaker:
    def __init__(
            self,
            names: StrList,
            container: DictList | None = None,
            title: str | None = None,
            color: str | None = None,
            **kwargs: Any
            ):
        valid_attrs = {key: value for key, value in kwargs.items()
            if hasattr(Table(), key)}
        
        self.names = names
        self.title = title
        self.container = container
        self.table = Table(title=self.title, **valid_attrs)

        content_handler(
            self.container,  # type: ignore
            self.names, self.table, self.container,# type: ignore
            color
            )
        
    
    def get_table(self) -> Table:
        return self.table
    
    @classmethod
    def create_from_standard_content(
        cls, 
        names: StrList, 
        rows: Content,
        title: str | None = None,
        color: str | None = None
        ) -> Table | None:
        table = Table(title=title)

        result_tab = content_handler(
            all([names, rows, check_other_types(names, rows)]),
            names, table, rows, color # type: ignore
        )

        return result_tab
    
    def __repr__(self) -> str:
        return f'created table with params:\n{"\n".join(
            [
                f"columns <name>: {self.names}",
                f"rows <count>: {len(self.container) if self.container else 'empty'}",
                f"title <name>: {self.title if self.title else 'none'}"
            ]
        )}'
    

if __name__ == '__main__':
    ...
    