from django.shortcuts import render
import json
import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseNotFound


def invalid_spec(request):
    return render(request, 'data/404.html', status=404)


def load_data():

    file_path = os.path.join(settings.BASE_DIR, 'data',
                             'fixtures', 'dump.json')
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)


def spec_list(request):
    data = load_data()

    # фильтруем только квалификации
    specialties = [item for item in data if item['model']
                   == 'data.specialty']

    context = {
        'title': 'Квалификации',
        'specialties': specialties,
    }

    return render(request, 'data/spec_list.html', context)


def spec_detail(request, id):
    data = load_data()

    try:
        if not id:
            raise ValueError

        id = int(id)
        if id <= 0:
            raise ValueError
    except:
        return render(request, 'data/404.html', status=404)

    # Ищем квалификацию по id
    specialty = next(
        (item for item in data if item['model'] == 'data.specialty' and item['pk'] == id), None)

    if specialty is None:
        return render(request, 'data/404.html', status=404)

    context = {
        'specialty': specialty
    }

    return render(request, 'data/spec_detail.html', context)
