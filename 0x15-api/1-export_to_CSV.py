#!/usr/bin/python3
"""A python script that, for a given employee ID,
captures information about his/her TODO list
progress and exports it in CSV format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = argv[1]
    user = requests.get(url + "users/{}".format(emp_id)).json()
    todo_list = requests.get(url + "todos", params={"userId": emp_id}).json()

    with open("{}.csv".format(emp_id), "w", encoding='utf8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow([emp_id, user.get("username"),
                         task.get("completed"), task.get("title")])
         for task in todo_list]
