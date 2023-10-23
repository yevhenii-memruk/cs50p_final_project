import json
import os.path
import sys
import datetime
from datetime import date

from timer import Timer
from system_getter import window_title


class NoCommandExist(Exception):
    pass
    

def main():
    try:
        while True:
            app_running = window_title()
            start_timer = Timer(app_running)
            start_timer.time_entry()
    except KeyboardInterrupt:
        json_object = json.dumps(Timer.data, indent=4)
        if os.path.exists(r"user_data\data_apps.json"):
            json_object = json.dumps(data_process_manager(load_local_json()), indent=4)
        else:
            # Creation of object "Total Time" for first program entry
            sas = Timer.data.copy()
            for count, app_total in enumerate(sas):
                if count == 0:
                    Timer.data.update(
                    {"Total Time": {app_running: list(Timer.data[app_running].values())[0]}}
                    )
                else:
                    Timer.data["Total Time"].update({app_total: list(Timer.data[app_total].values())[0]})
            json_object = json.dumps(Timer.data, indent=4)
        # Rewriting json file
        with open(r"user_data\data_apps.json", "w") as outfile:
            outfile.write(json_object)


def data_process_manager(json_file_dict: dict):
    """
    Opening the existed json file and checking if application was already used or not.

    :var timer_inner_dict_key: Variable of date (year-month-day) of current opening of app
    :var app_usage_time: Amount of time we spent in app for single working process

    """
    # Iterate all Apps' Titles in last working process
    for title in list(Timer.data.copy().keys()):
        timer_inner_dict_key = list(Timer.data[title])[0]
        app_usage_time = Timer.data[title][timer_inner_dict_key]

        # If date and app already existed
        if (
            title in json_file_dict
            and timer_inner_dict_key in json_file_dict[title]
        ):
            json_file_dict[title][timer_inner_dict_key] += app_usage_time
            if json_file_dict.get("Total Time") and json_file_dict["Total Time"].get(title):
                json_file_dict["Total Time"][title] += app_usage_time
        # If the date you using app is dufferent from last opening
        elif (
            title in json_file_dict
            and timer_inner_dict_key != list(json_file_dict[title])[0]
        ):
            json_file_dict[title][timer_inner_dict_key] = app_usage_time
            if json_file_dict.get("Total Time") and json_file_dict["Total Time"].get(title):
                json_file_dict["Total Time"][title] += app_usage_time
        # Creating new data of new opened app
        else:
            if not json_file_dict.get("Total Time"):
                json_file_dict.update({"Total Time": {title: 0}})
            for x, y in Timer.data[title].items():
                json_file_dict.update({title: {x: y}})
                # Creating new dictionary element - "Total Time" (only once)
                json_file_dict["Total Time"].update({title: y})

    return json_file_dict


def load_local_json() -> dict:
    with open(r"user_data\data_apps.json") as app_json_file:
        return json.load(app_json_file)


def show_total_time_app(app_name: str, json_file_dict: dict) -> str:
    total_time_in_sec = json_file_dict["Total Time"][app_name]
    total_time = datetime.timedelta(seconds=total_time_in_sec)
    return f"{app_name} : {str(total_time)}"


def apps_without_total(json_file_dict: dict) -> dict:
    copy_dict = json_file_dict.copy()
    if "Total Time" in copy_dict:
        copy_dict.pop("Total Time")
    return copy_dict


def get_today(json_file_dict: dict, today_date: str) -> list:
    dict_apps_without_total = apps_without_total(json_file_dict)
    today_apps_total_time = [
        (title, dict_apps_without_total[title].get(today_date, 0))
        for title in dict_apps_without_total
    ]
    return [
        (i[0], str(datetime.timedelta(seconds=i[1]))) for i in today_apps_total_time
    ]


def get_today_app(json_file_dict: dict, app_name: str, today_date: str) -> str:
    dict_apps_without_total = apps_without_total(json_file_dict)
    today_time = datetime.timedelta(seconds=dict_apps_without_total[app_name][today_date])
    return f"{app_name} : {today_time}"


if __name__ == "__main__":
    today_date = str(date.today())
    list_commands = "commands list:\n-list\n-today\n-total \'app_name\'\n-today \'app_name\'"
    try:
        if len(sys.argv) == 1:
            print(list_commands)
            main()
        elif len(sys.argv) == 2 and sys.argv[1] == "list":
            for app in load_local_json():
                print(app)
        elif len(sys.argv) == 2 and sys.argv[1] == "today":
            print()
            for iter, today_app in enumerate(get_today(load_local_json(), today_date), 1):
                app, time = today_app
                print(f"{iter}. {app} - {time}")
        elif len(sys.argv) == 3 and sys.argv[1] == "total" and sys.argv[2] in load_local_json():
            print(show_total_time_app(sys.argv[2], load_local_json()))
        elif len(sys.argv) == 3 and sys.argv[1] == "today" and sys.argv[2] in load_local_json():
            print(get_today_app(load_local_json(), sys.argv[2], today_date))
        else:
            print("\n", list_commands, "\n")
            raise NoCommandExist("There is no such command!")
    except IndexError:
        print("\n", list_commands, "\n")
        raise NoCommandExist("There is no such command!")    