from django.shortcuts import render
from todo_item.models import ItemModel


def item_view(request):
    lists = ItemModel.objects.filter(
        listmodel=request.user,
        id=5
    )

    # new_list = [
    #     ListModel.objects.create(
    #         name=f'Новый список{i}',
    #         user=request.user
    #     )
    #     for i in [5, 6, 7]
    # ]

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'list.html', context)
