from enum import Enum


class Categories(Enum):
    CHEESE = 'З СИРОМ'
    MEAT = 'З МЯСОМ'
    SEAFOOD = 'З МОРЕПРОДУКТАМИ'


menu = [
    {
        'title': 'Карбонара',
        'image': 'image(1).png',
        'price': 220,
        'category': []
    },
    {
        'title': 'Папероні',
        'image': 'image(2).png',
        'price': 220,
        'category': (Categories.CHEESE.value)

    },
    {
        'title': 'Барбекю',
        'image': 'image(3).png',
        'price': 220,
        'category': (Categories.CHEESE.value, Categories.MEAT.value)

    },
    {
        'title': 'Папероні з копченим м\'ясом',
        'image': 'image(4).png',
        'price': 220,
        'category': (Categories.MEAT.value)

    }
]
