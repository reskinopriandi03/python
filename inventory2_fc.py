class Inventory:
    def __init__(self, itemName, idNumber, quantity, price):
        self.itemName = str(itemName)
        self.idNumber = str(idNumber)
        self.quantity = str(quantity)
        self.price = str(price)

    def getItemName(self):
        return self.itemName
    def getId(self):
        return self.idNumber
    def getQuantity(self):
        return self.quantity
    def getPrice(self):
        return self.price
        
    def setItemName(self, itemName):
        self.itemName = itemName
    def setIdNumber(self, idNumber):
        self.idNumber = idNumber
    def setQuantity(self, quantity):
        self.quantity = quantity
    def setPrice(self, price):
        self.price = price

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
print("     7. Edit Stock         =")
print("     8. Edit Price         =")
print("     9. Total Item         =")
print("     0. Exit               =")
print("=====================================")

while(loop):
    print("\n\n")
    menu = input("Choose please  : ")
    if menu == "1":
        while True:
            itemName = input("Fill Item Name : ")
            if itemName.isalpha():  # "to make sure it only contains alphabet or letters"
                break
            else:
                print("Invalid input. Item Name should only contain letters.")
        while True:
            idNumber = input("Fill Id Number : ")
            if idNumber.isnumeric():  # "to make sure it only contains numerical"
                break
            else:
                print("Invalid input. Id Number should only contain numbers.")
        while True:
            quantity = input("Fill Quantity  : ")
            if quantity.isdigit():  # "to make sure it only contains positive numerical"
                break
            else:
                print("Invalid input. Quantity should be a positive number.")
        while True:
            price = input("Fill price     : ")
            if price.isdigit():  # Memeriksa apakah hanya terdiri dari angka, termasuk desimal
                break
            else:
                print("Invalid input. Price should be a valid number.")
        Item = Inventory(itemName, idNumber, quantity, price)
        List_item[idNumber] = Item
        print("new stock update!")
    elif menu == "2":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            del List_item[idNumber]
            print("stock update")
        else:
            print("no match data")
    elif menu == "3":
        total_value = 0  #prepare to set inventaris value
        for x in List_item:
            print("Item Name      : ", List_item[x].getItemName())
            print("Id Number      : ", List_item[x].getId())
            print("quantity       : ", List_item[x].getQuantity())
            print("price          : ", List_item[x].getPrice())
            item_value = int(List_item[x].getQuantity()) * int(List_item[x].getPrice())  # count value
            print("total value    : ", item_value)
            print("-----------------------------")
            total_value += item_value  # add value to total value
        print("Total Inventory Value : ", total_value)
    elif menu == "4":
        idNumber = input("Fill Id Number : ")
        if (idNumber in List_item):
            print("Item Name : ", List_item[idNumber].getItemName())
            print("Id Number : ", List_item[idNumber].getId())
            print("quantity : ", List_item[x].getQuantity())
            print("price : ", List_item[x].getPrice())
        else:
            print("no match data")
    elif menu == "5":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            newName = input("Fill New Name : ")
            List_item[idNumber].setItemName(newName)
            print("Name Update!")
        else:
            print("no match data")
    elif menu == "6":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            newNumber = input("Fill New Id : ")
            List_item[idNumber].setIdNumber(newNumber)
            print("Id Update!")
        else:
            print("no match data")
    elif menu == "7":
        idNumber = input("Fill Id Number : ")
        if idNumber in List_item:
            action = input("Choose '+' to add or '-' to subtract quantity : ")
            if action == "+":
                newStock = int(str(input("Fill Quantity to add : ")))
                current_quantity = int(List_item[idNumber].getQuantity())  # Konversi ke integer
                if newStock > 0:
                    List_item[idNumber].setQuantity(current_quantity + newStock)  # Konversi kembali ke string
                    print("Quantity updated!")
                else:
                    print("Insufficient quantity to subtract.")
            elif action == "-":
                newStock = int(input("Fill Quantity to subtract : "))
                current_quantity = int(List_item[idNumber].getQuantity())  # Konversi ke integer
                if newStock <= current_quantity and current_quantity > 0 :
                    List_item[idNumber].setQuantity(str(current_quantity - newStock))  # Konversi kembali ke string
                    print("Quantity updated!")
                else:
                    print("Insufficient quantity to subtract.")
            else:
                print("Invalid action. Please choose + or -.")
        else:
            print("No match data")
    elif menu == "8":
        idNumber = input("Fill Id Number : ")
        if(idNumber in List_item):
            newPrice = input("Fill New Price : ")
            if newPrice > 0:
                List_item[idNumber].setPrice(newPrice)
                print("Price Updated!")
            else:
                print("no minus price")
        else:
            print("no match data")    
    elif menu == "9":
        print("Total Items : ", len(List_item))
    elif menu == "0":
        print("thank you for using our inventory app")
        loop = False
    else:
        print("Invalid input. Please choose a valid option.")

