#!/usr/bin/python3
""" a Python script that, using a REST API, for a given
employee ID, returns information about his/her TODO list progress. """
import requests
import sys
import csv

if __name__ == '__main__':
    id_emp = sys.argv[1]
    res1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id_emp))
    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos'.format(id_emp))
    username_emp = res1.json().get('username')
    task_list = res2.json()
    done_list = []
    total_task = 0
    for i in task_list:
        if i.get('userId') == int(id_emp):
            done_list.append(i)
    with open("{}.csv".format(id_emp), mode='w') as file1:
        w = csv.writer(file1, delimiter=',', quoting=csv.QUOTE_ALL)
        for j in done_list:
            w.writerow([j['userId'], username_emp, j['completed'], j['title']])
