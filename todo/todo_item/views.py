from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Велопрогулка', 'is_done': True, 'date': '01.12.2019'},
        {'name': 'СноуПарк', 'is_done': False},
        {'name': 'Дайвинг', 'is_done': True},
        {'name': 'ПрыжокСпарашутом', 'is_done': True},
    ],
    'user_name': 'Admin',
}


def item_view(request):
    content = data
    return render(request, 'list.html', content)
