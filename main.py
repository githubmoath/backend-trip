import tasks

my_tasks = [
    {"id": 1, "title": "study python", "done": False},
    {"id": 2, "title": "computer vision", "done": True},
]

# tasks.show_tasks(my_tasks)

# print ("A")
# if __name__ == "__main__":
#     print ("B")
found =tasks.find_task_by_id(my_tasks, 1)
# print(type(found))
print(found)  # Output: "study python"

print(tasks.find_task_by_id(my_tasks, 5))
