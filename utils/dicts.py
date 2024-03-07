"""Функции для работы со словорями"""


def get_val(collection, key=None, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение
    по-умолчанию.
    :param collection: исходный словарь.
    :param key: ключ извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение по индексу или значение по-умолчанию.
    """

    for key_coll in collection.keys():
        if key_coll == key:
            return collection[key]
    return default
