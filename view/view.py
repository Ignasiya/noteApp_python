from control.control import Control
from module.add import Add
from module.delete import Delete
from module.edit import Edit
from module.exit import Exit
from module.read import Read
from module.save import Save
from module.show import Show


class View:
    control: Control

    def __init__(self):
        notes = []
        self.control = Control(notes, {Read('read', 'считать из файла'),
                                       Show('show', 'посмотреть'),
                                       Edit('edit', 'редактировать'),
                                       Add('add', 'добавить'),
                                       Delete('del', 'удалить'),
                                       Save('save', 'сохранить в файл'),
                                       Exit('exit', 'выход')})
        self.start(self.control)

    def start(self, control):
        for m in control.get_menu()
        print("".join(f"{key}{value}" for key, value in control.get_menu().items()))
