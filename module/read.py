import json
from abc import ABC

from data.notes import Note
from module.menu import Menu


class Read(Menu, ABC):

    def execute(self, note: dict):
        with open("data_file.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
            result = {}
            for j in data:
                try:
                    note = Note(j['id'], j['name'], j['body'], j['date'])
                    result[note.get_id()] = note
                except AttributeError:
                    print("Неверная структура")
        return result
