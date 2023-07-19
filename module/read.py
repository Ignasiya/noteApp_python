import json
from abc import ABC

from data.notes import Note
from module.menu import Menu


class Read(Menu, ABC):

    def execute(self, notes: list):
        try:
            with open(f"{input('введите имя файла ->')}.json", "r", encoding="UTF-8") as file:
                data = json.load(file)
                result = []
                for j in data:
                    try:
                        notes = Note(j['id'], j['name'], j['body'], j['date'])
                        result.append(notes)
                    except AttributeError:
                        print("неверная структура")
                print("файл загужен успешно")
                return result
        except FileNotFoundError:
            print("нет файла с таким именем")
