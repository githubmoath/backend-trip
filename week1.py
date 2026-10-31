
## day 1
# tasks =[# def show_tasks (ta) :

#     for task in ta:
#         print (task['id'])
#         print (task['title'])
#         print (task['done'])
#      {'id' : 1,'title' : 'study python','done' : False},
#      {'id' : 2,'title' : 'computer vasion','done' : True}
#       ]

# # print(tasks[1]['title'])
# # print (tasks[0]['done'])




# def add_task (ta, id, title):
#     task = {'id' : id, 'title' : title, 'done' : False}
#     ta.append(task)

# add_task(ta=tasks, id=3, title="learn web development")   
# add_task(ta=tasks, id=4, title="learn data science")

# def mark_done(ta, id):
#     for task in ta:
#         if task['id'] == id:
#             task['done'] = True
#             break

# mark_done(ta=tasks, id=4)




# # def delete_task(ta, task_id):
# #     for task in ta:
# #         if task['id'] == task_id:
# #             ta.remove(task)
# #             print("task "+ str(task_id) + " deleted")
# #             return
# #         # elif task['id'] != task_id:
# #     print("task "+ str(task_id) + " not found")
# #     return

# def delete_task(ta, task_id):
#     for task in ta:
#         if task['id'] == task_id:
#             ta.remove(task)
#             # print("task "+ str(task_id) + " deleted")
#             return True
#     return False

# def print_delete_result(ta, task_id):
#     if delete_task(ta, task_id):
#         print("task "+ str(task_id) + " deleted")
#     else:
#         print("task "+ str(task_id) + " not found")

# print_delete_result(tasks, 2)
# print_delete_result(tasks, 5)

# result = delete_task(ta=tasks, task_id=6)
# print("\nresult =", result)
# show_tasks(ta=tasks)

## day 2

# tasks = [
#     {"id": 1, "title": "Python", "done": False},
#     {"id": 2, "title": "Git", "done": True},
#     {"id": 3, "title": "AI", "done": False},
# ]

# def inspect(items, target_id):
#     titles = set()
#     for task in items:
#         titles.add(task["title"])
#         if task["id"] == target_id:
#             task["done"] = True
#     return titles

# result = inspect(tasks, 1)
# print("result =", result)
# print(inspect(tasks, 99))




## day3

# def change_title(title):
#     title = "New title"
#     print (title)
# def add_title(titles):
#     titles.append("New title")

# name = "Old title"
# names = ["Old title"]

# change_title(name)
# add_title(names)

# print(name)
# print(names)

# def replace_titles(titles):
#     titles = ["New title"]

# names = ["Old title"]
# replace_titles(names)
# print(names)

# def add_item(item, items=None):
#     if items is None:
#         items = []
#     items.append(item)
#     return items


# print(add_item("Python"))
# print(add_item("Git", []))



# not_finished_tasks = [task['title'] for task in tasks if task['done'] == False]
# print (not_finished_tasks)



print ("Alaa")
if __name__ == "__main__":
    print ("moath")