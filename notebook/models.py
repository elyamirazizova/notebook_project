import json
from datetime import datetime

class Note:
    """Класс, представляющий одну заметку."""

    def __init__(self, note_id, title, message, created_at=None, status="active", priority="medium"):
        self.note_id = note_id
        self.title = title
        self.message = message
        # Если дата не передана, используем текущую
        self.created_at = created_at or datetime.now().isoformat()
        self.status = status  # active, completed
        self.priority = priority  # low, medium, high

    def to_dict(self):
        """Преобразует объект Note в словарь для сохранения в JSON."""
        return {
            'id': self.note_id,
            'title': self.title,
            'message': self.message,
            'created_at': self.created_at,
            'status': self.status,
            'priority': self.priority
        }

    @classmethod
    def from_dict(cls, data):
        """Создает объект Note из словаря (при чтении из JSON)."""
        return cls(
            note_id=data['id'],
            title=data['title'],
            message=data['message'],
            created_at=data['created_at'],
            status=data.get('status', 'active'),
            priority=data.get('priority', 'medium')
        )

    def __str__(self):
        return (f"ID: {self.note_id}\n"
                f"Заголовок: {self.title}\n"
                f"Текст: {self.message}\n"
                f"Дата: {self.created_at}\n"
                f"Статус: {self.status}\n"
                f"Приоритет: {self.priority}\n")