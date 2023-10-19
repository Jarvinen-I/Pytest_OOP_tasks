import pytest
from Task_1.wikipedia import data_from_table_instance


expected_popularity = [
    (10 ** 7),
    (1.5 * 10 ** 7),
    (5 * 10 ** 7),
    (10 ** 8),
    (5 * 10 ** 8),
    (10 ** 9),
    (1.5 * 10 ** 9)
]


@pytest.mark.parametrize('expected_popularity', expected_popularity)
def test_data_from_table_instance(expected_popularity):
    for row in data_from_table_instance.rows:
        actual_popularity = row[1]
        try:
            assert actual_popularity > int(expected_popularity)
        except AssertionError:
            raise AssertionError(
                f'{row[0]} (Frontend:{row[2]}|Backend:{row[3]}) '
                f'has {"{0:,}".format(actual_popularity).replace(",", " ")} unique visitors per month.'
                f' (Expected more than {"{0:,}".format(int(expected_popularity)).replace(",", " ")})')
