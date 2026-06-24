# lists and they are mutable ie: once created it's value can be changed(add or remove both can be happened)

techhaus_employees = ["kushal", "sagar", "bibek", "nirajan", "bishop", "namuna"]
techhaus_interns = ("nischal", "deeptanker", "aarati", "sanju")


def print_example_data():
    print("Techhaus Employees:-", techhaus_employees)
    techhaus_employees.append("aayush")
    print("Techhaus Employees after append:-", techhaus_employees)
    techhaus_employees.remove("namuna")
    print("Techhaus Employees at index 3:-", techhaus_employees[3])
    print("Total no. of Techhaus Employees From The List:-", len(techhaus_employees))
    print("Techhaus Interns:-", techhaus_interns)
    print("Techhaus Intern at index 2:-", techhaus_interns[2])


if __name__ == "__main__":
    print_example_data()



 