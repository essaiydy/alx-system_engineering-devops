#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(base_url + "todos", params={"userId": employee_id}).json()
    
    return user, todos

def print_employee_tasks(name, completed_tasks, total_tasks):
    print("Employee {} is done with tasks({}/{}):".format(name, completed_tasks, total_tasks))
    [print("\t {}".format(c)) for c in completed_tasks]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        employee_id = sys.argv[1]
        user, todos = get_employee_data(employee_id)
        
        completed_tasks = [t.get("title") for t in todos if t.get("completed")]
        print_employee_tasks(user.get("name"), len(completed_tasks), len(todos))
