# References https://www.youtube.com/watch?v=k8asfUbWbI4

import datetime
import calendar

# Constants
balance = 5000
interest_rate = 13 * 0.01  # As a percent
monthly_payment = 500

# Getting data about days in current month
today = datetime.date.today()
# returns (day of week of first day of month, number of days in month)
monthrange = calendar.monthrange(today.year, today.month)
print(f"\nmonthrange evaluates to: {monthrange}")
# Can extract just one value of return statement
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
print(f"Days in current month: {days_in_current_month}")
days_till_end_month = days_in_current_month - today.day
print(f"Days until end of month: {days_till_end_month}")

# Start date via time delta and init end_date
start_date = today + datetime.timedelta(days=days_till_end_month + 1)
print(f"Start date: {start_date}")
end_date = start_date

# Pay off until balance is 0
while balance > 0:
    interest_charge = (interest_rate / 12) * balance  # Annual in month
    balance += interest_charge
    balance -= monthly_payment
    # Ternary operator: round to 2 decimal places while pos balance
    balance = 0 if balance < 0 else round(balance, 2)
    print(end_date, balance)
    # Correct end date to beginning of next month
    days_in_current_month = \
        calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)
