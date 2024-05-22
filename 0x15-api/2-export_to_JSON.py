#!/usr/bin/python3
"""Python script that, for a given employee ID,
captures information about his/her TODO list progress
and exports it in JSON format """

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo_list = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump({emp_id: [{"task": task.get("title"),
                             "completed": task.get("completed"),
                             "username": user.get("username")}
                            for task in todo_list]}, jsonfile)
