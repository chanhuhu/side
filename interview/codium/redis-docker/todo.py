from enum import Enum
from typing import Literal
import unittest

import redis

r = redis.Redis(host='localhost', port=6379) # listening to 0.0.0.0:6379

Task = str

def print_tasks(tasks: list[Task]) -> None:
    for task in tasks:
        print(task)

def print_help() -> None:
    print("available mode: {add,remove,show,quit,help}")
    
def main():
    tasks: list[Task] = []

    print_help()
    while True:
        mode = input("Enter mode: ")

        # do while for retrieving tasks
        if mode == 'add':
            while True:
                task = input("Enter for adding task: ")

                if task == '':
                    break

                tasks.append(task)
            r.sadd("tasks", *tasks)
        elif mode == 'remove':
            task = input("Enter your task with you want to delete: ")
            r.srem('tasks', task)
        elif mode == 'help':
            print_help()
        elif mode == 'show':
            for task in r.smembers('tasks'):
                print(task.decode("utf-8"))
        elif mode == 'quit':
            break
        else:
            print(f"NotImplemented mode: {mode}")

            

    print_tasks(tasks)
    

if __name__ == "__main__":
    exit(main())

