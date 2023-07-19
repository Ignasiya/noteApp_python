import json

from data.notes import Note

note1 = Note(0, "name", "body")
note2 = Note(1, "заголовок", "тело")
note = [note1, note2]

with open("data_file.json", "w", encoding="utf-8") as write_file:
    json.dump(note, write_file, default=lambda x: x.__dict__)

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
