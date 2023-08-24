from inventory import Inventory, write_csv


def edit_price(List_item, csv_path):
    idNumber = input("Fill Id Number : ")
    if(idNumber in List_item):
        newPrice = input("Fill New Price : ")
        if int(newPrice) > 0:
            List_item[idNumber].setPrice(newPrice)    
            write_csv(csv_path, List_item)
            print("Price Updated!")
        else:
            print("no minus price")
    else:
            print("no match data")   