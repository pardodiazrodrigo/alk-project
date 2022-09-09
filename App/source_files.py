import os
from datetime import date
from settings import PATH_DATA
import requests


def today_str() -> tuple:
    """
    Returns a tuple with the variables of the date
    """
    today = date.today()
    month = today.strftime("%B")
    month_num = today.month
    year = today.year
    day = today.day

    return day, month, month_num, year


def files_csv(data: dict) -> list:
    """
    :param: data: dict with the names and the urls of de files
    :return: the paths of the downloaded files
    """
    paths = []
    day, month, month_num, year = today_str()

    for category, url in data.items():

        path_file = f'{PATH_DATA}/{category}/{year}-{month}/'
        os.makedirs(os.path.dirname(path_file), exist_ok=True)
        csv_name = f'{category}-{day}-{month_num}-{year}.csv'

        try:
            res = requests.get(url)

            with open(f"{path_file}/{csv_name}", "wb") as f:
                f.write(res.content)
                paths.append(f"{path_file}/{csv_name}")

        except requests.exceptions.RequestException as e:
            print(e)

    return paths
