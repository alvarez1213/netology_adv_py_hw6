def task_1_1(list_of_dicts: list) -> list:
    """
    Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
    :param list_of_dicts: list
    :return: list
    """
    for i, d in reversed(list(enumerate(list_of_dicts))):
        if list(d.values())[0][1] != "Россия":
            del list_of_dicts[i]

    return list_of_dicts


def task_1_2(d: dict) -> list:
    """
    Вывести на экран все уникальные гео-ID из значений словаря d.
    :param d: dict
    :return: list
    """
    ret = set()
    for i in d.values():
        ret |= set(i)

    return list(ret)


def task_1_3(queries):
    """
    Дан список поисковых запросов. Получить распределение количества слов в них.
    Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
    :param queries: list
    :return: dict
    """
    total_q = len(queries)
    distr_dict = dict()
    for q in queries:
        k = q.split(" ")
        distr_dict[len(k)] = distr_dict.get(len(k), 0) + 1

    ret = {}
    for el in sorted(distr_dict.keys()):
        ret[el] = round(distr_dict[el] / total_q, 2)

    return ret


if __name__ == "__main__":
    pass
