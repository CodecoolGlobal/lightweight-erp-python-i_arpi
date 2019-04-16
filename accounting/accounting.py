""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    table = data_manager.get_table_from_file('items.csv')
    for row in table:
        row[1] = int(row[1])
        row[2] = int(row[2])
        row[3] = int(row[3])
        row[5] = int(row[5])

    while True:
        common.display_menu(get_options, 'Accounting Manager')
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(['id'], "Give id:")
        remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(['id'], "Give id:")
        update(table, id_)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        year = ui.get_inputs(['year: '], "Please, specify a year.")
        avg_amount(table, year)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")



def get_options():
    options = ["Display cash-flow table",
               "Add an item",
               "Remove an item",
               "Update cash-flow table",
               "Show the year with the highest profit",
               "Show the average profit in a given year",
               "Go back to main menu"]
    return options


def get_headers():
    headers = ["ID",
               "Month",
               "Day",
               "Year",
               "Type",
               "Amount"]
    return headers


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    common.show_table(table, get_headers())
    


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    common.add(table, get_headers, "Give new costumer's data, please!")
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

    '''
    table = data_manager.get_table_from_file('items.csv')
    ui.get_inputs(['ID: ', 'Which item do you want to change: ', 'What data would you like to store: '], 'Please, type in the ID of the transaction which you want to update.')
    for row in table:
        row[inputs[1]] = inputs[2]
    return table
    '''


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    same_year_transactions = []
    same_year_transactions_in = []
    same_year_transactions_out = []
    income = 0
    loss = 0
    for row in table:
        if row[3] == year:
            same_year_transactions.append(row)
    for row in same_year_transactions:
        if row[4] == 'in':
            same_year_transactions_in.append(row)
    for row in same_year_transactions_in:
        income += same_year_transactions_in[5]
    for row in same_year_transactions:
        if row[4] == 'out':
            same_year_transactions_out.append(row)
    for row in same_year_transactions_out:
        loss += same_year_transactions_out[5]
    avg_profit = (income - loss) / len(same_year_transactions)
    return avg_profit

