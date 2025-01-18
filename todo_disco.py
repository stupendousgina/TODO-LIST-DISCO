"""TO-DO LIST"""

def welcome(fill):
    name = input('Enter your name: ')
    print(f"""
    Hello, {name.title()}.
    Welcome to {fill}!""")

def menu_options():
    print("""
        To-do Menu:
    1. Add a task
    2. View your list
    3. Delete a task
    4. Quit application
    """)

def add_task():
    while True:
        task = input("Enter task to add: ")
        if task not in todo:
            todo.append(task)
            print(f"\t'{task}' added.")
        else:
            print(f"\t'{task}' exists already.")
            
        add_more = input("Add more tasks (yes/no)? ")
        if add_more.lower() != 'yes':
            break
        else:
            continue

def view_task(todo):
    if len(todo) > 0:
        print("\n\tYour To-Do List:")
        for i, task in enumerate(todo):
            print(f"{i+1}. {task}")
    else:
        print("There are no tasks in your to-do list.")

def delete_task(todo):
    while len(todo) > 0:
        view_task(todo)
        task = input("Enter the task to delete: ")
        
        if task in todo:
            todo.remove(task)
            print(f"\t'{task}' removed.")
        else:
            print(f"\t'{task}' does not exist.")
        
        delete_more = input('Delete another task (yes/no)? ')
        if delete_more.lower() != 'yes':
            break
        else:               
            continue
    else:
        print('\tThere are no tasks in your To-do List.')

todo = []

welcome(fill='your personal TO-DO list app')
while True:
    menu_options()
    try:
        selection = int(input("Enter a number/option: "))
        if selection < 1 or selection > 4:
            raise ValueError

        if selection == 1:
            add_task()
        elif selection == 2:
            view_task(todo)
        elif selection == 3:       
            delete_task(todo)
        elif selection == 4:
            print("\tThank you for using the To-do List app!")
            break
    except (ValueError, TypeError) as e:
        print("\n\tInvalid selection. Enter a number between 1 and 4 from the options menu.")

