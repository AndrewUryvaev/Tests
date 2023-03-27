ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

def numbers(id):
    number_list = list(ids.values())
    number_set_a = set(number_list[0])
    number_set_b = set(number_list[1])
    number_set_c = set(number_list[2])
    number_set = number_set_a | number_set_b | number_set_c
    return list(number_set)

geo_log = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def city(geo_logs):
    for number in range(len(geo_logs)):
        if geo_logs[number][f'visit{number + 1}'][1] == 'Россия':
            res = geo_logs[number]
    return res




lists = ['2018-01-01', 'yandex', 'cpc', 100]
def yandex(lists_over):
    dic = lists.pop()
    for i in reversed(lists):
        dic = {i: dic}
    return dic


if __name__ == '__main__':
    city(geo_log)
    numbers(ids)
    yandex(lists)

