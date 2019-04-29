""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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

    table = data_manager.get_table_from_file('store/games.csv')

    while True:
        ui.print_menu('Store module', get_options(), 'Back to main menu')
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
        ui.print_result(get_counts_by_manufacturers(table), 'The amount of games available per genre in store by manufacturers are: ')
    elif option == "6":
        try:
            manufacturer = ui.get_inputs(['manufacturer: '], "Please, specify the manufacturer.")
            ui.print_result(get_average_by_manufacturer(table, manufacturer[0])  , 'The average amount of games per genre in stock by the given manufacturer is: ')
        except ZeroDivisionError:
            message = "Sorry, no manufacturer by that name."
            ui.print_error_message(message)
    elif option == "0":
        return 'return'
    else:
        raise KeyError("There is no such option.")


def get_options():
    options = ["Display store table",
               "Add an item",
               "Remove an item",
               "Update store table",
               "Show the amount of games per genre available in store by manufacturers",
               "Show average amount of games per genre in stock by given manufacturer"]
    return options


def get_headers():
    headers = ["ID ",
               "Title ",
               "Manufacturer ",
               "Price ",
               "In stock "]
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


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    common.update(table, id_, get_headers())
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    
    '''
    games = {}
    manufacturers = set(row[2] for row in table)
    for manufacturer in manufacturers:
        count = 0
        for row in table:
            if manufacturer == row[2]:
                count += 1
                games.update({row[2]: count})
    return games
    '''

    games = {}
    for row in table:
        if row[2] in games.keys():
            games[row[2]] += 1
        else:
            games[row[2]] = 1
    return games


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
   
    count = 0
    games = 0
    for row in table:
        if manufacturer == row[2]:
            games += int(row[4])
            count += 1
    return games / count

