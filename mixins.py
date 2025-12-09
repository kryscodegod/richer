from modules import console, dataclass

@dataclass
class RuText:
    info: str = 'Класс для демонстрации примеров создания простых таблиц с помощью данного пакета'
    warn: str = '[red]Ошибка! Неверный формат данных!'
    note: str = '[red]Что-то пошло не так!'
    try_again: str = '[green] Попробуйте ввести данные в формате: [bold yellow]list<tuple>'
    set_data_first: str  = '[green] Введите список названий колонок в формате: [bold yellow]list<str>'
    set_data_second: str = '[green] Затем введите данные для создания столбцов в формате: [bold yellow]list<dict<str, str>>'
    set_data_alt: str = '[green] Вы также можете ввести данные в формате [bold yellow]list<tuple> [green]с методом [blue]create_from_standard_content()'
    set_data_warn: str = '[red]Помните, что  rich.Table принимает только renderable-объекты и строки!'

    def __post_init__(self):
        console.print("\n".join([
            self.set_data_first,
            self.set_data_second,
            self.set_data_alt,
            self.set_data_warn
        ]))
 
rt = RuText

