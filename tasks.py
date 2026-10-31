# def show_tasks (ta) :

#     for task in ta:
#         print (task['id'])
#         print (task['title'])
#         print (task['done'])

# import main
# import week1

# print ("A")
# if __name__ == "__main__":
#     print ("B")

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] ==task_id:
            return task
    return None