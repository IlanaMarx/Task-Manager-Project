# Task 15 - Capstone Project - Files
# Compulsory Task Part 1 and Compulsory Task Part 2

"""
This task program, will help a small business to manage tasks assigned
to each member of the team. This program will work with two text files,
user.txt and tasks.txt. This program will read and write data from and
to these text files. This program offers the following functionalities:
register user (only accessed by the user with the username 'admin'),
add task, view all tasks, view my tasks and display statistics (only
accessed by the user with the username 'admin').
"""

#=====importing libraries===========
# Import the datetime module to work with dates.
import datetime

#====Login Section====
# This code reads usernames and passwords that is stored in the
# 'user.txt' file and checks if the user entered valid credentials and
# allows them to login if they provided valid credentials.

# Initialize an empty dictionary to store the usernames and passwords.
users = {}
try:
    # Open the 'user.txt' file to read the usernames and passwords.
    # Use a context manager (the 'with' statement) to ensure the file
    # closes automatically when the end of the block of code is reached.
    with open("user.txt", "r") as user_file:
        # Loop through each line in the 'user.txt' file.
        for line in user_file:
            # Remove any whitespace from the beginning or end of each
            # line and splits it into username and password.
            username, password = line.strip().split(", ")
            # Store the username as the key and the password as the
            # value in the 'users' dictionary.
            users[username] = password

# Using 'except FileNotFoundError' to handle the case where the
# 'user.txt' file does not exist and display an informative message.
except FileNotFoundError:
    print("Error: user.txt file not found.")
    # Exit the program.
    exit()

# Initialize a boolean variable to track whether a user is logged in.
logged_in = False
# Initialize a variable to store the username of the user that is
# currently logged in.
current_user = None

# Creating a while loop that will run until a user is successfully
# logged in.
while not logged_in:
    # Get the user's username and password.
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    # Check if the username that was entered exists as a key in the
    # 'users' dictionary AND if the corresponding password matches.
    if username in users and users[username] == password:
        # If the username and pasword is valid, display a successful
        # login message.
        print(f"\nLogin successful! Welcome, {username}!")
        # Set the 'logged_in' variable to True, thus exiting the loop.
        logged_in = True
        # Store the username in the 'current_user' variable.
        current_user = username

    # If the username is not in the 'users' dictionary, display an error
    # message.
    elif username not in users:
        print("\nError: Username not found. Please try again.")

    # If the username is found but the password does not match, display
    # an error message that the password entered is incorrect.
    else:
        print("\nError: Incorrect password. Please try again.")


