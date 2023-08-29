import csv
import os
from inventory import Inventory, read_csv, write_csv
from add_item import add_item
from show_list import show_list
from find import find
from edit_name import edit_name
from edit_id import edit_id
from edit_stock import edit_stock
from edit_price import edit_price

csv_file = "inventory.csv"  # setted to store output user
csv_path = os.path.join(os.path.dirname(__file__), csv_file)
# Cek apakah file CSV sudah ada atau belum
csv_exists = os.path.exists(csv_path)

# Tambahkan judul jika file CSV belum ada
if not csv_exists:
    with open(csv_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Item", "ID", "Quantity", "Price"])

List_item = read_csv(csv_path)
loop = True

print("====================================")
print("          Inventory app             ")
print("====================================")
print("                MENU                ")
print("     1. Add Item           =")
print("     2. Delete Item        =")
print("     3. Show List Item     =")
print("     4. Find Item          =")
print("     5. Edit Item Name     =")
print("     6. Edit Id Number     =")
print("     7. Edit Stock         =")
print("     8. Edit Price         =")
print("     9. Total Item         =")
print("     0. Exit               =")
print("=====================================")

while(loop):
    print("\n\n")
    menu = input("Choose please  : ")
    if menu == "1":
        add_item(List_item, csv_path)

    elif menu == "2":
        idNumber = input("Fill Id Number : ")
        if idNumber in List_item:
            del List_item[idNumber]
            write_csv(csv_path, List_item)
            print("stock update")
    elif menu == "3":
        show_list(List_item)
    elif menu == "4":
        find(List_item)
    elif menu == "5":
        edit_name(List_item, csv_path)
    elif menu == "6":
        edit_id(List_item, csv_path)
    elif menu == "7":
        edit_stock(List_item, csv_path)
    elif menu == "8":
         edit_price(List_item, csv_path)
    elif menu == "9":
        print("Total Items : ", len(List_item))
    elif menu == "0":
        print("thank you for using our inventory app")
        loop = False
    else:
        print("Invalid input. Please choose a valid option.")
