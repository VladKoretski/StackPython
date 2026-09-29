import pytest
from tools.check_brackets import check_brackets as cb

brackets_params = (('(((([{}]))))', 'Сбалансированно'),
                   ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
                   ('{{[()]}}', 'Сбалансированно'),
                   ('}{}', 'Несбалансированно'),
                   ('{{[(])]}}', 'Несбалансированно'),
                   ('{[(])}', 'Несбалансированно')
                   )

@pytest.mark.parametrize('bracket_string, expected', brackets_params)
def test_check_brackets(bracket_string, expected):
    '''Тестируем функцию check_brackets'''
    assert cb(bracket_string) == expected
