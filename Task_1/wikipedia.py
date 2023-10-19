import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class DataFromTable:
    """Class for storing data"""
    rows: list


def get_data_from_table():
    """Function collects information from a table on the Wikipedia page and returns a list of collected data"""
    url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    table = soup.find('table').find('tbody').find_all('tr')[1:]
    data = []

    for row in table:
        cells = [cell.text[:-1] for cell in row.find_all('td')]
        title = cells[0].split('[')[0]
        popularity = int(''.join([i for i in cells[1].split('[')[0].split()[0] if i.isdigit()]))
        frontend = cells[2]
        backend = ', '.join([''.join([j for j in i if j.isalpha() or j in '+#( )./']).strip()
                             for i in cells[3].split(',')])
        databases = ', '.join([base for base in [''.join([j for j in i if j.isalpha() or j in '+#( )./']).strip()
                                                 for i in cells[4].split(',')] if len(base) > 0])

        data.append((title, popularity, frontend, backend, databases))

    return data


data_from_table_instance = DataFromTable(get_data_from_table())

if __name__ == '__main__':
    for row in data_from_table_instance.rows:
        print(row)
