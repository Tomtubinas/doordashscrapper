import csv

grocery_list = []

def List():
    print("Enter your grocery list.\nEnter Done when you've finished adding items.")
    add_to_list = True

    while add_to_list:
        item = input("Enter an item: ")
        if item.lower() == "done":
            add_to_list = False
        else:
            grocery_list.append(item.lower())

    print("Your grocery list:")
    for item in grocery_list:
        print(item)

def Remove(grocery_list):
    print("What item do you want to remove?")
    item_to_remove = input().lower()
    if item_to_remove in grocery_list:
        grocery_list.remove(item_to_remove)
        print(f"{item_to_remove.capitalize()} removed from the list.")
    else:
        print("Item not found in the list.")

def Locate():
    with open('doordashoutput.csv', 'r', encoding='latin-1') as file:
        for line in file:
            parts = line.strip().split(', ')
            name = parts[0]
            price = parts[1]
            for item in grocery_list:
                if item.lower() in name.lower():
                    print(f"{name}, {price}")
                    print("************************************")
                    break



loop = True
while loop:
    print("Welcome to the program.\nWhat would you like to do?\n1) Make a list\n2) Remove an item\n3) Find items\n4) Exit")
    option = input()

    if option == "1":
        List()
    elif option == "2":
        Remove(grocery_list)
    elif option == "3":
        Locate()
    elif option == "4":
        loop = False
        print("Exiting the program...")
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")