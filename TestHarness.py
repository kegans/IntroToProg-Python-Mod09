# ---------------------------------------------------------- #
# Title: Assignment 09 - Test Harness Module
# Description: A module of tests
# ChangeLog (Who,When,What):
# KSanchez,2020-12-10,Created script
# ---------------------------------------------------------- #

if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test person class in data module
print("Testing Person class in data module:")
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
print()

# Test employee class in data module
print("Testing Employee class in data module:")
objE1 = D.Employee(1, "Bob", "Smith")
objE2 = D.Employee(2, "Sue", "Jones")
lstTable = [objE1, objE2]
for row in lstTable:
    print(row.to_string(), type(row))
print()

# Test processing module
print("Testing FileProcessor Class in processing module:")
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(D.Employee(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))
print()

# Test IO classes
print("Testing Employee IO Class in io module:")
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
