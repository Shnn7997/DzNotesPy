import os
import json
import chardet
from datetime import datetime


class Note:
    def __init__(self, note_id, title, body, created_at=None, updated_at=None):
        self.id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now().strftime('%d.%m.%y %H:%M')
        self.updated_at = updated_at or self.created_at

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class NoteRepository:
    def __init__(self, notes_dir):
        self.notes_dir = notes_dir
        if not os.path.isdir(self.notes_dir):
            os.makedirs(self.notes_dir)

    def _get_note_filename(self, note_id, created_at):
        date = datetime.strptime(created_at, '%d.%m.%y %H:%M')
        filename = f'{note_id}_{date.strftime("%d.%m.%y_%H.%M")}.json'
        return os.path.join(self.notes_dir, filename)

    def create(self, note):
        note_filename = self._get_note_filename(note.id, note.created_at)
        with open(note_filename, 'w', encoding='utf-8') as f:
            json.dump(note.to_dict(), f, ensure_ascii=False, indent=4)

    def read_all(self, date_filter=None):
        note_files = os.listdir(self.notes_dir)
        notes = []
        for filename in note_files:
            if not filename.endswith('.json'):
                continue
            filepath = os.path.join(self.notes_dir, filename)
            with open(filepath, 'r') as f:
                note_data = json.load(f)
                note = Note(
                    note_data.get('id'),
                    note_data.get('title'),
                    note_data.get('body'),
                    note_data.get('created_at'),
                    note_data.get('updated_at')
                )
                if date_filter and note.created_at[:8] != date_filter:
                    continue
                notes.append(note)
        return notes

    def read_by_id(self, note_id):
        note_files = os.listdir(self.notes_dir)
        for filename in note_files:
            if not filename.endswith('.json'):
                continue
            filepath = os.path.join(self.notes_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                note_data = json.load(f)
                if note_data['id'] == note_id:
                    return Note(
                        note_data.get('id'),
                        note_data.get('title'),
                        note_data.get('body'),
                        note_data.get('created_at'),
                        note_data.get('updated_at')
                    )
        return None

    def update(self, note):
        note_filename = self._get_note_filename(note.id, note.created_at)
        with open(note_filename, 'w', encoding='utf-8') as f:
            json.dump(note.to_dict(), f, ensure_ascii=False, indent=4)

    def delete(self, note_id):
        note_files = os.listdir(self.notes_dir)
        for filename in note_files:
            if not filename.endswith('.json'):
                continue
            filepath = os.path.join(self.notes_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                note_data = json.load(f)
                if note_data['id'] == note_id:
                    # закрыть файл
                    f.close()
                    os.remove(filepath)
                    return True
        return False