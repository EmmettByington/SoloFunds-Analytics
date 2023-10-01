import csv

# Define ranges for principal amounts, day of the week, score, and tip percentage
principal_amount_ranges = [(200, 299), (300, 399)]
day_of_week_ranges = [2, 3, 4, 5, 6]
score_ranges = [(70, 74), (75, 79), (80, 84), (85, 89)]
tip_percentage_ranges = [(12.5, 12.99), (13.0, 13.49), (13.5, 13.99),
                         (14.0, 14.49), (14.5, 14.99)]

# Initialize dictionaries to hold counts of loans and paid back loans for each range
loan_counts = {}
paid_back_counts = {}

# Open the CSV file for reading
with open('updated_june.csv', mode='r') as file:
  # Create a CSV reader object
  csv_reader = csv.DictReader(file)

  # Iterate through each row in the CSV
  for row in csv_reader:
    # Extract data for each category (principal, day, score, tip)
    principal_amount = float(row["Principal Amount"].replace('$', '').replace(
        ',', ''))
    score = int(row["Score"])

    # Exclude loans with principal amounts below 200 or above 399 and score of below 70 or above 89
    if 200 <= principal_amount <= 399 and 70 <= score <= 89:
      day_of_week = int(row["Day of Week Lent"])
      tip_percentage = float(row["Tip Pct"].replace('%', ''))
      paid_back = int(row["Paid Back"])

      # Check which range each value falls into and update counts
      for principal_range in principal_amount_ranges:
        if principal_range[0] <= principal_amount <= principal_range[1]:
          principal_range_str = f'{principal_range[0]}-{principal_range[1]}'
          loan_counts.setdefault("Principal Range",
                                 {}).setdefault(principal_range_str, 0)
          paid_back_counts.setdefault("Principal Range",
                                      {}).setdefault(principal_range_str, 0)
          loan_counts["Principal Range"][principal_range_str] += 1
          if paid_back == 1:
            paid_back_counts["Principal Range"][principal_range_str] += 1

      for day_range in day_of_week_ranges:
        if day_of_week == day_range:
          day_range_str = str(day_range)
          loan_counts.setdefault("Day of Week",
                                 {}).setdefault(day_range_str, 0)
          paid_back_counts.setdefault("Day of Week",
                                      {}).setdefault(day_range_str, 0)
          loan_counts["Day of Week"][day_range_str] += 1
          if paid_back == 1:
            paid_back_counts["Day of Week"][day_range_str] += 1

      for score_range in score_ranges:
        if score_range[0] <= score <= score_range[1]:
          score_range_str = f'{score_range[0]}-{score_range[1]}'
          loan_counts.setdefault("Score Range",
                                 {}).setdefault(score_range_str, 0)
          paid_back_counts.setdefault("Score Range",
                                      {}).setdefault(score_range_str, 0)
          loan_counts["Score Range"][score_range_str] += 1
          if paid_back == 1:
            paid_back_counts["Score Range"][score_range_str] += 1

      for tip_range in tip_percentage_ranges:
        if tip_range[0] <= tip_percentage <= tip_range[1]:
          tip_range_str = f'{tip_range[0]}-{tip_range[1]}'  
          # Create a string representation of the range
          loan_counts.setdefault("Tip Percentage Range",
                                 {}).setdefault(tip_range_str, 0)
          paid_back_counts.setdefault("Tip Percentage Range",
                                      {}).setdefault(tip_range_str, 0)
          loan_counts["Tip Percentage Range"][tip_range_str] += 1
          if paid_back == 1:
            paid_back_counts["Tip Percentage Range"][tip_range_str] += 1


# Function to sort ranges within a category by the lower bound
def sort_ranges_by_lower_bound(ranges_dict):
  return sorted(ranges_dict.items(), key=lambda x: float(x[0].split('-')[0]))


# Calculate and print the payback percentage for each category and range
for category, ranges in loan_counts.items():
  sorted_ranges = sort_ranges_by_lower_bound(ranges)
  print(f'{category}:')
  for rng, loan_count in sorted_ranges:
    paid_back_count = paid_back_counts[category][rng]
    payback_percentage = (paid_back_count /
                          loan_count) * 100 if loan_count > 0 else 0
    print(f'  Range {rng}: {payback_percentage:.2f}%')
