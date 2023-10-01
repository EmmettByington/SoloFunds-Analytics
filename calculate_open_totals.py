import csv

# initialize a counter for amounts
total_principal = 0
total_donation = 0
total_slp = 0
total_funded = 0

# Open the CSV file for reading
with open('open_9_29.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    # iterate through each row to find if the loan is open
    for row in csv_reader:
        if row["Loan Status"] == "Funded":
            total_funded += 1

            # Extract the "Principal Amount" and "Donation Amount" columns, remove '$' and ',', and convert to floats
            principal_amount = float(row["Principal Amount"].replace('$', '').replace(',', ''))
            donation_amount = float(row["Donation Amount"].replace('$', '').replace(',', ''))

            # Calculate the SLP Amount (Principal Amount * 0.05)
            slp_amount = principal_amount * 0.05

            # Add the Principal Amount, Donation Amount, SLP Amount, and total to the respective totals
            total_principal += principal_amount
            total_donation += donation_amount
            total_slp += slp_amount
            total_lent = total_principal + total_donation + total_slp

# Format the total lent and total SLP with two decimal places
formatted_total_lent = round(total_lent, 2)
formatted_total_funded = int(total_funded)

# Print the formatted totals
print(f'Total Open Dollars: ${formatted_total_lent:.2f}')
print(f'Total Open Loans: {formatted_total_funded}')
