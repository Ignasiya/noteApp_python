from abc import ABC

import tabulate

from module.menu import Menu


class Show(Menu, ABC):

    def execute(self, notes: list):
        result = []
        for m in notes:
            result.append(m.to_list())
        print(tabulate.tabulate(result))
        return notes
