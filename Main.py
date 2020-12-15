# ------------------------------------------------------------------------ #
# Title: Assignment 09 - Main Module
# Description: The main file for working with modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# KSanchez,2020-12-10,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Done
if __name__ == "__main__":
    import DataClasses as D
    import ProcessingClasses as P
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Done
lstTable = []

try:
    # Load data from file into a list of employee objects when script starts
    lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
    lstTable.clear()
    for line in lstFileData:
        lstTable.append(D.Employee(line[0], line[1], line[2].strip()))

    while True:
        # Show user a menu of options
        Eio.print_menu_items()

        # Get user's menu option choice
        strChoice = Eio.input_menu_options()
        if strChoice.strip() == "1":
            # Show user current data in the list of employee objects
            Eio.print_current_list_items(lstTable)
            continue
        elif strChoice.strip() == "2":
            # Let user add data to the list of employee objects
            lstTable.append(Eio.input_employee_data())
            continue
        elif strChoice.strip() == "3":
            # let user save current data to file
            P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
            continue
        elif strChoice.strip() == "4":
            # Let user exit program
            break
except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep="\n")

# Main Body of Script  ---------------------------------------------------- #
