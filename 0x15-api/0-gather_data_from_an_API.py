#!/usr/bin/python3
"""A Python script that, for a given employee ID, returns
information about his/her TODO list progress"""

import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo_list = requests.get(url + "todos",
                             params={"userId": emp_id}).json()
    done_tasks = [task for task in todo_list if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todo_list)))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
