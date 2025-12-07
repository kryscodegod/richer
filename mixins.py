from modules import *

@dataclass
class RuText:
    warn: str = '[red]Ошибка! Неверный формат данных!'
    note: str = '[red]Что-то пошло не так!'
    try_again: str = '[green] Попробуйте ввести данные в формате: [bold yellow]list[tuple]'

rt = RuText

