import argparse
from notebook.commands import CommandHandler

def main():
    parser = argparse.ArgumentParser(description='Утилита для управления заметками')
    # Создаем субпарсеры для разных команд
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')

    # Команда добавления
    parser_add = subparsers.add_parser('add', help='Добавить новую заметку')
    parser_add.add_argument('--title', required=True, help='Заголовок заметки')
    parser_add.add_argument('--msg', required=True, help='Текст заметки')
    parser_add.add_argument('--priority', choices=['low', 'medium', 'high'],
                           default='medium', help='Приоритет заметки')

    # Команда списка
    parser_list = subparsers.add_parser('list', help='Показать все заметки')
    parser_list.add_argument('--status', choices=['active', 'completed'],
                            help='Фильтр по статусу')
    parser_list.add_argument('--priority', choices=['low', 'medium', 'high'],
                            help='Фильтр по приоритету')

    # Команда поиска
    parser_search = subparsers.add_parser('search', help='Найти заметки по ключевому слову')
    parser_search.add_argument('keyword', help='Ключевое слово для поиска')

    # Команда удаления
    parser_delete = subparsers.add_parser('delete', help='Удалить заметку по ID')
    parser_delete.add_argument('note_id', type=int, help='ID заметки для удаления')

    args = parser.parse_args()
    handler = CommandHandler()

    # Вызов соответствующей функции в зависимости от команды
    if args.command == 'add':
        handler.add_note(args.title, args.msg, args.priority)
    elif args.command == 'list':
        handler.list_notes(status=args.status, priority=args.priority)
    elif args.command == 'search':
        handler.search_notes(args.keyword)
    elif args.command == 'delete':
        handler.delete_note(args.note_id)
    else:
        # Если команда не передана, показываем справку
        parser.print_help()

if __name__ == '__main__':
    main()