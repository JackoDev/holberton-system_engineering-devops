#!/usr/bin/python3
""" a Python script that, using a REST API, for a given
employee ID, returns information about his/her TODO list progress. """
import requests
import sys

if __name__ == '__main__':
    id_emp = sys.argv[1]
    res1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id_emp))
    res2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos'.format(id_emp))
    name_emp = res1.json().get('name')
    task_list = res2.json()
    done_list = []
    total_task = 0
    for i in task_list:
        if i.get('userId') == int(id_emp):
            total_task += 1
            if i.get('completed') is True:
                done_list.append(i['title'])

    print('Employee {} is done with tasks({}/{}):'.format(name_emp,
                                                          len(done_list),
                                                          total_task))
    for i in done_list:
        print('\t {}'.format(i))
