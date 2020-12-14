from django.db import models


class ItemModel(models.Model):
    """
    Модель элемента списка дел
    """
    name = models.CharField(max_length=128, verbose_name='Название списка')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, blank=True)
    listmodel_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    expare_date = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Элемент списка дел'
        verbose_name_plural = 'Элемент списка дел'
        unique_together = ('name', 'listmodel_id')
