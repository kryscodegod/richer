from rich_tabler.modules import console # type: ignore
from rich_tabler.main import rt, TableMaker # type: ignore
from rich_tabler.utils import all_exceptions # type: ignore
from rich_tabler.custom_types import StrList, DictList, Container # type: ignore


class ExampleTableDemo(TableMaker):
    def __init__(
            self,
            names: StrList,
            container: DictList | None = None,
            title: str | None = None,
            color: str | None = None,
            ):
        super().__init__(names, container=container, title=title, color=color)

    def __call__(self, mod='default'):
        if mod == 'default':
           console.print(self.get_table, justify='center')
        else:
            rt()
    
    def __str__(self) -> str:
        return rt.info
       
def demo() -> None:
    names = ['id', 'name', 'status']
    content = [{'id': 1, 'name': 'Kristy', 'status': 'author'}]
    ext  = ExampleTableDemo(names, content, title='[magenta]author', color='cyan')
    console.log(ext)
    ext(mod='none')
    console.rule('[bold magenta]example-table')
    ext()

@all_exceptions
def example(cols: StrList, rows: Container | None = None) -> None:
    ext  = ExampleTableDemo(cols, rows,
                            title='[blue]example-table',
                            color='green')
    ext()

@all_exceptions
def example_full(cols: StrList , rows: Container | None = None,
                title: str | None = None, border: bool = True) -> None:
    if border:
       my_table = TableMaker(cols, container=rows, title=title).get_table
       console.print(my_table)
    else:
        console.print(TableMaker(cols, container=rows,
                                  title=title, show_edge=False).get_table)
    
if __name__ == '__main__':
    demo()

    