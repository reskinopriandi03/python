class Inventory:
    def __init__(self, itemName, idNumber):
        self.itemName = str(itemName)
        self.idNumber = str(idNumber)

    def getItemName(self):
        return self.itemName
    def getId(self):
        return self.idNumber
        
    def setItemName(self, itemName):
        self.itemName = itemName

    def setIdNumber(self, idNumber):
        self.idNumber = idNumber


List_item = {}
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
print("     7. Total Item         =")
print("     0. Exit               =")
print("=====================================")

while(loop):
    print("\n\n")
    menu = input("Choose please : ")
    if menu == "1":
        itemName = input("Fill Item Name : ")
        idNumber = input("Fill Id Number : ")
        Item = Inventory(itemName, idNumber)
        List_item[idNumber] = Item
    elif menu == "2":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            del List_item[idNumber]
        else:
            print("no match data")
    elif menu == "3":
        for x in List_item:
            print("Item Name : ", List_item[x].getItemName())
            print("Id Number : ", List_item[x].getId())
    elif menu == "4":
        idNumber = input("Fill Id Number : ")
        if (idNumber in List_item):
            print("Item Name : ", List_item[itemName].getItemName())
            print("Id Number : ", List_item[idNumber].getId())
        else:
            print("no match data")
    elif menu == "5":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            newName = input("Fill New Name : ")
            List_item[newName].setItemName(newName)
        else:
            print("no match data")
    elif menu == "6":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            newNumber = input("Fill New Id : ")
            List_item[idNumber].setIdNumber(newNumber)
        else:
            print("no match data")
    elif menu == "7":
        print("Total Items : ", len(List_item))
    elif menu == "0":
        loop = False
    else:
        print("error inside")
