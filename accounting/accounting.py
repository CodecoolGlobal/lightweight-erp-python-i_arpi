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

    table = data_manager.get_table_from_file('accounting/items.csv')
    '''
    for row in table:
        row[1] = int(row[1])
        row[2] = int(row[2])
        row[3] = int(row[3])
        row[5] = int(row[5])
    '''

    while True:
        ui.print_menu('Accounting Manager', get_options(), 'Back to main menu')
        try:
            if choose(table) != 'return':
                choose(table)
            else:
                return
        except KeyError as err:
            ui.print_error_message(str(err))
            '''
        except EnvironmentError:
            return
            '''


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
        ui.print_result(which_year_max(table), 'The year with the highest profit is: ')
    elif option == "6":
        try: 
            year = ui.get_inputs(['year: '], "Please, specify a year.")
            year_int = int(year[0])
            ui.print_result(avg_amount(table, year_int), "The average profit for the given year is: ")
        except ZeroDivisionError:
            message = "Sorry, no transactions in that year."
            ui.print_error_message(message)
    elif option == "0":
        return "return"
        # raise EnvironmentError
    else:
        raise KeyError("There is no such option.")



def get_options():
    options = ["Display cash-flow table",
               "Add an item",
               "Remove an item",
               "Update cash-flow table",
               "Show the year with the highest profit",
               "Show the average profit in a given year"]
    return options


def get_headers():
    headers = ["ID ",
               "Month ",
               "Day ",
               "Year ",
               "Type ",
               "Amount "]
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

    common.add(table, get_headers(), "Give new costumer's data, please!")
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

    year_profit = {}
    for row in table:
        year = row[3]
        if year in year_profit and row[4] == 'in':
            year_profit[year] += int(row[5])
        elif year in year_profit and row[4] == 'out':
            year_profit[year] -= int(row[5])
        elif year not in year_profit and row[4] == 'in':
            year_profit.update({year: int(row[5])})
        elif year not in year_profit and row[4] == 'out':
            row[5] = -int(row[5])
            year_profit.update({year: row[5]})
    highest_year = max(year_profit, key=lambda year: year_profit[year])
    return int(highest_year)

        

def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    
    profit = 0
    item_count = 0
    for row in table:
        row[3] = int(row[3])
        if row[3] == year and row[4] == 'in':
            profit += int(row[5])
            item_count += 1
        elif row[3] == year and row[4] == 'out':
            profit -= int(row[5])
            item_count += 1
    return profit / item_count

    

   
    
    

         
    
        




