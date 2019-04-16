""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def get_headers():
    headers = [ 'Id',
        'Name',
        'Email',
        'Subscribed']
    rerutn headers

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # your code
   common.show_table(table, get_headers())

    


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    common.add(table, get_headers, 'Give new costumers\s data, please!')
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

    # your code
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

    # your code
    common.update(table, id_, get_header())
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code

def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs([id], "Give id:")
        remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs([id], "Give id:"
        update(table, id_)
     elif option == "5":
        get_longest_name_id(table)
    elif option == "6":
        get_subscribed_emails(table)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

def get_options():
    options = ['Show cosumer\'s data',
        'Add new costumers',
        'Remove costumer'
        'Update costumer\'s data',
        'Show costumer with longest name',
        'Emails of subscripted costumers', 
        'Go back to main menu']
    return options

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file(customers.csv)
    while True:
        common.display_menu(get_options, 'CRM Menu')
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))

def get_features():
    
    feautures = [show_table]
