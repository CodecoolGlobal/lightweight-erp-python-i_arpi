""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
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

    table = data_manager.get_table_from_file('inventory/inventory.csv')

    while True:
        ui.print_menu('Inventory Module', get_options(), 'Back to main menu')
        try:
            if choose(table) == 'return':
                return
        except KeyError as err:
            ui.print_error_message(str(err))


def choose(table):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(['id: '], "Give id.")
        remove(table, id_[0])
    elif option == "4":
        id_ = ui.get_inputs(['id: '], "Give id.")
        update(table, id_[0])
    elif option == "5":
        ui.print_result(get_available_items(table), 'The still available items are: ')
    elif option == "6":
        ui.print_result(get_average_durability_by_manufacturers(table), 'The average durability times by manufacturers are: ')
    elif option == "0":
        return 'return'
    else:
        raise KeyError("There is no such option.")


def get_options():
    options = ["Display inventory table",
               "Add an item",
               "Remove an item",
               "Update inventory table",
               "Show the available items",
               "Show average durability times for each manufacturer"]
    return options


def get_headers():
    headers = ["ID ",
               "Name ",
               "Manufacturer ",
               "Purchase Year ",
               "Durability "]
    return headers


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, get_headers())


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    common.add(table, get_headers(), "Give new inventory item's data, please!")
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

    common.remove(table, id_)
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

    common.update(table, id_, get_headers())
    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """
    available = []
    year = 2016
    for row in table:
        row[3], row[4] = int(row[3]), int(row[4])
        if (row[3] + row[4]) >= year:
            available.append(row)
    return available




def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    manufacturers = set(row[2] for row in table)
    result = {}
    for item in manufacturers:
        sum_durability = 0
        count = 0
        for row in table:
            if item == row[2]:
                row[4] = int(row[4])
                sum_durability += row[4]
                count += 1
                avg_durability = float(sum_durability / count)
                result.update({row[2]: avg_durability})
    return result



