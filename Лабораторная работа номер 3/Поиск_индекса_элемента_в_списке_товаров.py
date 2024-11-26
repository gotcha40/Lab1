# TODO Напишите функцию для поиска индекса товара
def search_index(list_):
    if find_item in list_:
        index = list_.index(find_item)
        return index
    else:
        index_ = None
        return index_
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
for find_item in ['банан', 'груша', 'персик']:
    if search_index(items_list) is not None:
        print('Первое вхождение товара', find_item, 'имеет индекс', items_list.index(find_item))
    else:
        print('Товар', find_item, 'не найден в списке')