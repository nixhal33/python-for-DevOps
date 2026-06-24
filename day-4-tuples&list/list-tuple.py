# lists and they are mutable ie: once created it's value can be changed(add or remove both can be happened)

techhaus_employees = ["kushal","sagar","bibek","nirajan","bishop","namuna"]
print("Techhaus Employees:-", techhaus_employees)
techhaus_employees.append("aayush")
print("Techhaus Employees:-", techhaus_employees)
techhaus_employees.remove("namuna")
print("Techhaus Employees:-", techhaus_employees[3])
print("Total no. of Techhaus Employees From The List:-",len(techhaus_employees))



# tuple are immutable object where we can't add or remove the list if already is created.

techhaus_interns = ("nischal","deeptanker","aarati","sanju")
print("Techhaus Interns:", (techhaus_interns[2]))



 