def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Sample predicted inputs (price, discount_percent)
predicted_cases = [
    (1000, 25),   # should apply discount
    (750, 10),    # should not apply discount
    (1500, 20),   # should apply discount
    (2000, 50),   # should apply discount
    (400, 5),     # should not apply discount
    (950, 30),    # should apply discount
]

# Simulate input and display output
for i, (price, discount_percent) in enumerate(predicted_cases, start=1):
    final_price = calculate_discount(price, discount_percent)
    
    print(f"Item {i}:")
    print(f"  Original Price: KES {price}")
    print(f"  Discount: {discount_percent}%")
    
    if discount_percent >= 20:
        print(f"  ✅ Discount applied. Final Price: KES {final_price:.2f}\n")
    else:
        print(f"  ❌ No discount applied. Final Price: KES {final_price:.2f}\n")
