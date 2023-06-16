import argparse
from controller import NoteController


def main():
    parser = argparse.ArgumentParser(description='Программа заметки')
    parser.add_argument('--notes-dir', dest='notes_dir', type=str, default='notes', help='Директория для хранения заметок')
    args = parser.parse_args()

    controller = NoteController(args.notes_dir)

    while True:
        command = input('Введите команду (add, edit, delete, list, exit): ')
        if command == 'add':
            controller.add_note_controller()
        elif command == 'edit':
            note_id = input('Введите id заметки для редактирования: ')
            controller.edit_note_controller(note_id)
        elif command == 'delete':
            note_id = input('Введите id заметки для удаления: ')
            controller.delete_note_controller(note_id)
        elif command == 'list':
            date_filter = input('Введите дату для фильтрации заметок (оставьте пустым, чтобы показать все заметки): ')
            controller.list_notes_controller(date_filter)
        elif command == 'exit':
            break
        else:
            print('Неверная команда')


if __name__ == '__main__':
    main()