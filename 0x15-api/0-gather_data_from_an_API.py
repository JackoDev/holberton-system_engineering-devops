#!/usr/bin/python3
""" a Python script that, using a REST API, for a given
employee ID, returns information about his/her TODO list progress. """
from requests import get
from sys import argv


def get_from_api(id):
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users/{}".format(id)).json()
    done = get(url + "todos?userId={}".format(id)).json()
    new = []
    for i in done:
        if i.get("completed"):
            new.append(i.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(users["name"], len(new), len(done)))
    for j in new:
        print("\t {}".format(j))


if __name__ == "__main__":
    get_from_api(int(argv[1]))
