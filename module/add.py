from abc import ABC
from datetime import datetime

from data.notes import Note
from module.menu import Menu


class Add(Menu, ABC):

    def execute(self, notes: list):
        name, body = input('введите имя заметки ->'), input('введите описание ->')
        last_id = 0
        if notes: last_id = notes[-1].get_id()
        note = Note(last_id + 1, name, body, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        notes.append(note)
        print('заметка добавлена')
        return notes
