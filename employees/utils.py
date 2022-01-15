import random, datetime
from employees.models import *

names_list = ['Евгений', 'Сергей', 'Иван', 'Дмитрий', 'Алексей', 'Андрей', 'Александр', 'Олег', 'Игорь', 'Вадим',
              'Степан', 'Максим']
lnames_list = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Петров', 'Лебедев', 'Козлов', 'Новиков', 'Морозов',
               'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Виноградов', 'Богданов', 'Воробьёв',
               'Фёдоров', 'Михайлов', 'Беляев', 'Сидоров', 'Белов']
depar_list = ['Отдел кадров', 'Бухгалтерия', 'Отдел снабжения', 'Производственно-технический отдел',
              'Производители работ']


def fill_employees(subdivisions, pos_list):
    for el in lnames_list:
        Employee.objects.create(
            f_name=random.choice(names_list),
            l_name=el,
            subdivision=random.choice(subdivisions),
            department=random.choice(depar_list),
            position=random.choice(pos_list),
            employment_date=datetime.date(2021, 11, 11)
        )


if __name__ == '__main__':
    pass
