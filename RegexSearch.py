# Automate the boring stuff with Python.
# Chapter 8, Reading and Writing Files
# Regex Search
#
# Write a program that opens all .txt files in a folder and searches
# for any line that matches a user-supplied regular expression. The results
# should be printed to the screen.

import os
import re


def set_dir():
    while True:
        target = input("Enter the path of the directory to by searched (leave blank for default path):")

        if target is '':
            os.chdir("./default")
            print("Using directory: ", os.getcwd())
            break
        elif os.path.isdir(target):
            os.chdir(target)
            print("Using directory: ", os.getcwd())
            break
        else:
            print('Invalid path!')


def set_search_re():
    search_expression = input('Enter your search term(RegEx): ')
    search_expression = re.compile(search_expression)
    return search_expression


def set_list_of_txt_files():
    files = os.listdir()
    text_files = files.copy()

    i = 1

    for file in files:
        print('Found file {} of {}: '.format(i, len(files)), file)
        i += 1
        if not file.endswith('.txt'):
            print('File {} is not a text file. '.format(file), 'Removed.')
            text_files.remove(file)
        else:
            print('File {} is a text file. '.format(file), 'Retained."')
    return text_files


def search_txt_files(files, term):
    matches = []
    for file in files:
        fin = open(file, 'r')

        lines = fin.readlines()
        for line in lines:
            match = term.search(line)
            if match:
                matches.append(line)
        fin.close()

    return matches


def main():
    # pick directory to be searched
    set_dir()

    files = set_list_of_txt_files()

    # get the user supplied regex
    search_re = set_search_re()

    # use the search regex on the list of files
    # capture the matching lines as a list
    matching_lines = search_txt_files(files, search_re)

    print(matching_lines, end='\n')


if __name__ == '__main__':
    main()
