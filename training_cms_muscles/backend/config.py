import os

# ... (остальной код Config) ...

# Определяем базовую директорию проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Если запущено на Render, там будет переменная окружения RENDER.
# Render также смонтирует наш диск в папку '/data'.
# Создаём итоговый путь к файлу базы данных.
if os.environ.get('RENDER'):
    DB_PATH = '/data/database.db'
else:
    DB_PATH = os.path.join(BASE_DIR, 'database.db')
