from abc import ABC

from module.menu import Menu


class Edit(Menu, ABC):

    def execute(self, notes: list):
        pass
