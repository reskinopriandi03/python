from inventory import Inventory, write_csv


def edit_stock(List_item, csv_path):
    idNumber = input("Fill Id Number : ")
    if idNumber in List_item:
        action = input("Choose '+' to add or '-' to subtract quantity : ")
        if action == "+":
            newStock = int(str(input("Fill Quantity to add : ")))
            current_quantity = int(List_item[idNumber].getQuantity())  # Konversi ke integer
            if newStock > 0:
                List_item[idNumber].setQuantity(current_quantity + newStock)  # Konversi kembali ke string
                    
                write_csv(csv_path, List_item)
                    
                print("Quantity updated!")
            else:
                print("Insufficient quantity to subtract.")
        elif action == "-":
            newStock = int(input("Fill Quantity to subtract : "))
            current_quantity = int(List_item[idNumber].getQuantity())  # Konversi ke integer
            if newStock <= current_quantity and current_quantity > 0 :
                List_item[idNumber].setQuantity(str(current_quantity - newStock))  # Konversi kembali ke string
                    
                write_csv(csv_path, List_item)
                    
                print("Quantity updated!")
            else:
                print("Insufficient quantity to subtract.")
        else:
                print("Invalid action. Please choose + or -.")
    else:
        print("No match data")