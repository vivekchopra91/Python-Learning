# list1 = ["Jalandhar", "Ludhiana", "Amritsar", "Patiala", "Bathinda", "Moga", "Ropar", "Mohali", "Phagwara", "Guraya", "Phillaur"]
# i = 0
# for cities in list1:
#     i+=1
#     print( i, cities)

list2 = [["Rohit", 85], ["Rahul", 89], ["Param", 75], ["Jeet", 90]]
for name, marks in list2:
    print("Student 1 is :", [name], "and his marks in last test is :", [marks])

dict1 = dict(list2)
# print(dict1)
for student, percentage in dict1.items():
    print(student, "and his '%' is :", percentage)



# Quiz: print only numeric items from a list
l2 = ["Sham", "Raju", 66, 4, 3, 80, 90, "Babu rao"]
for item in l2:
    if str(item).isnumeric() and item >6:
        print(item)
    


# using else with for loop: 
l1 = ["sham", "raju", "babu-rao", "chin-chim-chu"]
for item in l1:
    # print(item, end=" ")
    # print(item)
    if item == "where":
        break
else:               # else statement only gets passed if for loop ends normally, otherwise it will not execute else statement
    print("\nThis for loop ended.")