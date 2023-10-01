# SoloFunds-Analytics
Analytical tools for managing a lending business on Solo Funds, including data update scripts, real-time lending tracking, monthly performance analysis, and borrower strategy comparisons.

## Scripts

### 1. Data Update Script
   - **File:** [raw_data_processor.py](raw_data_processor.py)
   - **Description:** This Python script updates raw CSV data from a lending business on Solo Funds. It cleans and formats the data, adding necessary columns for later analysis.
   - **Usage:**
     ```bash
     python raw_data_processor.py
     ```
   - **Output:** Updated CSV file (`updated_june.csv`).

### 2. Real-Time Lending Tracking
   - **File:** [calculate_open_totals.py](calculate_open_totals.py)
   - **Description:** Track the real-time lending status, including the total amount lent, total returns, profit, return on investment (ROI), and more.
   - **Usage:**
     ```bash
     python calculate_open_totals.py
     ```
   - **Output:** Real-time lending metrics displayed in the console.
     - **Example** Total Open Dollars: $27932.96 Total Open Loans: 114

### 3. Monthly Performance Analysis
   - **File:** [calculate_monthly_kpis.py](calculate_monthly_kpis.py)
   - **Description:** Calculate monthly key performance indicators (KPIs) for a lending business based on updated data. Includes metrics such as loans paid back, total loans, on-time payback rate, total lent, total received, profit, and ROI.
   - **Usage:**
     ```bash
     python calculate_monthly_kpis.py
     ```
   - **Output:** Monthly KPIs displayed in the console.
     - **Example** Loans Paid Back: 106
Total Loans: 137
On Time Payback Rate: 77.37%
Total Lent: $39019.49
Total Received: $40207.34
Profit: $1187.85
Monthly ROI: 6.14%
Yearly ROI: 104.43%
Capital Use: 2.02 times

### 4. Borrower Strategy Comparisons
   - **File:** [calculate_payback_rates.py](calculate_payback_rates.py)
   - **Description:** Categorize loans based on principal amounts, day of the week lent, borrower score, and tip percentage. Calculate and print payback rates for each category and range, providing insights into the repayment performance of different loan parameters.
   - **Usage:**
     ```bash
     python calculate_payback_rates.py
     ```
   - **Output:** Payback rates for different loan parameters displayed in the console.
     - **Example**   Principal Range:
  Range 200-299: 76.84%
  Range 300-399: 78.57%
Day of Week:
  Range 2: 59.09%
  Range 3: 90.48%
  Range 4: 94.74%
  Range 5: 78.95%
  Range 6: 67.65%
Score Range:
  Range 70-74: 80.39%
  Range 75-79: 76.00%
  Range 80-84: 75.68%
  Range 85-89: 75.00%
Tip Percentage Range:
  Range 12.5-12.99: 75.00%
  Range 13.0-13.49: 92.00%
  Range 13.5-13.99: 62.07%
  Range 14.0-14.49: 78.95%
  Range 14.5-14.99: 77.78%

## How to Run
1. Ensure you have Python installed on your machine.
2. Adjust file paths if your CSV files are named differently or located in different directories.
3. Run the desired script using the following command:
   ```bash
   python calculate_monthly_kpis.py
   python calculate_open_totals.py
   python calculate_payback_rates.py
   python raw_data_processor.py

