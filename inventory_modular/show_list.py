from inventory import Inventory

def show_list(List_item):
    total_value = 0
    for index, item in enumerate(List_item.values(), start=1):
        print("Item Name      : ", item.getItemName())
        print("Id Number      : ", item.getId())
        print("quantity       : ", item.getQuantity())
        print("price          : ", item.getPrice())
        item_value = int(item.getQuantity()) * int(item.getPrice())
        print("total value    : ", item_value)
        print("-----------------------------")
        total_value += item_value

    print("Total Inventory Value : ", total_value)
