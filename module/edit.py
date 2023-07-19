from abc import ABC

from module.menu import Menu


class Edit(Menu, ABC):

    def execute(self, note: list):
        pass
