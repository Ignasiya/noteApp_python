import json
from abc import ABC

from module.menu import Menu


class Save(Menu, ABC):

    def execute(self, notes: list):
        if notes:
            with open(f"{input('введите имя файла ->')}.json", "w", encoding="UTF-8") as file:
                file.write(json.dumps(notes, default=lambda x: x.__dict__, ensure_ascii=False))
        else: print("ошибка, база пуста")
        return notes
