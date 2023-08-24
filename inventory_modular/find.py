from inventory import Inventory

def find(List_item):
    idNumber = input("Fill Id Number : ")
    if (idNumber in List_item):
        print("Item Name : ", List_item[idNumber].getItemName())
        print("Id Number : ", List_item[idNumber].getId())
        print("quantity : ", List_item[idNumber].getQuantity())
        print("price : ", List_item[idNumber].getPrice())
    else:
            print("no match data")