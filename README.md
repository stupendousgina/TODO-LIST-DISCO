# To-Do List Disco

A command-line interface (CLI) To-Do List Application that allows users to create a to-do list by adding tasks, view list, remove tasks and exit application.

## Features

1. Personal welcome message
2. Display menu for options
   - Valid Option selections:
   1. Add a task
      - add more until user is done
      - alerts:
        - for tasks added
        - if task exists already
   2. View to-do list
      - organized numbered list
      - alerts:
        - if there are no tasks
   3. Delete a task
      - delete more until user is done
      - alerts for:
        - tasks removed
        - task does not exist
        - no tasks
      - displays to-do list for ease and usability
   4. Quit application
      - friendly message
   - Invalid selection:
     - alerts when option selected is not on menu

### Dependencies

- initializing

### Executing program

When the file is open and initialized:

1. User is prompted from the command line to enter their name for a personal welcome message
2. Displays menu for To-do list options
3. User is prompted to select a number from the menu for an option they would like to perform.

- All menu selection inputs will be integers.
- Options 1 and 3 will continue until user decides to break.
- Option 2 displays numbered task titles
- Option 4 will Exit the app with a friendly message.
- When the app is exited, the list is not stored and user cannot access the list again.
- Empty list is re-initialized.

####

Thanks CodingTemple, Udemy & Youtube

By Gina
