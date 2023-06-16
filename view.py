class NoteView:
    def get_note_info(self):
        note_id = input('Введите id заметки: ')
        title = input('Введите заголовок заметки: ')
        body = input('Введите текст заметки: ')
        return note_id, title, body

    def list_notes(self, notes):
        if not notes:
            print('Заметок не найдено')
            return
        for note in notes:
            print(f'{note.id}\t{note.created_at}\t{note.title}')

    def show_note_details(self, note):
        print(f'ID: {note.id}')
        print(f'Дата создания: {note.created_at}')
        print(f'Дата изменения: {note.updated_at}')
        print(f'Заголовок: {note.title}')
        print(f'Текст: {note.body}')

    def edit_note_view(self, note):
        print(f'Редактирование заметки {note.id}')
        new_title = input(f'Введите новый заголовок (текущий: {note.title}): ')
        new_body = input(f'Введите новый текст (текущий: {note.body}): ')
        return new_title, new_body

    def show_success_message(self, message):
        print(message)

    def show_error_message(self, message):
        print(f'Ошибка: {message}')
