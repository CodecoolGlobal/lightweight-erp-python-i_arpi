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
    headers = [ 'Id ',
        'Name ',
        'Email ',
        'Subscribed ']
    return headers

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # your code
    ui.print_table(table, get_headers())

    


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    title_list = get_headers()
    common.add(table, title_list, 'Give new costumers\'s data, please!')
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
    ui.print_table(table, get_headers())
    


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
    common.update(table, id_, get_headers())
    


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
    longest_so_far = ''
    for row in table: 
        if len(row[2]) > len(longest_so_far):
            longest_so_far = row[2]
            longests_id = row[1]
    return longest_so_far

    
    


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
    subscribed_emails = []
    for row in table:
        subscription = int(row[3])
        if subscription == 1:
            email = row[2]
            email_name = email + ';' + row[1]
            subscribed_emails.append(email_name)
    return subscribed_emails

def choose(table):
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        id_ = ui.get_inputs(['id'], "Give id:")[0]
        remove(table, id_)
    elif option == "4":
        id_ = ui.get_inputs(['id'], "Give id:")[0]
        update(table, id_)
    elif option == "5":
        ui.print_result(get_longest_name_id(table), "The customer's ID with the longest name is: ")
    elif option == "6":
        ui.print_result(get_subscribed_emails(table), "The customers who has subscribed to the newsletter are: ")
    elif option == "0":
        raise EnvironmentError
    else:
        raise KeyError("There is no such option.")

def get_options():
    options = ['Show costumer\'s data',
        'Add new costumers',
        'Remove costumer',
        'Update costumer\'s data',
        "Show costumer's ID with the longest name",
        'Emails of subscripted costumers' ]
    return options

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file('crm/customers.csv')
    while True:
        ui.print_menu("CRM Menu", get_options(), "Go back to main menu")
        try:
            choose(table)
        except KeyError as err:
            ui.print_error_message(str(err))
        except EnvironmentError:
            return

"""
def get_features():
    
    features = {"0" : sys.exit(),
        "1" : show_table(tabel), 
        "2" : add(table),
        "3" : id_ = ui.get_inputs(['id_number'], "Give id:") remove(table, id_[0]),
        "4" : id_ = ui.get_inputs(['id_number'], "Give id:") update(table, id_[0]),
        "5" : get_longest_name_id(table),
        "6" : get_subscribed_emails(),
        }
        return features
        """
