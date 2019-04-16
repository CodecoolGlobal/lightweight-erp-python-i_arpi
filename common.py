""" Common module
implement commonly used functions here
"""
import ui
import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # your code

    return generated

def choose(features):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    features[option]

def display_menu(options, menu_name):
     
     ui.print_menu(menu_name, options, "Exit menu.")

def show_table(table, title_list):
    
    ui.print_table(table, title_list)

def add(table, label_list, title):
    new_record = ui.get_inputs(label_list, title)
    new_row = [generate_random(table)] + new_record
    table.append(new_row)


def remove(table, id_):
    for row in table:
        if row[0] == id_:
            table.remove(row)
<<<<<<< HEAD
    
=======


>>>>>>> d2c71bb88749d7b221048db44a301ec7b7b83535
def update(table, id_, label_list):
    for row in table:
        if row[0] == id_:
            updating_record = ui.get_inputs(label_list, 'Give new data:')
            row = row[0] + updating_record
        






