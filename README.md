# SoloFunds-Analytics
Analytical tools for managing a lending business on Solo Funds, including data update scripts, real-time lending tracking, monthly performance analysis, and borrower strategy comparisons.

## Scripts

### 1. Data Update Script
   - **File:** [data_update_script.py](data_update_script.py)
   - **Description:** This Python script updates raw CSV data from a lending business on Solo Funds. It cleans and formats the data, adding necessary columns for later analysis.
   - **Usage:**
     ```bash
     python data_update_script.py
     ```
   - **Output:** Updated CSV file (`updated_june.csv`).

### 2. Real-Time Lending Tracking
   - **File:** [real_time_lending_tracking.py](real_time_lending_tracking.py)
   - **Description:** Track the real-time lending status, including the total amount lent, total returns, profit, return on investment (ROI), and more.
   - **Usage:**
     ```bash
     python real_time_lending_tracking.py
     ```
   - **Output:** Real-time lending metrics displayed in the console.

### 3. Monthly Performance Analysis
   - **File:** [calculate_monthly_kpis.py](calculate_monthly_kpis.py)
   - **Description:** Calculate monthly key performance indicators (KPIs) for a lending business based on updated data. Includes metrics such as loans paid back, total loans, on-time payback rate, total lent, total received, profit, and ROI.
   - **Usage:**
     ```bash
     python calculate_monthly_kpis.py
     ```
   - **Output:** Monthly KPIs displayed in the console.

### 4. Borrower Strategy Comparisons
   - **File:** [calculate_payback_rates.py](calculate_payback_rates.py)
   - **Description:** Categorize loans based on principal amounts, day of the week lent, borrower score, and tip percentage. Calculate and print payback rates for each category and range, providing insights into the repayment performance of different loan parameters.
   - **Usage:**
     ```bash
     python calculate_payback_rates.py
     ```
   - **Output:** Payback rates for different loan parameters displayed in the console.

## How to Run
1. Ensure you have Python installed on your machine.
2. Adjust file paths if your CSV files are named differently or located in different directories.
3. Run the desired script using the following command:
   ```bash
   python script_name.py

