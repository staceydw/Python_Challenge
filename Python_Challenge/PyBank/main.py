import csv

# Set variables
total_months = 0
total = 0
total_changes = 0
prev_value = 0
max_increase = 0
max_month = ""
min = 0
min_month = ""

# Open budget data file
csv_path = "Resources/budget_data.csv"
with open(csv_path) as data:
    reader = csv.reader(data)

# Skip the header row
    next(reader)

# Loop through each row in the dataset
    for row in reader:
        current = int(row[1])
        total_months = total_months + 1
        total = total + current
        if total_months > 1 : 
            change = current - prev_value
            total_changes = total_changes + change 
            if change > max_increase:
               
               max_increase = change
               max_month = row[0]
            
            if change < min:
               min = change
               min_month = row[0]
        prev_value = current

print("Financial Analysis")
print("---------------------------")
print("Total Months: ", total_months)
print("Total: ", total)
print("Average Change", total_changes / (total_months - 1))
print("Greatest Increase in Profits: ", max_month, max_increase)
print("Greatest Decrease in Profits: ", min_month, min)

# Export file
file_output = "Analysis/budget_data.txt"
with open(file_output,"w") as output:
    output.write(str("Financial Analysis" + ".\n"))
    output.write(str("---------------------------" + ".\n"))
    output.write(str("Total Months: " + ".\n"))
    output.write(str("Total: " + ".\n"))
    output.write(str("Average Change: " + ".\n"))
    output.write(str("Greatest Increase in Profits: " + ".\n"))
    output.write(str("Greatest Decrease in Profits: " + ".\n"))
