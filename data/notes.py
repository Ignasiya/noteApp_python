import datetime


class Note:
    id: int
    _name: str
    _body: str
    _date: str

    # def __init__(self, id: int, name: str, body: str) -> None:
    #     self.id = id + 1
    #     self.name = name
    #     self.body = body
    #     self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self, id: int, name: str, body: str, date: str) -> None:
        self.id = id + 1
        self.name = name
        self.body = body
        self.date = date

    def get_id(self) -> int:
        return self.id