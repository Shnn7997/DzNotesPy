from datetime import datetime
from model import Note, NoteRepository
from view import NoteView


class NoteController:
    def __init__(self, notes_dir):
        self.model = NoteRepository(notes_dir)
        self.view = NoteView()

    def add_note_controller(self):
        note_id = input('Введите id заметки: ')
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        created_at = datetime.now().strftime('%d.%m.%y %H:%M')
        note = Note(note_id, title, body, created_at=created_at)
        self.model.create(note)
        self.view.show_success_message('Заметка успешно сохранена')

    def edit_note_controller(self, note_id):
        note = self.model.read_by_id(note_id)
        if note:
            new_title, new_body = self.view.edit_note_view(note)
            note.title = new_title or note.title
            note.body = new_body or note.body
            note.updated_at = datetime.now().strftime('%d.%m.%y %H:%M')
            self.model.update(note)
            self.view.show_success_message(f'Заметка с id {note_id} успешно обновлена')
        else:
            self.view.show_error_message(f'Заметка с id {note_id} не найдена')

    def delete_note_controller(self, note_id):
        deleted = self.model.delete(note_id)
        if deleted:
            self.view.show_success_message(f'Заметка с id {note_id} успешно удалена')
        else:
            self.view.show_error_message(f'Заметка с id {note_id} не найдена')

    def list_notes_controller(self, date_filter=None):
        notes = self.model.read_all(date_filter)
        self.view.list_notes(notes)
        if notes:
            note_id = input('Введите id заметки для просмотра деталей (оставьте пустым для выхода): ')
            if note_id:
                self.show_note_details_controller(note_id)

    def show_note_details_controller(self, note_id):
        note = self.model.read_by_id(note_id)
        if note:
            self.view.show_note_details(note)
        else:
            self.view.show_error_message(f'Заметка с id {note_id} не найдена')