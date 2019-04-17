""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
import sys
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ["Display a table"
    "Add a new person",
    "Remove person",
    "Update infomation",
    "Who is the oldest?",
    "Who is the closest to the avarage age?"]

    table = data_manager.get_table_from_file("hr/persons_test.csv")
    ui.print_menu
    option = ui.get_inputs(["Please enter a number: "], "")
    if option[0] == "1":
        show_table(table)
    elif option[0] == "2":
        table = add(table)
    elif option[0] == "3":
        show_table(table)
        id_ = ui.get_inputs(['Please type ID to remove: '], "\n")
        table = remove(table, id_)
    elif option[0] == "4":
        show_table(table)
        id_ = ui.get_inputs(["Please type ID to update: "], "\n")
        table = update(table, id_)
    elif option[0] == "5":
        ui.print_result(get_oldest_person(table), "The oldest person is: ")
    elif option[0] == "6":
        ui.print_result(get_persons_closest_to_average(table), "People closest to average age: ")
    elif option[0] == "0":
        sys.exit()
    else:
        ui.print_error_message("There is no such an option.")


def show_menu_hr():
    ui.print_show_menu_hr("HR menu", options, "Enter a number: ")

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    title_list = ['ID', 'Name', 'Birth date']
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    year = int(table[0][2])
    people_list = []
    for component in table:
        if int(component[2]) < year:
            year = int(component[2])
            people_list[0] = component[1]
        elif int(component[2]) == year:
            year = int(component[2])
            people_list.append(component[1])
    return people_list


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
    years = []
    for component in table:
        years.append(int(component[2]))
        a = 0
    for component in years:
        a += int(component)
    average_of_years = float(a)/int(len(years))
    first_person = int(table[0][2])
    people_list = []
    for component in table:
        if abs(int(component[2]) - average_of_years) < abs(first_person - average_of_years):
            first_person = int(component[2])
            people_list[0] = component[1]
        elif abs(int(component[2]) - average_of_years) == abs(first_person - average_of_years):
            first_person = int(component[2])
            people_list.append(component[1])
    return people_list 