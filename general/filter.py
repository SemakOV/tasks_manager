import django_filters
from general.models import Task


class FilterTasksState(django_filters.FilterSet):
    CHOICES = (
        ('Новая', 'Новая'),
        ('Запланированная', 'Запланированная'),
        ('в Работе', 'в Работе')
    )
    state = django_filters.ChoiceFilter(label='Сортировать по статусу', choices=CHOICES) #,  method='filter_by_order')

    class Meta:
        model = Task
        fields = ('state',)

    # def filter_by_order(self, queryset, name, value):
    #     return queryset.order_by('time_out')