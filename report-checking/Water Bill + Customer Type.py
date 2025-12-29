customer_type = input("Enter Your Customer Type: ").capitalize()
customer_usage = int(input("Enter Your Last Month Usage: "))
bill = 0
discount = 0
if customer_type == "Domestic":
    if customer_usage <= 500:
        bill = customer_usage * 5
    elif customer_usage <= 1500:
        bill = customer_usage * 8 
        if customer_usage > 1000:
            discount = 0.05 
elif customer_type == "Commercial":
    if customer_usage <= 1000:
        bill = customer_type * 8
    elif customer_usage >= 1000 and customer_usage<= 5000:
        if customer_usage > 3000:
            discount = 0.1
    elif customer_usage > 5000:
        if customer_usage >3000:
            bill = customer_usage * 15
            discount = 0.1

total_bill = bill 
discount_amount = bill * discount
print(f"Customer type = {customer_type}.")
print(f"Your Previous Bill Is {bill}")
print(f"After Discount Your Bill Is {discount_amount}")