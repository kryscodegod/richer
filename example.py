from rich_tabler.main import *


class ExampleTableDemo(TableMaker):
    def __init__(
            self,
            names: StrList,
            container: DictList = None,
            title: str | None = None,
            color: str | None = None,
            ):
        super().__init__(names, container=container, title=title, color=color)

    def __call__(self, mod='default'):
        if mod == 'default':
           console.print(self.get_table())
        else:
            rt()
    
    def __str__(self) -> str:
        return rt.info
    
    
if __name__ == '__main__':
    names = ['id', 'name', 'status']
    content = [{'id': '1', 'name': 'Kristy', 'status': 'author'}]
    ext  = ExampleTableDemo(names, content, title='[magenta]author', color='cyan')
    console.log(ext)
    ext(mod='none')
    ext()