""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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
    elif option == "7":
        id= ui.get_inputs(['id: '], "Give id.")
        ui.print_result(get_title_by_id_from_table(table, id[0]), 'The name of the game with the given ID is: ')
    elif option == "8":
        ui.print_result(get_item_id_sold_last_from_table(table), 'The ID of the game sold most recently is: ')
    elif option == "9":
        ui.print_result(get_item_title_sold_last_from_table(table), 'The title of the game sold most recently is: ')
    elif option == "10":
        item_ids = ui.get_inputs(['id: ', 'id: ', 'id: ', 'id: '], "Give the ids.")
        ui.print_result(get_the_sum_of_prices_from_table(table, item_ids), 'The overall price of the games with the given IDs: ')
    elif option == "11":
        id = ui.get_inputs(['id: '], "Give sales id.")
        ui.print_result(get_customer_id_by_sale_id_from_table(table, id[0]), 'The ID of the customer with the given sale ID is: ')
    elif option == "12":
        ui.print_result(get_all_customer_ids(table),'The costumer IDs in table are: ')
    elif option == "13":
        ui.print_result(get_all_sales_ids_for_customer_ids_from_table(table),'The sales IDs for the customer IDs are: ')
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
               "Show the games sold between two given dates",
               "Show the name of a game by a given ID",
               "Show the ID of the game sold most recently",
               "Show the title of the game sold most recently",
               "Show the overall price of the games with the given IDs",
               "Show the ID of the customer with the given sale ID",
               "Show all customer ID's",
               "Show all sales IDs for the customer IDs"]
    return options


def get_headers():
    headers = ["ID ",
               "Title ",
               "Price ",
               "Month ",
               "Day ",
               "Year ",
               "Customer ID"]
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
            result.append(row[:6])
        elif (row[5] >= year_from and row[3] == month_from and row[4] > day_from) and (row[5] <= year_to and row[3] == year_to and row[4] < year_to): 
            result.append(row[:6])
    return result


    # your code


# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    for row in table:
        if id == row[0]:
            return row[1]



def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    for row in table:
        if id == row[0]:
            return row[1]


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    table = data_manager.get_table_from_file('sales/sales.csv')
    return get_item_id_sold_last_from_table(table)

def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code
    max = 0

    for i in table:
        i[5] = int(i[5])

        
        if int(i[5]) > max:
            max = i[5]

    

        if int(i[5]) > max:
            max = i[5]


    
    max_year_games = []

    for i in table:
        if int(i[5]) == max:
            max_year_games.append(i)
        

    


    
    ######################
    max = 0
    for i in max_year_games:
        i[3] = int(i[3])

        

        if int(i[3]) > max:
            max = i[3]

    max_month_games = []

    for i in max_year_games:
        if int(i[3]) == max:
            max_month_games.append(i)

    


    ######################
    max = 0
    for i in max_month_games:
        i[4] = int(i[4])

        

        if int(i[4]) > max:
            max = i[4]

    max_day_games = []

    for i in max_month_games:
        if int(i[4]) == max:
            max_day_games.append(i)
    

    

    return(max_day_games[0][0])
    #return "kH34Ju#&"


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """
    max_date = []
    year = int(table[0][5])
    month = int(table[0][3])
    day = int(table[0][4])
    for row in table:
        row[3], row[4], row[5] = int(row[3]), int(row[4]), int(row[5])
        if row[5] >= year:
            max_date.append(row[5])
        if row[3] >= month and row[5] == max_date[0]:
            max_date.append(row[3])
        if row[4] >= day and row[5] == max_date[0] and row[3] == max_date[1]:
            max_date.append(row[4])
        if row[5] == max_date[0] and row[3] == max_date[1] and row[4] == max_date[2]:
            return row[1]
            



def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """
    table = data_manager.get_table_from_file('sales/sales.csv')
    result = 0
    for element in item_ids:
        for row in table:
            row[2] = int(row[2])
            if element == row[0]:
                result += row[2]
    return result

    


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    result = 0
    for element in item_ids:
        for row in table:
            row[2] = int(row[2])
            if element == row[0]:
                result += row[2]
    return result


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    try:
        for row in table:
            if sale_id == row[0]:
                result = row[6]
        return result
    except UnboundLocalError:
        return None


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    try:
        for row in table:
            if sale_id == row[0]:
                result = row[6]
        return result
    except UnboundLocalError:
        return None


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    table = data_manager.get_table_from_file('sales/sales.csv')
    return get_all_customer_ids_from_table(table)


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    customer_ids = set({})
    for row in table:
        customer_ids.add(str(row[6]))
    return customer_ids

def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """
    table = data_manager.get_table_from_file(file_name = 'sales/sales.csv')
    return get_all_sales_ids_for_customer_ids_from_table(table)
    # your code


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    sales_ids_for_costumers = {}
    for row in table:
        costumer_id = row[6]
        if costumer_id in sales_ids_for_costumers.keys():
            sales_ids = sales_ids_for_costumers[costumer_id]
            sales_ids.append(row[0])
            sales_ids_for_costumers[costumer_id] = sales_ids
        else:
            sales_ids_for_costumers[costumer_id]= [row[0]]
    return sales_ids_for_costumers
            

    # your code


def get_num_of_sales_per_customer_ids():
    """

     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
    table = data_manager.get_table_from_file(file_name = 'sales/sales.csv')
    
    list_of_ids = [list_[-1] for list_ in table] #7=last element of sales list
    dict_of_ids = {}
    for i in list_of_ids:
        if i in dict_of_ids:
            dict_of_ids[i] += 1
        else:
            dict_of_ids[i] = 1
    
    return dict_of_ids
   

def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
    list_of_ids = [list_[-1] for list_ in table] #7=last element of sales list
    dict_of_ids = {}
    for i in list_of_ids:
        if i in dict_of_ids:
            dict_of_ids[i] += 1
        else:
            dict_of_ids[i] = 1
    

    return dict_of_ids

    # your code

def import_data_manager_customers():
    customer_table = data_manager.get_table_from_file(file_name = 'crm/customers.csv')

    return customer_table

