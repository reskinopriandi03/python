import csv
import os

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

def read_csv(csv_path):
    List_item = {}
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Lewati baris judul kolom
        for row in csv_reader:
            item = Inventory(row[1], row[2], row[3], row[4])
            List_item[row[2]] = item
    return List_item

def write_csv(csv_path, List_item):
    rows_to_write = [["No.", "Item", "ID", "Quantity", "Price"]]
    for index, item in enumerate(List_item.values(), start=1):
        rows_to_write.append([index, item.getItemName(), item.getId(), item.getQuantity(), item.getPrice()])
    with open(csv_path, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(rows_to_write)
