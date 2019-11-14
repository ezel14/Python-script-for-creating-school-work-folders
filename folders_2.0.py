import os
import sys
import shutil
from pathlib import Path


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
                    print("Created folder %s: " % folder)
                else:
                    print("Folder: %s already exists" % folder)
                i += 1
        else:
            print("Exiting! The number is not greater than 0.")
            sys.exit(1)
        print("Finished creating folders! Exiting!")
    else:
        print("Can't change the Current Working Directory")


def function3():
    """cd to the directory and create a single parent folder"""
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
            print("Finished creating folder! Exiting!")


def function4():
    """Create folders in different directories"""
    f = '1'
    while f == '1':
        # Print the current directory before change
        print("Current Working Directory: ", os.getcwd())
        # Prompt user for the directory
        directory = input("Specify the directory to change to: ")
        # Check if new path exists
        if os.path.exists(directory):
            # Change the current working Directory
            os.chdir(directory)
            print("Current Working Directory: ", os.getcwd())
            # Create the folders in the directory
            # Get the amount of folders to create from the user
            # Initialise a counter
            i = 1
            n = int(input("Enter the number of folders you want to create in the directory: "))
            if n > 0:
                while i <= n:
                    folder = input("Enter the name for the folder %d: " % i)
                    if not os.path.exists(folder):
                        os.mkdir(folder)
                        print("Created folder %s: " % folder)
                    else:
                        print("Folder: %s already exists" % folder)
                    i += 1
            else:
                print("The number is not greater than 0.")
            print("Finished creating folders!")
            # Prompt user to continue or exit
            f = input("1 ~ Continue creating folders. "
                      "2 ~ Exit ")
        else:
            print("Unable change the Current Working Directory")


def function5():
    """Remove a directory to the recycling bin"""
    f = '1'
    while f == '1':
        # Print the current directory
        print("Current Working Directory: ", os.getcwd())
        # Prompt user for the directory
        directory = input("Specify the directory to change to: ")
        for path in Path(directory).iterdir():
            print(path)
        remove = input("Specify the directory to remove: ")
        shutil.rmtree(remove)
        print("Directory moved to Recycle Bin")
        # Prompt user to continue or exit
        print("1 ~ Remove another directory")
        print("2 ~ Exit")
        f = input(": ")


def function6():
    """Rename folders in different directories"""
    # Print the current directory before change
    print("Current Working Directory: ", os.getcwd())
    # Prompt user for the directory
    directory = input("Specify the directory to change to: ")
    # Check if new path exists
    if os.path.exists(directory):
        f = '1'
        while f == '1':
            os.chdir(directory)
            # listing directories
            print("The dir is: %s\n" % os.listdir(os.getcwd()))
            src = input("Specify the src: ")
            dst = input("Specify the dst: ")
            # renaming directory
            os.rename(src, dst)
            print("Successfully renamed.")
            # listing directories after renaming
            print("the dir is: %s\n" % os.listdir(os.getcwd()))
            # Prompt user to continue or exit
            print("1 ~ Rename another")
            print("2 ~ Exit")
            f = input(": ")
    else:
        print("Can't change the Current Working Directory")


if __name__ == "__main__":
    # Initialise method
    method = '0'
    # Run while method is not equal to 4
    while method != '7':
        print("*******************************************************************************************************")
        print("* 1 ~ Cd to dir create parent folder then create [week]1-12 sub folders                               *")
        print("* 2 ~ Cd to dir create parent folder and individually name[sub folders]                               *")
        print("* 3 ~ Create a directory folder                                                                       *")
        print("* 4 ~ Create folders in different directories                                                         *")
        print("* 5 ~ Remove a directory to the recycling bin                                                         *")
        print("* 6 ~ Rename a directory                                                                              *")
        print("* 7 ~ Exit the program                                                                                *")
        print("*******************************************************************************************************")
        # Get a number from the user
        method = input("Select a function: ")
        # Check the selected number
        if method.isdigit():
            if method == '7':
                print("Method %s selected exiting program" % method)
            if method == '1' or method == '2' or method == '3' or method == '4' or method == '5' or method == '6':
                print("You have selected method", method)
                # Check for the function number
                if method == '1':
                    function1()
                if method == '2':
                    function2()
                if method == '3':
                    function3()
                if method == '4':
                    function4()
                if method == '5':
                    function5()
                if method == '6':
                    function6()
        else:
            print("Please enter a function number to continue.")
