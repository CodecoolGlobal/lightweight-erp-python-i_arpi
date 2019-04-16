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

    options = ["Display cash-flow table",
               "Add an item",
               "Remove an item",
               "Update cash-flow table"]

    ui.print_menu("Accounting Manager", options, "Back to main menu")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ['ID', 'Month', 'Day', 'Year of transaction', 'Type', 'Amount']
    accounting_data = data_manager.get_table_from_file('items.csv')
    for datas in accounting_data:
        datas[1] = int(datas[1])
        datas[2] = int(datas[2])
        datas[3] = int(datas[3])
        datas[5] = int(datas[5])
    ui.print_table(accounting_data, title_list)



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    input_data = []
    input_data[0] = common.generate_random(table)
    ui.get_inputs(['Month of the transaction: ', 'Day of the transaction: ', 'Year of the transaction: ', 'Type of the transaction (in or out): ', 'Amount of transaction in USD: '], 'Please provide data for adding a transaction')
    input_data.append(inputs)
    table.append(input_data)
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

    ui.get_inputs(['ID: '], 'Please, type in the ID of the transaction which you want to delete.')
    for row in table:
        if inputs[0] == row[0]:
            table.remove(row)
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
    table = data_manager.get_table_from_file('items.csv')
    ui.get_inputs(['ID: ', 'Which item do you want to change: ', 'What data would you like to store: '], 'Please, type in the ID of the transaction which you want to update.')
    for row in table:
        row[inputs[1]] = inputs[2]
    return table


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
    count = 0
    losss = 0
    for row in table:
        if row[3] == year:
            same_year_transactions.append(row)
    for row in same_year_transactions:
        if row[4] == 'in':
            same_year_transactions_in.append(row)
    for row in same_year_transactions_in:
        count += same_year_transactions_in[5]
    for row in same_year_transactions:
        if row[4] == 'out':
            same_year_transactions_out.append(row)
        loss += same_year_transactions_out[5]
    avg = (count - loss) / len(same_year_transactions)
    return avg

