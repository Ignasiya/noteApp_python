from abc import ABC

from module.menu import Menu


class Add(Menu, ABC):

    def execute(self, note: list):
        pass
