from utils import *

class TableMaker:
    def __init__(
            self,
            names: StrList,
            container: DictList = None,
            title: str | None = None,
            color: str | None = None,
            ):
        self.names = names
        self.title = title
        self.container = container
        self.table = Table(title=self.title)
        if self.container and check_type(self.names, self.container):
            for name in self.names:
                self.table.add_column(name, style=color)
            for item in self.container:
                self.table.add_row(*stringify(item.values()))
        else:
            console.print(rt.warn)
    
    def get_table(self) -> Table:
        return self.table
    
    @classmethod
    def create_from_standart_content(
        cls, 
        names: StrList, 
        rows: StrList,
        title: str | None = None,
        color: str | None = None
        ):
        if all([names, rows, check_other_types(names, rows),]):
            table = Table(title=title)
            for name in names:
              table.add_column(name, style=color)
            for item in rows:
              table.add_row(*stringify(item))
            return table
        else:
            console.print(f'{rt.note}\n{rt.try_again}')

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