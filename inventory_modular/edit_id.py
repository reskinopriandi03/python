from inventory import Inventory
from inventory import write_csv

def edit_id(List_item, csv_path):
    idNumber = input("Fill Id Number : ")
    if(idNumber in List_item):
        newNumber = input("Fill New Id : ")
        List_item[idNumber].setIdNumber(newNumber)
        write_csv(csv_path, List_item)
        print("Id Update!")
    else:
        print("no match data")