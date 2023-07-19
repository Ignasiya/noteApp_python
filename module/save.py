import json
from abc import ABC

from module.menu import Menu


class Save(Menu, ABC):

    def execute(self, note: list):
        with open("data_file.json", "w", encoding="utf-8") as write_file:
            json.dump(note, write_file, default=lambda x: x.__dict__)
