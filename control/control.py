class Control:
    menu: dict
    notes: list

    def __init__(self, notes, menu):
        self.notes = notes
        self.menu = menu

    def get_notes(self):
        return self.notes

    def get_menu(self):
        return self.menu

    def on_execute(self, item: str):
        self.menu[item].execute(self.notes)
