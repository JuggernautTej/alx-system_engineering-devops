#!/usr/bin/python3
""" Python script that, for all employees,
captures information about their TODO list progress
and exports it in JSON format """

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todo_list = requests.get(url + "todos").json()

    data = {}
    for user in users:
        emp_id = user.get("id")
        user_name = user.get("username")
        tasks = [{"task": task.get("title"),
                  "completed": task.get("completed"),
                  "username": user_name}
                 for task in todo_list if task.get("userId") == emp_id]
        data[emp_id] = tasks

    with open("todo_all_employees.json", "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)
