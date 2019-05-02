"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoud using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    while True:
        ui.print_menu('Data Analyser module', get_options(), 'Back to main menu')
        try:
            if choose() == 'return':
                return
        except KeyError as err:
            ui.print_error_message(str(err))


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        ui.print_result(get_the_last_buyer_name(), 'The name of the customer with the last purchase is: ')
    elif option == "2":
        ui.print_result(get_the_last_buyer_id(), 'The ID of the customer with the last purchase is: ')
    elif option == "3":
        ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(), 'The name of the customer who spent the most and the amount spent are: ')
    elif option == "4":
        ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(), "The most frequent buyer's name is: ")
    elif option == "5":
        ui.print_result(get_the_most_frequent_buyers_names(num=1), 'The ID of the customer who spent the most and the amount spent are: ')
    elif option == "6":
        ui.print_result(get_the_most_frequent_buyers_ids(num=1), "The most frequent buyer's ID is: ")
    elif option == "0":
        return 'return'
    else:
        raise KeyError("There is no such option.")


def get_options():
    options = ["Show the last buyer's name",
               "Show the last buyer's ID",
               "Show the buyer's name who spent most and the amount of money spent",
               "Show the buyer's ID who spent most and the amount of money spent ",
               "Show the most frequent's buyers' name",
               "Show the most frequent's buyers' ID"]
    return options



def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    sale_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(sale_id)
    name = crm.get_name_by_id(customer_id)
    return name



def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    sale_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(sale_id)
    return customer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    sales_data = sales.get_all_sales_ids_for_customer_ids()

    for element in sales_data.keys():
        sales_data.update({element: sales.get_the_sum_of_prices(sales_data[element])})
    
    name = crm.get_name_by_id(max(sales_data, key=sales_data.get))
    amount = sales_data[max(sales_data, key=sales_data.get)]
        
    return (name, amount) 
  


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """
    sales_data = sales.get_all_sales_ids_for_customer_ids()

    for element in sales_data.keys():
        sales_data.update({element: sales.get_the_sum_of_prices(sales_data[element])})
    
    best_buyer_id = max(sales_data, key=sales_data.get)
    amount = sales_data[max(sales_data, key=sales_data.get)]
    return (best_buyer_id, amount)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """

    # your code


    dict_of_ids = sales.get_num_of_sales_per_customer_ids()

    customer_table = sales.import_data_manager_customers()
    #customer_table = data_manager.get_table_from_file('customers/customers.csv')

    dict_of_ids_values = list(dict_of_ids.items())
    list_of_IDs = list(dict_of_ids.keys())

    dict_of_ids_values_sorted = []

    while dict_of_ids_values:
        minimum = dict_of_ids_values[0][1]
        smallest_item = dict_of_ids_values[0]  
        for x in dict_of_ids_values: 
            if x[1] < minimum:
                minimum = x[1]
                smallest_item = x
        dict_of_ids_values_sorted.append(smallest_item)
        dict_of_ids_values.remove(smallest_item) 

    tuple_of_ids = dict_of_ids_values_sorted
    
    dict_ordered = dict((y, x) for y, x in tuple_of_ids)
    

    list_of_frequent_buyers_data = []

    for i in dict_ordered:
        for j in customer_table:
            for k in j:
                if k == i:
                    list_of_frequent_buyers_data.append(j)

    
    

    tuple_list = []
    for index, j in enumerate(list_of_frequent_buyers_data):
            my_tuple = ( str(j[1]), int(list(dict_ordered.values())[index]) )
            tuple_list.append(my_tuple)

    
    reverse_tuple_list = tuple_list[::-1]

    return (reverse_tuple_list[0:num])


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # your code
    
    dict_of_ids = sales.get_num_of_sales_per_customer_ids()

    dict_of_ids_values = list(dict_of_ids.items())
    list_of_IDs = list(dict_of_ids.keys())

    dict_of_ids_values_sorted = []

    while dict_of_ids_values:
        minimum = dict_of_ids_values[0][1]
        smallest_item = dict_of_ids_values[0]  
        for x in dict_of_ids_values: 
            if x[1] < minimum:
                minimum = x[1]
                smallest_item = x
        dict_of_ids_values_sorted.append(smallest_item)
        dict_of_ids_values.remove(smallest_item) 

    tuple_of_ids = dict_of_ids_values_sorted
    
    tuple_of_ids = (tuple_of_ids[::-1]) # sorba rendezés csökkenpbe(legnagyobb jön először)

    return (tuple_of_ids[0:num])