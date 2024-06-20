def calculate_discount(price, discount_percent):
    if discount_percent >= 20 and discount_percent <= 100:
        return ((discount_percent/100)*price)
    else:
        return price

price = int(input("Enter the price of your product: "))
discount_percent = int(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)
print (f"Final price of product after applying {discount_percent} is {final_price}")

