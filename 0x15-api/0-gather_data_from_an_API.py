#!/usr/bin/python3
""" a Python script that, using a REST API, for a given
employee ID, returns information about his/her TODO list progress. """
import requests
from sys import argv

try:
    todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    todos = requests.get(todos)
    user = requests.get(user)
    u = user.json()
    t = todos.json()
    done = 0
    tasks = []
    for i in t:
        if i['completed'] is True:
            done += 1
            tasks.append(i['title'])
    print("Employee {} is done with tasks({}/{}):".format(
        u['name'], done, len(t)))
    for t in tasks:
        print("\t {}".format(t))
except Exception as error:
    pass
