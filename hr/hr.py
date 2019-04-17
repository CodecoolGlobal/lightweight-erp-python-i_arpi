import sys
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    table = data_manager.get_table_from_file("hr/persons.csv")
    while True:
        ui.print_menu("HR menu", get_options(), "Go back to main menu")
        try:
            choose(table)
        except KeyError as err:
            ui.print_error_message(str(err))

##

def choose(table):
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

def get_options():
    options = ["Display a table",
    "Add a new person",
    "Remove person",
    "Update infomation",
    "Who is the oldest?",
    "Who is the closest to the avarage age?"]
    return options

def get_label_list():
    labels = ['ID', 'Name: ', 'Birth year: ']
    return labels


def show_table(table):
    title_list = ['ID', 'Name', 'Birth date']
    ui.print_table(table, title_list)


def add(table):
    common.add(table, get_label_list(), 'Give new data:')
    return table


def remove(table, id_):
    common.remove(table, id_)
    return table


def update(table, id_):
    common.update(table, id_, get_label_list())
    return table

# special functions:
# ------------------

def get_oldest_person(table):
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