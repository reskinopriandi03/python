import csv
from inventory import Inventory

def add_item(List_item, csv_path):
    while True:
        itemName = input("Fill Item Name : ")
        if itemName.isalpha():
             # Check if the name already exists
            if any(item.getItemName() == itemName for item in List_item.values()):
                print("the name already exist")
                continue
            break
        else:
            print("Invalid input. Item Name should only contain letters.")
    while True:
        idNumber = input("Fill Id Number : ")
        if idNumber.isnumeric():
            # Check if the ID already exists
            if idNumber in List_item:
                print("the id already exist")
                continue
            break
        else:
            print("Invalid input. Id Number should only contain numbers.")
    while True:
        quantity = input("Fill Quantity  : ")
        if quantity.isdigit():
            break
        else:
            print("Invalid input. Quantity should be a positive number.")
    while True:
        price = input("Fill price     : ")
        if price.isdigit():
            break
        else:
            print("Invalid input. Price should be a valid number.")
    
    Item = Inventory(itemName, idNumber, quantity, price)
    List_item[idNumber] = Item

    with open(csv_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([len(List_item), List_item[idNumber].getItemName(), idNumber, List_item[idNumber].getQuantity(), List_item[idNumber].getPrice()])
        print("new stock update!")