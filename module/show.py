from abc import ABC

from module.menu import Menu


class Show(Menu, ABC):

    def execute(self, note: list):
        pass
