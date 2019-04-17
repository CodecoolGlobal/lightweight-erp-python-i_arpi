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
    abc = 'abcdefghijklmnopqrstvwxyz'
    upper_abc = abc.upper()
    special_characters = '&£$@€~^©–#$*÷%+!?:'
    numbers = '0123456789'
    end_part = ''
    while True:
        for i in range(2):
            abc_index = random.randint(0, len(abc)-1)
            upper_index = random.randint(0, len(upper_abc)-1)
            special_index = random.randint(0, len(special_characters)-1)
            numbers_index = random.randint(0, len(numbers)-1)
            
            char_from_abc = abc[abc_index]
            char_from_upper = upper_abc[upper_index]
            char_from_special = special_characters[special_index]
            char_from_numbers = numbers[numbers_index]

            generated += char_from_abc + char_from_upper +char_from_numbers + char_from_special

        for row in table:
            if row[0] != generated:
                return generated

def choose(features):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    features[option]


def add(table, label_list, title):
    sliced_label_list = label_list[1:]
    new_record = ui.get_inputs(sliced_label_list, title)
    new_row = [generate_random(table)] + new_record
    table.append(new_row)
    ui.print_table(table, label_list)


def remove(table, id_):
    for row in table:
        if str(row[0]).strip() == id_.strip():
            table.remove(row)
    
    
    
def update(table, id_, label_list):
    updated_record = []
    for row in table:
        if str(row[0]).strip() == str(id_).strip():
            updated_record.append(id_)
            table.remove(row)
            updating_record = ui.get_inputs(label_list[1:], 'Give new data:')
            updated_record.append(updating_record)
            table.append(updated_record)
        






