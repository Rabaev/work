# Переменные
dish_number = 0

# Книга рецептов
recept_book = {
    'Омлет': {
        'name': 'Омлет',
        'type': '2-е',
        'ingridients': [
                {'product' : 'Яйца', 'quantity': 2, 'unit': 'шт'},
                {'product' : 'Молоко', 'quantity': 50, 'unit': 'мл'},
                {'product' : 'Помидор', 'quantity': 100, 'unit': 'г'},
        ]
    }, 
    'Яблочный пирог': { 
        'name': 'Яблочный пирог',
        'type': 'Десерт',
        'ingridients': [
                {'product' : 'Яйца', 'quantity': 1, 'unit': 'шт'},
                {'product' : 'Мука', 'quantity': 300, 'unit': 'г'},
                {'product' : 'Масло', 'quantity': 60, 'unit': 'г'},
                {'product' : 'Яблоки', 'quantity': 80, 'unit': 'г'},
        ]
    },
    'Суп': {
        'name': 'Суп',
        'type': '1-е',
        'ingridients': [
                {'product' : 'Вода', 'quantity': 100, 'unit': 'мл'},
                {'product' : 'Помидор', 'quantity': 300, 'unit': 'г'},
        ]
    }, 
}


with open('receptbook.txt', 'w') as doc:
    for items in recept_book.values():
        dish_number += 1
        name = 'Блюдо № %.0f: ' % dish_number + str(items['name']) + '\n'
        doc.write(name)
        items_count = 'Ингридиентов: ' + str(len(items['ingridients'])) + '\n'
        doc.write(items_count)
        doc.write('Список ингридиентов:\n')
        for i in items['ingridients']:
            products = '{0} | {1} | {2}'.format(i['product'], i['quantity'], i['unit']) + '\n'
            doc.write(str(products))
        doc.write('\n')