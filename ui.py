""" User Interface (UI) module """

#ILYEN MÓDON KAP ADATOKAT A PRINT TABLE

def make_table():
    titles = make_title()
    first_table = [["kH14J&", "Age of Empires II", "1", "21", "2016", "in", "31", "14"], 
        ["kH38Jm&", "ARMA" ,"10", "23", "2016", "out", "40", "14"], 
        ["eH34Jd&", "Amnesia", "2", "12", "2016", "in", "400", "14"], 
        ["kH38Ju&","Age of Wonders: Shadow Magic", "3", "10", "2016", "in", "20", "12"]]
    tables = [titles] + first_table
    #print(tables)   
    return(tables)

def make_title():
    titles = ["serial", "title", "number", "sold", "sold year", "in stock", "how many sold sold item", "useless number"]
    return titles

#ILYEN MÓDON KAP ADATOKAT A PRINT TABLE

def len_of_colums():
    
    new_tableses = new_tables()
    lenght_of_items = []
    for lists in new_tableses:
        
        for item in lists:
            lenght_of_items.append(len(item))

    #print(lenght_of_items)
    lenght_of_table = len_of_table()
    composite_list = [lenght_of_items[x:x+lenght_of_table] for x in range(0, len(lenght_of_items),lenght_of_table)]
    #print (composite_list)
    
    
    
    longest_titles = []

    for i in composite_list:
        longest_titles.append(max(i))
    #print(longest_titles)

    longest_titles2 = []
    for i in longest_titles:
        i += 2
        longest_titles2.append(i)
    print(longest_titles2)
    return(longest_titles2)

def title_list():
    list_titles = ["serial", "title",]

#print(table)

def len_of_row(): #table kivéve az argumentből
    table = make_table()
    make_table()
    first_line = 0
    lenght_of_row = len(table[first_line])
    #print(lenght_of_row) #= 7
    return lenght_of_row
    

def len_of_table():
    table = make_table()
    #make_table()
    first_line = 0
    lenght_of_table = len(table)
    #print(lenght_of_table) #=5
    return lenght_of_table



#def get_max_lenght(): 

def new_tables():
    table = make_table()
    new_table = list(zip(*table))
    #print(new_table)
    return new_table

new_tables()


table = make_table()
def print_table(table, title_list):   #print_table(table, title_list)
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your goes code
    #table = make_table()
    dash_char = "-" 
    right_slash = "/"
    left_slash = "\\"
    separator = "|"
    
    longest_titles2 = len_of_colums()
            
    """
    max_widht_item_of_colums = 
    max_width_item = max([len(str(item)) for item in 
    """
    separator_line = []
    for i in longest_titles2:
        separator_line.append(i*dash_char+separator)
    #print(separator_line)

    joint_separator_line = "".join(separator_line)
    #print(joint_separator_line)
    list_separator_line = separator + joint_separator_line
    last_line = left_slash +(len(joint_separator_line)-1)*dash_char+ right_slash

    first_line = right_slash + (len(joint_separator_line)-1)*dash_char+ left_slash
    print(first_line)

    for lists in table:
        
        if lists == table[0]:
            pass
        else:
        
            print(f"\n{list_separator_line}")
        
        print(end = separator)
        for enum, item in enumerate(lists):
              
            print(item.center(longest_titles2[enum]), end= separator)
                

    print("")
    print(last_line)
    
"""
def max_(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
"""
print_table(table, title_list)


  
# 7 28 2 2 4 3 3 

len_of_colums()



#CSAK MINTA KÓD INNEN
def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
"kH14J&",