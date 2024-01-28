
def get_positive_integer_input(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity >= 0:
                return quantity
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_or_no_input(prompt):
    while True:
        answer = input(prompt).lower()
        if answer == 'y' or answer == 'n':
            return answer == 'y'
        else:
            print('Please answer "Y" or "N".')

def calculate_order_price(num_pizzas, requires_delivery, used_app, is_tuesday):
    pizza_price = 12  # Cost of one pizza
    delivery_cost = 2.50  # Delivery cost per order
    app_discount_percentage = 0.25  # 25% discount for app orders

    # Calculating total pizza cost
    total_pizza_cost = num_pizzas * pizza_price

    # Calculating delivery cost
    total_delivery_cost = delivery_cost if requires_delivery and num_pizzas < 5 else 0 

    # Calculating total order cost before discounts
    total_order_cost_before_discounts = total_pizza_cost + total_delivery_cost

    # Apply Tuesday discount
    total_order_cost_after_tuesday_discount = total_order_cost_before_discounts * 0.5 if is_tuesday else total_order_cost_before_discounts

    # Apply app discount
    total_order_cost = total_order_cost_after_tuesday_discount * (1 - app_discount_percentage) if used_app else total_order_cost_after_tuesday_discount

    return total_order_cost

#main program starts here
print("BPP Pizza Price Calculator")
print("==========================")

#asking user how many pizza they want
num_pizzas = get_positive_integer_input("\nHow many pizzas ordered? ")

#asking user if delivery is required
requires_delivery = get_yes_or_no_input("Is delivery required? (Y/N) ")

#user ordering on Tuesday or not
is_tuesday = get_yes_or_no_input("Is it Tuesday? (Y/N) ")

#asking if the user has ordered using BPP app
used_app = get_yes_or_no_input("Did the customer use the app? (Y/N) ")


#Calculating total price of pizzas after all the details
total_price = calculate_order_price(num_pizzas, requires_delivery, used_app, is_tuesday)

#Getting total price in £(pound)
print(f"\nTotal Price: £{total_price:.2f}")
