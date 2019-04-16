""" Common module
implement commonly used functions here
"""

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

def display_menu(options, menu_name):
     
     ui.print_menu(menu_name, options, "Exit menu.")

def show_table(table, title_list):
    
    ui.print_table(table, title_list)

def add(table, label_list, title):
    new_record = ui.get_inputs(label_list, title)
    table.append(new_record)





