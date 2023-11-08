from enum import Enum


class Categories(Enum):
    PROGRAMS = 'Програмне Забезпечення'
    DETAILS_FOR_PC = 'Деталі для Компа'
    ACCESORIES = 'Аксесуари'


menu = [
    {
        'title': 'Powerpoint_key',
        'image': 'image(1)2.png',
        'price': 999,
        'category': (Categories.PROGRAMS.value)
    },
    {
        'title': 'RTX3080',
        'image': 'image(2)1.png',
        'price': 15699,
        'category': (Categories.DETAILS_FOR_PC.value)

    },
    {
        'title': 'Intel Core i5-12400F',
        'image': 'image(3)1.png',
        'price': 3499,
        'category': ( Categories.DETAILS_FOR_PC.value)

    },
    {
        'title': 'Мишка RZTK S 430 USB Black',
        'image': 'image(4)1.png',
        'price': 799,
        'category': (Categories.ACCESORIES.value)

    },
    {
        'title': 'Клавіатура',
        'image': 'image(5)1.jpg',
        'price': 1499,
        'category': (Categories.ACCESORIES.value)

    },
]
