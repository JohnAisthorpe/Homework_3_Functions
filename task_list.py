tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print uncompleted tasks
def print_uncompleted(list):
    for dict in list:
        while dict["completed"] == False:
            print(dict['description'])
            break

# print_uncompleted(tasks)

# 2. Print completed tasks
def print_completed(list):
    for dict in list:
        while dict["completed"] == True:
            print(dict['description'])
            break

# print_completed(tasks)

# 3. Print a list of all descriptions
def print_all_tasks(list):
    for dict in list:
        print(dict['description'])

# print_all_tasks(tasks)

# 4. Print task that takes at least a given amount of time
def print_long_tasks(list, min_task_length):
    for dict in list:
        while dict["time_taken"] >= min_task_length:
            print(dict['description'])
            break

print_long_tasks(tasks, 15)

# 5. print task with given description
def print_specific_task(list, description):
    for dict in list:
        while dict["description"] == description:
            print(dict)
            break

print_specific_task(tasks, "Walk Dog")