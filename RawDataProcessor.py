import numpy as np
import pandas as pd

# Read in loans file
df = pd.read_csv('june.csv')

# Delete un-needed columns
df.drop(columns=['Late Fee', 'Recovery Fee'], inplace=True)

# Add new columns with default values
df['Slp Amount'] = 0.0
df['Total Loan Amount'] = 0.0
df['Tip Pct'] = 0.0
df['Day of Week Lent'] = 0
df['Day of Week Due'] = 0
df['Paid Back'] = 0
df['Fulfilled Loan'] = 0

# Format columns for calculations
df['Principal Amount'] = df['Principal Amount'].str.replace('$', '').astype(float)
df['Donation Amount'] = df['Donation Amount'].str.replace('$', '').astype(float)
df['Tip Amount'] = df['Tip Amount'].str.replace('$', '').astype(float)

# Calculate Slp Amount
df['Slp Amount'] = 0.05 * df['Principal Amount']

# Calculate Total Loan Amount
df['Total Loan Amount'] = df['Principal Amount'] + df['Donation Amount'] + df['Slp Amount']
# Format the 'Total Loan Amount' column
df['Total Loan Amount'] = df['Total Loan Amount'].map('${:.2f}'.format)

# Format the 'Slp Amount' column
df['Slp Amount'] = df['Slp Amount'].map('${:.2f}'.format)

# Calculate Tip Pct
df['Tip Pct'] = df['Tip Amount'] / df['Principal Amount'] * 100
# Format the 'Tip Pct' column
df['Tip Pct'] = df['Tip Pct'].map('{:.2f}%'.format)

# Fill 'Payback Date' with 'Due Date' + 1 day if it's empty
df['Payback Date'] = df['Payback Date'].fillna((pd.to_datetime(df['Due Date']) + pd.DateOffset(days=1)).dt.date)

# Convert date columns to datetime format
date_columns = ['Origination Date', 'Due Date', 'Payback Date']
df[date_columns] = df[date_columns].apply(pd.to_datetime)

# Calculate Day of Week Lent and Day of Week Due
df['Day of Week Lent'] = pd.to_datetime(df['Origination Date']).dt.dayofweek + 2
df['Day of Week Due'] = pd.to_datetime(df['Due Date']).dt.dayofweek + 2
# Apply a condition to set the value to 1 if it's equal to 8
df.loc[df['Day of Week Lent'] == 8, 'Day of Week Lent'] = 1
df.loc[df['Day of Week Due'] == 8, 'Day of Week Due'] = 1

# Calculate Paid Back
df['Paid Back'] = np.where(df['Loan Status'] == 'Paid back', 1, 0)

# Calculate Fulfilled Loan
df['Fulfilled Loan'] = np.where(df['Principal Amount'] > 0, 1, 0)

# Format columns back to original
df['Principal Amount'] = df['Principal Amount'].map('${:.2f}'.format)
df['Donation Amount'] = df['Donation Amount'].map('${:.2f}'.format)
df['Tip Amount'] = df['Tip Amount'].map('${:.2f}'.format)

# Define the desired column order
desired_column_order = [
    'Origination Date',
    'Due Date',
    'Payback Date',
    'Borrower Name',
    'Loan Status',
    'Collections Status',
    'Principal Amount',
    'Slp Amount',
    'Donation Amount',
    'Total Loan Amount',
    'Tip Amount',
    'Tip Pct',
    'SLP?',
    'Score',
    'Credits Received',
    'Total Returns',
    'Day of Week Lent',
    'Day of Week Due',
    'Paid Back',
    'Fulfilled Loan'
]

# Reorder the columns in the DataFrame
df = df[desired_column_order]

# Write the updated DataFrame to a new CSV file
df.to_csv('updated_june.csv', index=False)

