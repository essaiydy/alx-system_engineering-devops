#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID'''

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    usinfo = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]

    todo_respo = requests.get(url).json()
    name_respo = requests.get(usinfo).json()
    EMPLOYEE_NAME = name_respo.get("name")
    TOTAL_NUMBER_OF_TASKS = len(todo_respo)
    NUMBER_OF_DONE_TASKS = 0

    for task in todo_respo:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {} is done with tasks {}/{}".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in todo_respo:
        if task["completed"]:
            print("\t {}".format(task["title"]))
