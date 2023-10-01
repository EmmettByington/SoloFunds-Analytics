import csv

# Initialize a list to hold the data
data = []

# Open the CSV file for reading
with open('updated_june.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

# Initialize the variables
starting_capital = 19336
total_lent = 0
total_received = 0
on_time_loans = 0
total_loans = 0

# Iterate through each row in the data
for row in data:
    # Extract the loan amount from the 'Total loan amount' column and clean/format it
    Total_loan_amount = float(row["Total Loan Amount"].replace('$', '').replace(',', '').strip())

    # Extract the received amount from 'Total Returns' column and clean/format it
    Total_returns = float(row["Total Returns"].replace('$', '').replace(',', '').strip())

    # Extract the on time and total loans
    on_time_loans += int(row["Paid Back"].strip())
    total_loans += int(row["Fulfilled Loan"].strip())

    # Add the amounts to the totals
    total_lent += Total_loan_amount
    total_received += Total_returns

# Format totals to 2 decimal places
formatted_total_lent = round(total_lent, 2)
formatted_total_received = round(total_received, 2)

# Calculate profit, payback rate, monthly roi, yearly roi, and capital use
profit = round((formatted_total_received - formatted_total_lent), 2)
monthly_return = round(profit / starting_capital * 100, 2)
future_value = starting_capital * ((1 + (monthly_return / 100)) ** 12)
yearly_return = round(((future_value - starting_capital) / starting_capital * 100), 2)
payback_rate = round((on_time_loans / total_loans * 100), 2)
capital_use = round((total_lent / starting_capital), 2)

# Print the findings
print('---')
print(f'Loans Paid Back: {on_time_loans}')
print(f'Total Loans: {total_loans}')
print(f'On Time Payback Rate: {payback_rate}%')
print(f'Total Lent: ${formatted_total_lent}')
print(f'Total Received: ${formatted_total_received}')
print(f'Profit: ${profit}')
print(f'Monthly ROI: {monthly_return}%')
print(f'Yearly ROI: {yearly_return}%')
print(f'Capital Use: {capital_use} times')
print('---')
