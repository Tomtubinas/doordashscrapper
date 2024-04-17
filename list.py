import csv

grocery_list = []

def Print():
    n = 1
    print("Your grocery list:")
    for item in grocery_list:
        print(f"{n}) {item}")
        n += 1

def List():
    print("Enter your grocery list.\nEnter Done when you've finished adding items.")
    add_to_list = True

    while add_to_list:
        item = input("Enter an item: ")
        if item.lower() == "done":
            add_to_list = False
        else:
            Locate(item)
    Print()

def Remove(grocery_list):
    Print()
    item_to_remove = int(input("What item do you want to remove?")) - 1
    if item_to_remove < len(grocery_list):
        grocery_list.pop(item_to_remove)
        print("Item removed from the list.")
    else:
        print("Item not found in the list.")
    Print()

def Locate(item):
    search = []
    with open('doordashoutput.csv', 'r', encoding='latin-1') as file:
        for line in file:
            parts = line.strip().split(', ')
            name = parts[0]
            price = parts[1]
            if item.lower() in name.lower():
                search.append((name, price))
    n = 1
    for results in search:
        print(f"{n}) {results[0]}, {results[1]}")
        n += 1
    add = input("What item do you want to add to your cart?")
    add = int(add) - 1
    print(search[int(add)])
    addToList = search[add]
    grocery_list.append(addToList)



loop = True
while loop:
    print("Welcome to the program.\nWhat would you like to do?\n1) Make a list\n2) Remove an item\n3) Exit")
    option = input()
    if option == "1":
        List()
    elif option == "2":
        Remove(grocery_list)
    elif option == "3":
        loop = False
        print("Exiting the program...")
    else:
        print("Invalid option. Please enter 1, 2, or 3")
