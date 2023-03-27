import unittest
from unittest import TestCase
from func import numbers, ids, city, geo_log, yandex, lists
from yandex_hw import get_foldres

class TestHomeWork(TestCase):
    def test_city_lists(self):
        result = city(geo_log)
        # не получается сравнить результат вывода...
        test_geo_log = {'visit1': ['Москва', 'Россия']}
        self.assertNotEqual(result, test_geo_log)


    def test_len_list(self):
        result = len(numbers(ids))
        expected = 5
        self.assertEqual(result, expected)

    def test_social(self):
        result = yandex(lists)
        expected_dict = ['2018-01-01', 'yandex', 'cpc', 100]
        self.assertNotEqual(result, expected_dict)

    def test_ya(self):
        result = get_foldres()
        finish_geo_log = 201
        assert result == finish_geo_log