inventory = {
    "яблука": 8,
    "банани": 3,
    "апельсини": 7,
    "груші": 2
}

def update_inventory(product, amount):
    if product in inventory:
        inventory[product] += amount
    else:
        inventory[product] = amount
    if inventory[product] < 0:
        inventory[product] = 0

update_inventory("яблука", -5)
update_inventory("банани", 4)
update_inventory("персики", 3)

low_stock = [product for product, qty in inventory.items() if qty < 5]

print("Оновлений склад:")
print(inventory)

print("\nПродукти з кількістю менше 5:")
print(low_stock)
