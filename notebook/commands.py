from .storage import Storage

class CommandHandler:
    """Обработчик команд для менеджера заметок."""

    def __init__(self):
        self.storage = Storage()

    def add_note(self, title, message, priority="medium"):
        """Добавляет новую заметку."""
        notes = self.storage.read_notes()
        new_id = self.storage.get_next_id()
        new_note = Note(new_id, title, message, priority=priority)
        notes.append(new_note)
        self.storage.write_notes(notes)
        print(f"Заметка добавлена с ID: {new_id}")

    def list_notes(self, status=None, priority=None):
        """Выводит список всех заметок с возможной фильтрацией."""
        notes = self.storage.read_notes()

        # Применяем фильтры, если они заданы
        if status:
            notes = [note for note in notes if note.status == status]
        if priority:
            notes = [note for note in notes if note.priority == priority]

        if not notes:
            print("Заметок не найдено.")
        else:
            for note in notes:
                print(note)
                print("-" * 20)

    def search_notes(self, keyword):
        """Ищет заметки по ключевому слову в заголовке и тексте."""
        notes = self.storage.read_notes()
        found_notes = []
        # Поиск без учета регистра
        keyword_lower = keyword.lower()
        for note in notes:
            if (keyword_lower in note.title.lower() or
                    keyword_lower in note.message.lower()):
                found_notes.append(note)

        if not found_notes:
            print(f"Заметки по запросу '{keyword}' не найдены.")
        else:
            print(f"Найдено заметок: {len(found_notes)}")
            for note in found_notes:
                print(note)
                print("-" * 20)

    def delete_note(self, note_id):
        """Удаляет заметку по ID."""
        notes = self.storage.read_notes()
        # Ищем заметку для удаления
        for i, note in enumerate(notes):
            if note.note_id == note_id:
                deleted_note = notes.pop(i)
                self.storage.write_notes(notes)
                print(f"Заметка с ID {note_id} удалена.")
                return
        # Если не нашли
        print(f"Заметка с ID {note_id} не найдена.")