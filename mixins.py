from modules import Panel, console, dataclass

@dataclass
class RuText:
    attantion: str = '[yellow]Внимание! [green]Возможно несоответствие типа передаваемых данных ...'
    info: str = 'Класс для демонстрации примеров создания простых таблиц с помощью данного пакета'
    warn: str = '[red]Ошибка! Неверный формат данных!'
    note: str = '[red]Что-то пошло не так!'
    created: str = 'Создана таблица со следующими параметрами'
    attr_not_found: str = 'Не найден метод или свойство'
    invalid_data: str = 'Данные должны быть кортежем строк!'
    try_again: str = '[green] Попробуйте передать в конструктор данные в формате: [bold yellow]list<tuple>'
    set_data_first: str  = '[green] Передайте в конструктор список названий колонок в формате: [bold yellow]list<str>'
    set_data_second: str = '[green] Затем передайте в конструктор данные для создания столбцов в формате: [bold yellow]list<dict<str, str>>'
    set_data_alt: str = '[green] Вы также можете передать в конструктор данные в формате [bold yellow]list<tuple> [green]с методом ~ [bold yellow]create_from_standard_content()'
    set_data_warn: str = '[red] Помните, что  rich.Table принимает только renderable-объекты и строки!'

    def __post_init__(self):
        console.print(Panel("\n".join([
            self.set_data_first,
            self.set_data_second,
            self.set_data_alt,
            self.set_data_warn
        ]), title='[magenta]help'))
 
rt = RuText

