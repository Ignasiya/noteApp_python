from abc import ABC

from module.menu import Menu


class Exit(Menu, ABC):

    def execute(self, note: list):
        SystemExit()
