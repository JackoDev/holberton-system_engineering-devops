#!/usr/bin/python3
""" a Python script that, using a REST API, for a given
employee ID, returns information about his/her TODO list progress. """
import requests
import sys


if __name__ == "__main__":
    source = "https://jsonplaceholder.typicode.com/"
    url_user = "{}users/{}".format(source, sys.argv[1])
    req_user = requests.get(url_user)
    user_out = req_user.json()
    print("Employee {} is done with tasks".format(user_out.get('name')), end="")
    task_list = '{}todos?userId={}'.format(source, sys.argv[1])
    req_user = requests.get(task_list)
    tasks = req_user.json()
    done = []
    
    for task in tasks:
        if task.get('completed') is True:
            done.append(task)
    print("({}/{}):".format(len(done), len(tasks)))
    for task in done:
        print("\t {}".format(task.get("title")))
