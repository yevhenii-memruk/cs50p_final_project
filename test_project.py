import datetime
from project import show_total_time_app
from project import get_today
from project import apps_without_total
from project import get_today_app

import pytest


# TEST DICTIONARY
test_dictionary = {
    "Total Time": {
        "Visual Studio Code": 47,
        "Clock": 9,
        "Telegram": 2,
        "Google Chrome": 3,
    },
    "Visual Studio Code": {"2023-10-19": 26, "2023-09-10": 10, "2022-02-18": 11},
    "Clock": {"2023-10-19": 9},
    "Telegram": {"2023-10-19": 2},
    "Google Chrome": {"2023-10-19": 3},
}


def test_show_total_time_app():
    total_time = datetime.timedelta(
        seconds=test_dictionary["Total Time"]["Google Chrome"]
    )
    assert (
        show_total_time_app("Google Chrome", test_dictionary)
        == f"Google Chrome : {str(total_time)}"
    )


def test_apps_without_total():
    copy_test_dict = test_dictionary.copy()
    copy_test_dict.pop("Total Time")
    assert apps_without_total(test_dictionary) == copy_test_dict
    assert apps_without_total(test_dictionary) != test_dictionary


def test_get_today():
    today_date = "2023-10-19"
    for title in get_today(test_dictionary, today_date):
        seconds = test_dictionary[title[0]].get(today_date, 0)
        seconds_in_datetime = str(datetime.timedelta(seconds=seconds))
        assert title == (title[0], seconds_in_datetime)


def test_get_today_app():
    today_date = "2023-10-19"
    title = "Visual Studio Code"
    seconds = test_dictionary[title].get(today_date, 0)
    seconds_in_datetime = str(datetime.timedelta(seconds=seconds))
    assert (
        get_today_app(test_dictionary, title, today_date)
        == f"{title} : {seconds_in_datetime}"
    )
