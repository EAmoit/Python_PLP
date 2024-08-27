def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = (discount_percent/100)*price
        final_price = price - discount_price
        return final_price
    else:
        return price

try:    
#user is prompted for input
    original_price = float(input("Please enter the original price of the item: Kshs "))
    discount_percent = float(input("Please enter the discount percentage:"))

    final_price = calculate_discount(original_price, discount_percent)
#print results
    if discount_percent >= 20:
        print(f"The price after {discount_percent}% discount is: Kshs {final_price:.2f}")
    else:
        print(f"No discount applied. The price is: {original_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")