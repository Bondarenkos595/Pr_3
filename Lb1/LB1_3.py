sales = [
    {"продукт": "яблука", "кількість": 50, "ціна": 10},
    {"продукт": "банани", "кількість": 30, "ціна": 15},
    {"продукт": "яблука", "кількість": 20, "ціна": 10},
    {"продукт": "апельсини", "кількість": 100, "ціна": 5},
    {"продукт": "банани", "кількість": 40, "ціна": 15},
    {"продукт": "груші", "кількість": 10, "ціна": 25}
]

def calculate_total_income(sales_list):
    income_by_product = {}
    for sale in sales_list:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]
        income_by_product[product] = income_by_product.get(product, 0) + total
    return income_by_product

total_income = calculate_total_income(sales)

high_income_products = [product for product, income in total_income.items() if income > 1000]

print("Загальний дохід по продуктах:")
print(total_income)

print("\nПродукти з доходом понад 1000:")
print(high_income_products)
