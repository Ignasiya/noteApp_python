import json
from abc import ABC

from module.menu import Menu


class Save(Menu, ABC):

    def execute(self, note: list):
        if note:
            with open("data_file.json", "w", encoding="UTF-8") as file:
                file.write(json.dumps(note, default=lambda x: x.__dict__, ensure_ascii=False))
        else: print("ошибка, база пуста")
