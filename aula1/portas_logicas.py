from linear_algebra import dot

options = [0,1,2,3,4]

def get_option():
    try:
        option = input("Select a boolean function.\n0 = AND\n1 = OR\n2 = NE\n3 = NOU\n4 = FINISH\nSelection: ")
        int_option = int(option)
        if int_option in options:
            return int_option, get_port_name(int_option)
        else:
            print(f"\"{int_option}\" isn't a valid choice!\n")
            return -1, ""
    except:
        print("You choose an invalid choice!!!\n")
        return -1, ""

def get_port_name(selection):
    if selection == 0:
        return "AND"
    elif selection == 1:
        return "OR"
    elif selection == 2:
        return "NE"
    elif selection == 3:
        return "NOU"
    else:
        return ""

def step_function(x, selection):
    if selection == 0:
        return port_and(x)
    elif selection == 1:
        return port_or(x)
    elif selection == 2:
        return port_ne(x)
    elif selection == 3:
        return port_nou(x)
    else:
        return 0

    
def port_and(x):
    return 1 if x >= 1.5 else 0

def port_or(x):
    return 1 if x > 0 else 0

def port_ne(x):
    return 0 if x >= 1.5 else 1

def port_nou(x):
    return 0 if x > 0 else 1

def perceptron_output(weights, bias, x, selection):
    calculation = dot(weights, x) + bias
    return step_function(calculation, selection)

def execute():
    selection = -1
    port_name = ""
    while selection < 0:
        selection, port_name = get_option()
    
    if selection == 4:
        print("program finished")
        return

    x0 = [0,0]
    x1 = [0,1]
    x2 = [1,0]
    x3 = [1,1]

    weights = [1,1]
    bias = 0

    saida0 = perceptron_output(weights, bias, x0, selection)
    saida1 = perceptron_output(weights, bias, x1, selection)
    saida2 = perceptron_output(weights, bias, x2, selection)
    saida3 = perceptron_output(weights, bias, x3, selection)

    print(f"PERCEPTRON IMPLEMENTANDO FUNCAO BOOLEANA {port_name}")
    print(f"0 {port_name} 0 = {saida0}")
    print(f"0 {port_name} 1 = {saida1}")
    print(f"1 {port_name} 0 = {saida2}")
    print(f"1 {port_name} 1 = {saida3}")
    execute()

execute()