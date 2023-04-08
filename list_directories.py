#!/usr/bin/env python3.11



# list all files, directories and subdirectories's files in a given directory source of help for this 
# from stackoverflow: https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
# this function will not print out with formatted keys and values instead the keys are the path of the file 
# and the values are the name of the file

def list_files_recursive(directory, files, recursive_dictionary):
    print("Printing files and directories recursively with keys as fullpath and filename:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            recursive_dictionary[root + "/" + file] = file
    print(seperator, recursive_dictionary, '\n',seperator)
    print(type(recursive_dictionary))
    print_dict_as_json(recursive_dictionary)
    return recursive_dictionary
    



# List all files and filesizes in a user provided directory. We will use the os.walk() function to walk through our 
# directory and list all files and their sizes. size_of_file() will return the size of the file in bytes, and the 
# directory[files[0]] will update our dictionary with the name of the file and the corresponding size of the file.
# REFERENCES: 
# https://www.geeksforgeeks.org/how-to-get-file-size-in-python/

def list_directory_files(directory):
    print("Printing your files and sizes only in directory:" , directory )
    print("with keys {filename: size_of_file:}")
    files = os.listdir(directory)
    files.sort()
    list_dictionary = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            size_of_file = os.path.getsize(root + "/" + file)
            dictionary = {"file": file, "size": size_of_file}
            list_dictionary.append(dictionary)
    print(seperator, list_dictionary, '\n',seperator)
    print(type(list_dictionary))
    #print_dict_as_json(list_dictionary)   #uncomment this line if you want to print the dictionary as json file
    
  


def print_dict_as_json(dictionary):
    print("Printing dictionary as json:")
    print(seperator, json.dumps(dictionary, indent=4, sort_keys=True), seperator)


def print_dict_with_keys(directory):
    print("Printing dictionary with keys in format of {path: filename: size_of_file:} as keys")
    files = os.listdir(directory)
    files.sort()
    list_dictionary = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            size_of_file = os.path.getsize(root + "/" + file)
            new_dictionary = {"path": root, "filename": file, "size": size_of_file}
            list_dictionary.append(new_dictionary)
    print(seperator, list_dictionary, '\n', seperator)
    print(type(list_dictionary))
    #print_dict_as_json(list_dictionary) #uncomment if you would like you list also in json format
    return list_dictionary

# This function is suppose to turn a list into a dictionary, and return the dictionary
# however, I could not get this to work, if anyone could help me with this function

def convert_list_to_dictionary(list_of_dictionary):
    print("Converting list to dictionary:")
    pairs = itertools.zip_longest(*[iter(list_of_dictionary)]*2, fillvalue=None)
    dictionary_from_list = {key: value for key, value in pairs}
    return dictionary_from_list


# Create a dictionary with list of files from a given directory, and print to the screen.
# Users can use this dictionary to list all files in a directory. Users will be given 



if __name__ == "__main__":
    import os
    import sys
    import json
    import itertools
    

    
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
        print(type(dictionary))

        print(convert_list_to_dictionary(dictionary))
        list_directory_files(directory)
        #print_dict_as_json(dictionary) # uncomment if you would like you list also in json format
        quit() # Exit the program and not process any further files

    # Create a list of all of the files in the directory with os.listdir() commmand, and sort it. We will then call our two functions
    # 1) to list the directory files and their sizes, and then print to the screen and 2)to list the files and their sizes in the directory
    # recursively, which will print all of the subdirectories as well.

    files = os.listdir(directory)
    files.sort()
    #list_directory_files(directory)
    #print_dict_with_keys(directory)
    list_files_recursive(directory, files, recursive_dictionary)

    #dictionary = print_dict_with_keys(directory)

    #convert_list_to_dictionary(dictionary)
    # Convert the dictionary to a list of dictionaries, and print to the screen.
    

    
   




