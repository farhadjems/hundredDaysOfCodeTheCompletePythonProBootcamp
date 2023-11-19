
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        # return
        return "inputs are not valid" 
    
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    name = formatted_f_name + " " +formatted_l_name
    # print(name)
    return name


print(format_name("FARHAD", "JEMS"))