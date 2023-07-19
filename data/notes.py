import datetime


class Note:
    id: int
    _name: str
    _body: str
    _date: str

    def __init__(self, id: int, name: str, body: str, date: str) -> None:
        self.id = id
        self.name = name
        self.body = body
        self.date = date

    def get_id(self) -> int:
        return self.id

    def to_list(self) -> list:
        return [self.id, self.name, self.body, self.date]