# The while loop will continue to run and allow the user to choose other
# menu options until they choose 'e' to exit the program.
while True:
    # Check if the current user is 'admin' and display the appropriate
    # menu options.
    if current_user == "admin":

        # Present the menu to the 'admin' user and convert the user
        # input to lower case.
        menu = input('''\nPlease select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
''').lower()

    # If the current user is not 'admin', then display the appropriate
    # menu for non-admin users and convert the user input to lower case.
    else:
        menu = input('''\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
''').lower()

    # The menu option 'r' is to register a new user and will add a new
    # user to the 'user.txt' file. This menu option is only available to
    # the 'admin' user.
    if menu == 'r':
        # Check if the current user that is logged in is 'admin'.
        if current_user == "admin":
            print("\n--- Register a new user ---\n")
            new_username = input("Please enter a new username: ")

            # Using a while loop that will continue to run and allow the
            # 'admin' user to register a new user until the new username
            # is unique and the passwords match.
            while True:
                # If the new username already exists in the 'users'
                # dictionary, display an error message and get new
                # username input.
                if new_username in users:
                    print("Error: Username already exists.")
                    new_username = input("\nPlease enter a new username: ")

                # If the new username is unique get the new password and
                # confim the new password.
                else:
                    new_password = input("\nPlease enter a new password: ")
                    confirm_password = input("\nConfirm the new password: ")

                    # Check if the new password and confirmed password
                    # match.
                    if new_password == confirm_password:

                        # Open the 'user.txt' file in append mode, using
                        # a context manager ensuring it closes
                        # automatically.
                        with open("user.txt", "a") as reg_file:
                            # Write the new username and password to the
                            # 'user.txt' file.
                            reg_file.write(f"\n{new_username}, {new_password}")

                        # Add the new username and new password to the
                        # 'users' dictionary.
                        users[new_username] = new_password
                        print(f"\nUser {new_username} registered successfully")
                        break

                    else:
                        print("Error: Passwords do not match.")

        # If a non-admin user tries to register a new user, display an
        # informative message about the restricted access.
        else:
            print("Error: Only the 'admin' user can register new users.")


    # The menu option 'a' will allow a user to add a new task to the
    # 'tasks.txt' file.
    elif menu == 'a':
        print("\n--- Add a new task ---\n")
        assigned_user = input("Enter the username of the person the task is "
                              "assigned to: ")

        task_title = input("Enter the title of the task: ")
        task_description = input("Enter a description of the task: ")

        # The while loop will continue to run until the user enters the
        # due date of the task in the correct format (dd mmm yyyy).
        while True:
            try:
                # Get the due date of the task in dd mmm yyyy format.
                date_due = input("Enter the due date for the task in the "
                                 "format dd mmm yyyy: ")

                # Using the strptime() function to validate that the
                # user input is in the correct format (dd mmm yyyy).
                due_date = datetime.datetime.strptime(date_due, '%d %b %Y')

                # Using the strftime() function to convert 'due_date'
                # into a string and using the title() function to
                # capitalize the month.
                due_date = due_date.strftime('%d %b %Y').title()
                break

            # Handle the case where the 'date_due' input is in the
            # incorrect format and display an informative message.
            except ValueError:
                print("Error: Invalid date format. Please use dd mmm yyyy.")

        # Get the current date using the datetime module and format it
        # as dd mmm yyyy using the strftime() function.
        current_date = datetime.date.today().strftime('%d %b %Y')
        task_complete = "No"

        # Open the 'tasks.txt' file to append/add the new task details
        # to the file. Use a context manager to ensure the file closes
        # automatically.
        with open("tasks.txt", "a") as tasks_file:
            # Write the task details to the 'tasks.txt' file.
            tasks_file.write(f"\n{assigned_user}, {task_title}, "
                             f"{task_description}, {current_date}, "
                             f"{due_date}, {task_complete}")

        print(f"\nTask '{task_title}' added successfully.")


    # The menu option 'va' allows users to view all tasks by reading the
    # tasks from the 'tasks.txt' file and printing it to the console.
    elif menu == 'va':
        print("\n--- View all tasks ---")

        # Initialize a count variable to display the number of the task.
        count_task = 1
        try:
            # Open the 'tasks.txt' file to read the task details. Use a
            # context manager to ensure the file closes automatically.
            with open("tasks.txt", "r") as tasks_file:

                # Loop through each line in the 'tasks.txt' file.
                for line in tasks_file:
                    # Remove any leading or trailing whitespaces.
                    tasks = line.strip()
                    # Check that the line is not empty.
                    if tasks != "":
                        # Split the line into task details.
                        details = tasks.split(", ")
                        # Display the results.
                        print("__" * 40)
                        print(f"\nTask {count_task}: \t\t{details[1]}")
                        print(f"Assigned to: \t\t{details[0]}")
                        print(f"Date assigned: \t\t{details[3]}")
                        print(f"Due Date: \t\t{details[4]}")
                        print(f"Task Complete? \t\t{details[5]}")
                        print(f"Task description:\n {details[2]}")
                        count_task += 1
                print("__" * 40)

        # Handle the case where the 'tasks.txt' file does not exist and
        # display an informative message.
        except FileNotFoundError:
            print("Error: tasks.txt file not found.")


    # The menu option 'vm' will display the tasks that are assigned to
    # the user that is currently logged in.
    elif menu == 'vm':
        print(f"\n--- My Tasks ({current_user}) ---")

        # Initialize a boolean variable to track if any tasks are found
        # for the current user.
        found_tasks = False
        try:
            # Open the 'tasks.txt' file to read the task information.
            # Use a context manager to ensure the file closes
            # automatically.
            with open("tasks.txt", "r") as tasks_file:
                # Loop through each line in the 'tasks.txt' file.
                for line in tasks_file:
                    # Remove any leading or trailing whitespaces.
                    task_info = line.strip()
                    # Check that the line is not empty.
                    if task_info != "":
                        # Split the line into task details.
                        info = task_info.split(", ")

                        # Check if the username in the task matches the
                        # currently logged in user.
                        if info[0] == current_user:
                            # Display the results.
                            print("__" * 40)
                            print(f"\nTask: \t\t\t{info[1]}")
                            print(f"Assigned to: \t\t{info[0]}")
                            print(f"Date assigned: \t\t{info[3]}")
                            print(f"Due Date: \t\t{info[4]}")
                            print(f"Task Complete? \t\t{info[5]}")
                            print(f"Task description:\n {info[2]}")
                            # Set 'found_tasks' to True as at least one
                            # task was found.
                            found_tasks = True
                print("__" * 40)

                # If no tasks were found for the currently logged in
                # user, display an informative message.
                if not found_tasks:
                    print("No tasks assigned to you.")

        # Handle the case where the 'tasks.txt' file does not exist and
        # display an informative message.
        except FileNotFoundError:
            print("Error: tasks.txt file not found.")


    # The menu option 'ds' will display the total number of tasks and
    # the total number of users. This menu option is only available to
    # the 'admin' user.
    elif menu == 'ds':
        # Check if the current user that is logged in is 'admin'.
        if current_user == 'admin':
            total_tasks = 0
            try:
                # Open the 'tasks.txt' file in read mode. Use a context
                # manager to ensure the file closes automatically.
                with open("tasks.txt", "r") as tasks_file:
                    for line in tasks_file:
                        task = line.strip()
                        # Check that the line is not empty.
                        if task != "":
                            # Increment 'total_tasks' by 1 for every
                            # line in the 'tasks.txt' file.
                            total_tasks += 1

            # Handle the case where the 'tasks.txt' file does not exist.
            # If 'tasks.txt' is not found, the total_tasks is 0 and an
            # informative message is displayed.
            except FileNotFoundError:
                total_tasks = 0
                print("\nError: tasks.txt file not found, therefore the total "
                      "number of tasks is set to 0.")

            # The total number of users is equal to the number of
            # key-value pairs in the 'users' dictionary.
            total_users = len(users)

            # Display the statistics.
            print("\n--- Display statistics ---")
            print(f"Total number of tasks: {total_tasks}")
            print(f"Total number of users: {total_users}")
            print("----------------------------")

        # If a non-admin user tries to access the display statistics
        # (ds) menu option, display an informative message about the
        # restricted access.
        else:
            print("Only the 'admin' user can choose to display statistics.")


    # The menu option 'e' will log out the user and exit the program.
    elif menu == 'e':
        print(f"Goodbye!!! {current_user} successfully logged out.")
        exit()

    # Handle the case where the user enters an invalid input and display
    # an informative message.
    else:
        print("You have entered an invalid input. Please try again")
