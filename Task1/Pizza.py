def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.50 if num_pizzas < 5 and delivery_required else 0
    if is_tuesday:
        pizza_price *= 0.5
    total_price = num_pizzas * pizza_price + delivery_cost
    if used_app:
        total_price *= 0.75
    return round(total_price, 2)


def calculate_order_total(prices):
    # Sort the prices in ascending order
    prices.sort()
    
    # Check if all prices are valid (positive numbers)
    if any(price <= 0 for price in prices):
        print("Please enter valid charges!")
        return None
    
    # Sum up the three highest prices (as the cheapest one is free)
    order_total = sum(prices[1:])
    
    # Calculate the discount percentage
    discount_percentage = ((sum(prices) - max(prices)) / sum(prices)) * 100
    
    return order_total, discount_percentage


def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================\n")

    try:
        num_pizzas = int(input("How many pizzas ordered? "))
        if num_pizzas <= 0:
            raise ValueError("Please enter a positive integer!")

        delivery_required = input("Is delivery required? (Y/N) ").strip().upper() == 'Y'
        is_tuesday = input("Is it Tuesday? (Y/N) ").strip().upper() == 'Y'
        used_app = input("Did the customer use the app? (Y/N) ").strip().upper() == 'Y'

        total_price = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

        print(f"\nTotal Price: £{total_price:.2f}")

        # Collect pizza charges from the user
        prices = []
        for i in range(1, 5):
            price = float(input(f"Enter Price of Pizza #{i}: "))
            prices.append(price)
        
        # Calculate order total and discount
        result = calculate_order_total(prices)
        if result:
            order_total, discount_percentage = result
            print(f"\nOrder Total is £{order_total:.2f}, a fabulous discount of {discount_percentage:.0f}%!")
    except ValueError as e:
        print(e)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()
