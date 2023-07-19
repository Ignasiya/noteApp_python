from abc import ABC

from module.menu import Menu


class Delete(Menu, ABC):

    def execute(self, note: list):
        pass
