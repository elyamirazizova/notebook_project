import json
import os
from .models import Note

class Storage:
    """Класс для работы с файлом-хранилищем заметок."""

    def __init__(self, filename='notes.json'):
        self.filename = filename

    def read_notes(self):
        """Читает все заметки из файла."""
        # Обработка исключения: файл может не существовать
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                # Преобразуем словари из файла в объекты Note
                return [Note.from_dict(note_data) for note_data in data]
        except FileNotFoundError:
            # Если файла нет, возвращаем пустой список
            return []
        except (json.JSONDecodeError, KeyError) as e:
            # Обработка ошибок поврежденного файла
            print(f"Ошибка при чтении файла: {e}. Возвращен пустой список.")
            return []

    def write_notes(self, notes):
        """Сохраняет список заметок в файл."""
        # Обработка исключения при записи (например, нет прав)
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                # Преобразуем каждый объект Note в словарь
                notes_data = [note.to_dict() for note in notes]
                json.dump(notes_data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")

    def get_next_id(self):
        """Генерирует следующий ID для новой заметки."""
        notes = self.read_notes()
        if not notes:
            return 1
        # Находим максимальный ID среди существующих заметок
        return max(note.note_id for note in notes) + 1