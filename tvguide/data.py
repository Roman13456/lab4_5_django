from datetime import datetime

CHANNELS = [
    {'id': 1, 'name': '1+1', 'country': 'Україна'},
    {'id': 2, 'name': 'Discovery', 'country': 'США'},
    {'id': 3, 'name': 'National Geographic', 'country': 'США'},
    {'id': 4, 'name': 'ICTV', 'country': 'Україна'},
    {'id': 5, 'name': 'СТБ', 'country': 'Україна'},
]

PROGRAMS = [
    {'id': 101, 'title': 'ТСН', 'description': 'Новини дня від 1+1.', 'start_time': datetime(2025, 4, 22, 19, 30), 'end_time': datetime(2025, 4, 22, 20, 15), 'channel_id': 1},
    {'id': 102, 'title': 'Світ навиворіт', 'description': 'Пригоди Дмитра Комарова.', 'start_time': datetime(2025, 4, 22, 20, 15), 'end_time': datetime(2025, 4, 22, 21, 0), 'channel_id': 1},
    {'id': 103, 'title': 'Gold Rush', 'description': 'Пошук золота на Алясці.', 'start_time': datetime(2025, 4, 22, 20, 0), 'end_time': datetime(2025, 4, 22, 21, 0), 'channel_id': 2},
    {'id': 104, 'title': 'Deadliest Catch', 'description': 'Небезпечний вилов крабів.', 'start_time': datetime(2025, 4, 22, 21, 0), 'end_time': datetime(2025, 4, 22, 22, 0), 'channel_id': 2},
    {'id': 105, 'title': 'Explorer', 'description': 'Дослідження світу.', 'start_time': datetime(2025, 4, 22, 21, 0), 'end_time': datetime(2025, 4, 22, 22, 0), 'channel_id': 3},
    {'id': 106, 'title': 'Science of Stupid', 'description': 'Наука дурних вчинків.', 'start_time': datetime(2025, 4, 22, 22, 0), 'end_time': datetime(2025, 4, 22, 22, 30), 'channel_id': 3},
    {'id': 107, 'title': 'Надзвичайні новини', 'description': 'Кримінальні новини.', 'start_time': datetime(2025, 4, 22, 18, 45), 'end_time': datetime(2025, 4, 22, 19, 30), 'channel_id': 4},
    {'id': 108, 'title': 'Дизель Шоу', 'description': 'Гумористичне шоу.', 'start_time': datetime(2025, 4, 22, 19, 30), 'end_time': datetime(2025, 4, 22, 21, 0), 'channel_id': 4},
    {'id': 109, 'title': 'Вікна-Новини', 'description': 'Головні новини дня.', 'start_time': datetime(2025, 4, 22, 22, 0), 'end_time': datetime(2025, 4, 22, 22, 45), 'channel_id': 5},
    {'id': 110, 'title': 'МастерШеф', 'description': 'Кулінарне шоу.', 'start_time': datetime(2025, 4, 22, 20, 0), 'end_time': datetime(2025, 4, 22, 22, 0), 'channel_id': 5},
]
