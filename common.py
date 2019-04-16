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

def read_in_data_from_file(file_name):
    table = []
    with open(file_name) as file:
        for row in file:
            datas_in_row = row.strip().split(';')
            table.append(datas_in_row)
    return table


