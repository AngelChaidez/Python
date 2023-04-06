#!/usr/bin/env python3.11



# list all files, directories and subdirectories's files in a given directory source of help for this 
# from stackoverflow: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files

def list_files_recursive(directory, files, recursive_dictionary):
    print("Printing files and directories recursively")
    for root, dirs, files in os.walk(directory):
        for file in files:
            recursive_dictionary[root + "/" + file] = file
    print(seperator, recursive_dictionary, '\n',seperator)
    



# List all files and filesizes in a user provided directory. We will use the os.walk() function to walk through our 
# directory and list all files and their sizes. size_of_file() will return the size of the file in bytes, and the 
# directory[files[0]] will update our dictionary with the name of the file and the corresponding size of the file.
# REFERENCES: 
# https://www.geeksforgeeks.org/how-to-get-file-size-in-python/

def list_directory_files(directory):
    print("Printing your files and sizes in directory:" , directory)
    files = os.listdir(directory)
    files.sort()
    dictionary = {}
    for files in os.walk(directory):
        size_of_file = os.path.getsize(files[0])
        dictionary[files[0]] = size_of_file
    print(seperator, dictionary, '\n',seperator)


def print_dict_as_json(dictionary):
    print("Printing dictionary as json:")
    print(seperator, json.dumps(dictionary, indent=4, sort_keys=True), seperator)


def print_dict_with_keys(dictionary):
    print("Printing dictionary with keys:")
    new_dictionary = {"files": dictionary.keys(), "sizes": dictionary.values()}
    print(seperator, next(iter(new_dictionary.items())), '\n',seperator)


# Create a dictionary with list of files from a given directory, and print to the screen.
# Users can use this dictionary to list all files in a directory. Users will be given 



if __name__ == "__main__":
    import os
    import sys
    import json
    

    
    # Create a dictionary with list of files from a given directory, and print to the screen.
    # Users can use this dictionary to list all files in a directory. Users will be given 
    
    dictionary = {}
    recursive_dictionary = {}
    directory = input("Please enter the directory you want to list the files in: ")
    directory = os.path.abspath(directory)
    seperator = "======================================================================================================================================================================="
    
    # Check if provided path exists, if not resort to using the current directory with the os.getcwd() function
    if not os.path.exists(directory):
        directory = os.getcwd()
        print("The directory you entered does not exist.")
        print("Will resort to using your current working directory")
        print(directory, ":", '\n')
        files = os.listdir(directory)
        files.sort()
        for file in files:
            size_of_file = os.stat(file).st_size
            dictionary[file] = size_of_file
        print(seperator, dictionary, '\n',seperator)
        print_dict_as_json(dictionary)
        quit() # Exit the program and not process any further files

    # Create a list of all of the files in the directory with os.listdir() commmand, and sort it. We will then call our two functions
    # 1) to list the directory files and their sizes, and then print to the screen and 2)to list the files and their sizes in the directory
    # recursively, which will print all of the subdirectories as well.

    files = os.listdir(directory)
    files.sort()
    list_directory_files(directory)
    list_files_recursive(directory, files, recursive_dictionary)
    print_dict_with_keys(dictionary)
    

    # Uncomment the following to have both the files only dictionary print in json formatting and/or have the recursive dictionary print in 
    # json formatting. WARNING: This will take up all of your screen if you have directories will large amount of directories/subdirectories
    # and files. YOU HAVE BEEN WARNED 

    #print_dict_as_json(dictionary)
    #print_dict_as_json(recursive_dictionary)
   




