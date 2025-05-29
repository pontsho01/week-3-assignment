# Week 3 Assignment

# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Get user input for original price and discount percentage
try:
    price = float(input("Enter the original price of the item: R"))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if final_price != price:
        print(f"Discount applied! Final price: R{final_price:.2f}")
    else:
        print(f"No discount applied. Final price: R{price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
