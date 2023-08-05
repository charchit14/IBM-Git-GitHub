def calculate_simple_interest(principal, rate, time):
    """
    Function to calculate Simple Interest.

    :param principal: The principal amount (initial investment).
    :param rate: The annual interest rate.
    :param time: The time period in years.
    :return: The simple interest amount.
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage:
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
time_period = float(input("Enter the time period in years: "))

simple_interest_result = calculate_simple_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", simple_interest_result)

