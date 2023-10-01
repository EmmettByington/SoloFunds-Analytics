# SoloFunds-Analytics
Analytical tools for managing a lending business on Solo Funds, including data update scripts, real-time lending tracking, monthly performance analysis, and borrower strategy comparisons.

## Scripts

### 1. [Data Update Script](data_update_script.py)
- **Description:** This Python script updates raw CSV data from a lending business on Solo Funds. It cleans and formats the data, adding necessary columns for later analysis.
- **Usage:**
  ```bash
  python data_update_script.py
Output: Updated CSV file (updated_june.csv).
2. Real-Time Lending Tracking
Description: Track the real-time lending status, including the total amount lent, total returns, profit, return on investment (ROI), and more.
Usage:
bash
Copy code
python real_time_lending_tracking.py
Output: Real-time lending metrics displayed in the console.
3. Monthly Performance Analysis
Description: Calculate monthly key performance indicators (KPIs) for a lending business based on updated data. Includes metrics such as loans paid back, total loans, on-time payback rate, total lent, total received, profit, and ROI.
Usage:
bash
Copy code
python calculate_monthly_kpis.py
Output: Monthly KPIs displayed in the console.
4. Borrower Strategy Comparisons
Description: Categorize loans based on principal amounts, day of the week lent, borrower score, and tip percentage. Calculate and print payback rates for each category and range, providing insights into the repayment performance of different loan parameters.
Usage:
bash
Copy code
python calculate_payback_rates.py
Output: Payback rates for different loan parameters displayed in the console.
How to Run
Ensure you have Python installed on your machine.
Adjust file paths if your CSV files are named differently or located in different directories.
Run the desired script using the following command:
bash
Copy code
python script_name.py
View the results in the console.
Feel free to explore and modify these scripts to suit your lending business needs on Solo Funds. If you have any questions or suggestions, please don't hesitate to reach out!

csharp
Copy code

Replace `script_name.py` with the appropriate script file name when providing i
