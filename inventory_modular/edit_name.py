from inventory import Inventory
from inventory import write_csv



def edit_name(List_item, csv_path):
    idNumber = input("Fill Id Number : ")
    if(idNumber in List_item):
        newName = input("Fill New Name : ")
        List_item[idNumber].setItemName(newName)
            
        write_csv(csv_path, List_item)
            
        print("Name Update!")
    else:
        print("no match data")