""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

    table = data_manager.get_table_from_file('sales/sales.csv')

    while True:
        ui.print_menu('Sales module', get_options(), 'Back to main menu')
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
        ui.print_result(get_lowest_price_item_id(table), 'The ID of the game sold for the lowest price is: ')
    elif option == "6":
        dates= ui.get_inputs(['month from: ', 'day from: ', 'year from: ', 'month to: ', 'day to: ', 'year to: '], "Please specify the time intervallum.")
        ui.print_result(get_items_sold_between(table, int(dates[0]), int(dates[1]), int(dates[2]), int(dates[3]), int(dates[4]), int(dates[5])), 'The games sold between the two given dates are: ')
    elif option == "0":
        return 'return'
    else:
        raise KeyError("There is no such option.")


def get_options():
    options = ["Display sales table",
               "Add an item",
               "Remove an item",
               "Update sales table",
               "Show the ID of the game sold for the lowest price",
               "Show the games sold between two given dates"]
    return options


def get_headers():
    headers = ["ID ",
               "Title ",
               "Price ",
               "Month ",
               "Day ",
               "Year "]
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

    common.add(table, get_headers(), "Give new item's data, please!")
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

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    lowest = int(table[0][2])
    for row in table:
        row[2] = int(row[2])
        if lowest > row[2]:
            lowest = row[2]
            id = row[0]
    return id



def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    
    result = []
    for row in table:
        row[2], row[3], row[4], row[5] = int(row[2]), int(row[3]), int(row[4]), int(row[5])
        if (row[5] >= year_from and row[3] > month_from) and (row[5] <= year_to and row[3] < month_to):
            result.append(row)
        elif (row[5] >= year_from and row[3] == month_from and row[4] > day_from) and (row[5] <= year_to and row[3] == year_to and row[4] < year_to): 
            result.append(row)
    return result

