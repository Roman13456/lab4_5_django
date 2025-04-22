from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .data import CHANNELS, PROGRAMS


def home(request):
    """Представлення для домашньої сторінки."""
    return render(request, 'tvguide/home.html')

def channel_list(request):
    """Представлення для списку телеканалів."""
    context = {
        'channels': CHANNELS
    }
    return render(request, 'tvguide/channel_list.html', context)

def channel_detail(request, channel_id):
    """Представлення для детальної сторінки телеканалу."""
    # Знаходимо канал за ID
    channel = None
    for c in CHANNELS:
        if c['id'] == channel_id:
            channel = c
            break

    if channel is None:
        raise Http404("Телеканал не знайдено")

    # Знаходимо програми для цього каналу
    channel_programs = [p for p in PROGRAMS if p['channel_id'] == channel_id]

    # Сортуємо програми за часом початку
    channel_programs.sort(key=lambda x: x['start_time'])

    context = {
        'channel': channel,
        'programs': channel_programs,
    }
    return render(request, 'tvguide/channel_detail.html', context)

def program_list(request):
    """Представлення для списку всіх телепрограм."""
    # Отримуємо всі програми
    all_programs = PROGRAMS[:] # Копія списку, щоб не змінювати оригінал при сортуванні

    # Сортуємо програми за часом початку, найближчі першими
    all_programs.sort(key=lambda x: x['start_time'])

    # Додаємо назву каналу до кожної програми для зручності відображення
    programs_with_channel_name = []
    channel_dict = {c['id']: c['name'] for c in CHANNELS} # Створюємо словник для швидкого пошуку назви каналу

    for program in all_programs:
        program_copy = program.copy() # Копіюємо словник програми
        program_copy['channel_name'] = channel_dict.get(program['channel_id'], 'Невідомий канал')
        programs_with_channel_name.append(program_copy)


    context = {
        'programs': programs_with_channel_name,
    }
    return render(request, 'tvguide/program_list.html', context)
