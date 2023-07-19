from control.control import Control
from module.add import Add
from module.delete import Delete
from module.edit import Edit
from module.exit import Exit
from module.read import Read
from module.save import Save
from module.show import Show


def start(control):
    print('_________МЕНЮ_________\n', ' help - все команды\n')
    while True:
        try:
            key = input('->')
            control.on_execute(key)
        except KeyboardInterrupt:
            print("выход")
            exit()


class View:
    control: Control

    def __init__(self):
        notes = {}
        self.control = Control(notes, [Read('read', 'считать из файла'),
                                       Show('show', 'посмотреть'),
                                       Edit('edit', 'редактировать'),
                                       Add('add', 'добавить'),
                                       Delete('del', 'удалить'),
                                       Save('save', 'сохранить в файл'),
                                       Exit('exit', 'выход')])
        start(self.control)
