import os
import sys


def function1():
    """cd to the directory create a parent folder then create [week]1-12 sub folders"""
    # Print the current directory before change
    print("Current Working Directory: ", os.getcwd())
    # Prompt user for the directory
    directory = input("Specify the directory to change to: ")
    # Check if new path exists
    if os.path.exists(directory):
        # Change the current working Directory
        os.chdir(directory)
        print("Current Working Directory: ", os.getcwd())
        # Get the parent folder name from the user
        parent_folder = input("Enter the parent folder name: ")
        # Check if directory already exists
        if not os.path.exists(parent_folder):
            os.mkdir(parent_folder)
        # Change to parent folder directory
        print("Changing to the directory %s" % parent_folder)
        os.chdir(parent_folder)
        print("Creating folders..")
        folders = ['week1', 'week2', 'week3', 'week4', 'week5', 'week6',
                   'week7', 'week8', 'week9', 'week10', 'week11', 'week12']
        # Create the folders in the parent folder directory
        for folder in folders:
            if not os.path.exists(folder):
                os.mkdir(folder)
            else:
                print("Folder: %s exists" % folder)
        print("Finished creating folders week1-12! Exiting!")
    else:
        print("Can't change the Current Working Directory")


def function2():
    """cd to the directory create a parent folder name, enter the number of folders to create and
    individually name the [sub folders]"""
    # Print the current directory before change
    print("Current Working Directory: ", os.getcwd())
    # Prompt user for the directory
    directory = input("Specify the directory to change to: ")
    # Check if new path exists
    if os.path.exists(directory):
        # Change the current working Directory
        os.chdir(directory)
        print("Current Working Directory: ", os.getcwd())
        # Get the parent folder name from the user
        parent_folder = input("Enter the parent folder name: ")
        # Check if directory already exists
        if not os.path.exists(parent_folder):
            os.mkdir(parent_folder)
            print("Creating parent folder: %s" % parent_folder)
        # Change to parent folder directory
        print("Changing to the directory: %s" % parent_folder)
        os.chdir(parent_folder)
        # Create the folders in the parent folder directory
        # Get the amount of folders to create from the user
        i = 1
        n = int(input("Enter the number of sub folders you want to create in the directory: "))
        if n > 0:
            while i <= n:
                folder = input("Enter the name for sub folder %d: " % i)
                if not os.path.exists(folder):
                    os.mkdir(folder)
                else:
                    print("Folder: %s exists" % folder)
                i += 1
        else:
            print("Exiting! The number is not greater than 0.")
            sys.exit(1)
        print("Finished creating folders! Exiting!")
    else:
        print("Can't change the Current Working Directory")


if __name__ == "__main__":
    print("1 - cd to dir create parent folder then create [week]1-12 sub folders")
    print("2 - cd to dir create parent folder, specify the amount of folders and individually name [sub folders]")
    # Get a number from the user
    method = input("Choose a method 1 or 2: ")
    # Check the selected number
    if method.isdigit():
        if method == '1' or method == '2':
            print("method is a Number", method)
            # Check for the function number
            if method == '1':
                function1()
            if method == '2':
                function2()
        else:
            print("The number must be 1 or 2. Your number is:", method)
    else:
        print("Enter a number to continue.Exiting!")
